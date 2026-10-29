"""Copy the fee caps table into the web page's folder as JSON.

Run from the repository root: python code/01_build_caps.py
"""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(root / "data/clean/fee_caps.csv", encoding="utf-8")))
for r in rows:
    r["cap_tk"] = int(r["cap_tk"])
(root / "docs/caps.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {len(rows)} caps to docs/caps.json")
