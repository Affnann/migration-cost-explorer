"""Builds the data file the calculator page reads (docs/caps.json): the current
cap for each destination, plus the survey's average cost where the survey has one.

Run from the repository root: python code/01_build_caps.py
"""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
caps = [r for r in csv.DictReader(open(root / "data/clean/fee_caps.csv", encoding="utf-8")) if r["current"] == "yes"]
survey = {r["destination"]: r for r in csv.DictReader(open(root / "data/clean/survey_cost_by_destination.csv", encoding="utf-8"))}
col = {"male workers": "mean_cost_male_tk", "female workers": "mean_cost_female_tk", "all workers": "mean_cost_all_tk"}
for r in caps:
    r["cap_tk"] = int(r["cap_tk"])
    s = survey.get(r["destination"])
    r["survey_avg_paid_tk"] = int(s[col[r["applies_to"]]]) if s else None
(root / "docs/caps.json").write_text(json.dumps(caps, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {len(caps)} destinations to docs/caps.json "
      f"({sum(r['survey_avg_paid_tk'] is not None for r in caps)} with survey averages)")
