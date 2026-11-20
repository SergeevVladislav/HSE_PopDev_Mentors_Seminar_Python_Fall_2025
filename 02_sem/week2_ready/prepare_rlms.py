"""Create a local 2024 teaching extract from an RLMS-HSE individual Stata file.

Usage: python prepare_rlms.py --input /path/to/RLMS_IND_1994_2025_eng_DTA.7z
Download the English individual data yourself from https://www.hse.ru/en/rlms/downloads.
The input is never modified. Microdata and local provenance must not be uploaded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

import pandas as pd
import py7zr
import pyreadstat

ROOT = Path(__file__).resolve().parent
RENAME = {
    "year": "year", "age": "age", "h5": "sex_code", "j1": "work_status",
    "j10": "earnings_rub", "j6_2": "hours_week", "diplom": "education_code",
    "inwgt": "person_weight",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def prepare(stata: Path, source: Path) -> None:
    _, meta = pyreadstat.read_dta(str(stata), metadataonly=True)
    required = set(RENAME) | {"idind"}
    missing = required - set(meta.column_names)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}. Use English longitudinal IND data.")
    # Refuse a different variable definition instead of silently relabelling it.
    expected = {"j10": "AFTER-TAX WAGES LAST 30D", "j6_2": "HRS IN AVERAGE WORKWEEK",
                "h5": "RESPONDENT GENDER", "diplom": "COMPLETED EDUCATION"}
    for name, fragment in expected.items():
        if fragment not in (meta.column_names_to_labels[name] or "").upper():
            raise ValueError(f"Unexpected {name} label. Check the current RLMS codebook before proceeding.")
    print("Reading selected variables; this may take a few minutes.", flush=True)
    data, _ = pyreadstat.read_dta(str(stata), usecols=sorted(required),
                                 apply_value_formats=False)
    selected = data.loc[data["year"].eq(2024)].copy()
    if selected.empty:
        raise ValueError("The file has no observations for 2024.")
    if selected["idind"].isna().any() or selected["idind"].duplicated().any():
        raise ValueError("Person IDs are missing or duplicated within 2024; inspect the source.")
    result = selected[list(RENAME)].rename(columns=RENAME)
    output = ROOT / "data" / "rlms_2024_earnings.csv"
    output.parent.mkdir(exist_ok=True)
    if output.exists():
        old = pd.read_csv(output)
        if not old.equals(result.reset_index(drop=True)):
            raise FileExistsError(f"A different extract already exists at {output}. Rename it first.")
    result.to_csv(output, index=False)
    provenance = {
        "source": "RLMS-HSE English longitudinal individual data", "year": 2024,
        "source_filename": source.name, "source_sha256": sha256(source),
        "source_url": "https://www.hse.ru/en/rlms/downloads", "rows": len(result),
        "columns": RENAME, "extract_sha256": sha256(output),
        "source_labels": {key: meta.column_names_to_labels[key] for key in RENAME},
        "source_value_labels": {key: meta.variable_value_labels.get(key, {}) for key in RENAME},
        "transformations": ["Keep year 2024", "Verify one record per person",
                            "Select and rename columns", "Remove person identifiers"],
        "missing_values": "Original numeric response codes are retained; Stata missing becomes blank.",
    }
    (output.parent / "rlms_local_provenance.json").write_text(
        json.dumps(provenance, indent=2), encoding="utf-8")
    print(f"Ready: {output.name}; {len(result):,} rows, {len(result.columns)} columns.")
    print("Keep the CSV, raw file and local provenance on your computer; publish code and aggregate results.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="English longitudinal IND .7z or .dta")
    args = parser.parse_args()
    source = args.input.expanduser().resolve()
    if not source.is_file():
        parser.error(f"File does not exist: {source}")
    if source.suffix.lower() == ".dta":
        prepare(source, source)
        return
    if source.suffix.lower() != ".7z":
        parser.error("Use a .7z archive or an extracted .dta file.")
    with tempfile.TemporaryDirectory(prefix="popdev_rlms_") as temp:
        with py7zr.SevenZipFile(source) as archive:
            candidates = [item for item in archive.list()
                          if item.filename.lower().endswith(".dta")
                          and "ind" in Path(item.filename).name.lower()]
            if len(candidates) != 1:
                raise ValueError("Expected one individual Stata file. Extract it manually and pass --input file.dta.")
            item = candidates[0]
            destination = (Path(temp) / item.filename).resolve()
            if not destination.is_relative_to(Path(temp).resolve()):
                raise ValueError("Unsafe archive member path.")
            size = item.uncompressed or 0
            if shutil.disk_usage(temp).free < size + 1024**3:
                raise OSError(f"Need about {size / 1024**3 + 1:.1f} GiB of free temporary space.")
            print(f"Unpacking {size / 1024**3:.1f} GiB temporarily; input will be preserved.", flush=True)
            archive.extract(path=temp, targets=[item.filename])
        prepare(destination, source)
    print("Temporary unpacked file removed.")


if __name__ == "__main__":
    main()
