"""Checks the survey tables copied from the BBS Cost of Migration Survey 2020.

Run from the repository root: python code/02_check_survey.py
Every check must pass; any failure means a number was misread.
"""
import csv
from pathlib import Path

root = Path(__file__).resolve().parent.parent
cost = list(csv.DictReader(open(root / "data/clean/survey_cost_by_destination.csv", encoding="utf-8")))
borrow = list(csv.DictReader(open(root / "data/clean/survey_borrowing_by_sex.csv", encoding="utf-8")))
fails = 0

def check(ok, msg):
    global fails
    print(("ok   " if ok else "FAIL ") + msg)
    fails += 0 if ok else 1

# 1. Months to recover = average cost / average monthly income (the report's own definition).
for r in cost:
    m = int(r["mean_cost_all_tk"]) / int(r["mean_monthly_income_tk"])
    check(round(m, 1) == float(r["months_of_income_to_recover"]),
          f'{r["destination"]}: {r["mean_cost_all_tk"]} / {r["mean_monthly_income_tk"]} = {m:.2f} vs printed {r["months_of_income_to_recover"]}')

# 2. The all-workers average must lie between the male and female averages.
for r in cost:
    lo, hi = sorted([int(r["mean_cost_male_tk"]), int(r["mean_cost_female_tk"])])
    check(lo <= int(r["mean_cost_all_tk"]) <= hi, f'{r["destination"]}: all-worker average lies between male and female')

# 3. Borrowing: male + female = all, and the percentages match the counts.
tot = {k: sum(int(r[f"workers_{k}"]) for r in borrow) for k in ("male", "female", "all")}
check(tot["male"] + tot["female"] == tot["all"], "borrowing: male + female totals equal the all-worker total")
for r in borrow:
    check(int(r["workers_male"]) + int(r["workers_female"]) == int(r["workers_all"]),
          f'borrowing "{r["borrowed_to_migrate"]}": male + female = all')
    for k in ("male", "female", "all"):
        pct = 100 * int(r[f"workers_{k}"]) / tot[k]
        check(round(pct, 1) == float(r[f"percent_{k}"]),
              f'borrowing "{r["borrowed_to_migrate"]}" {k}: {pct:.2f}% vs printed {r[f"percent_{k}"]}%')

print(f"\n{fails} failed" if fails else "\nall checks passed")
raise SystemExit(1 if fails else 0)
