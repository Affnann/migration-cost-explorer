"""Compares what workers paid (BBS survey, workers who left 2015-2018) with the
2017 government caps, and draws the chart in figures/.

Run from the repository root: python code/03_compare.py
"""
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent.parent
caps = list(csv.DictReader(open(root / "data/clean/fee_caps.csv", encoding="utf-8")))
survey = {r["destination"]: r for r in csv.DictReader(open(root / "data/clean/survey_cost_by_destination.csv", encoding="utf-8"))}

def cap_2017(dest, applies_to="all workers"):
    for c in caps:
        if c["destination"] == dest and c["year_set"] == "2017" and c["applies_to"] == applies_to:
            return int(c["cap_tk"])
    raise KeyError(dest)

# (label, destination, survey column, cap row)
pairs = [
    ("Saudi Arabia (men)", "Saudi Arabia", "mean_cost_male_tk", "male workers"),
    ("Saudi Arabia (women)", "Saudi Arabia", "mean_cost_female_tk", "female workers"),
    ("Oman", "Oman", "mean_cost_all_tk", "all workers"),
    ("Malaysia", "Malaysia", "mean_cost_all_tk", "all workers"),
    ("Qatar", "Qatar", "mean_cost_all_tk", "all workers"),
    ("Singapore", "Singapore", "mean_cost_all_tk", "all workers"),
]
rows = []
for label, dest, col, who in pairs:
    paid = int(survey[dest][col])
    cap = cap_2017(dest, who)
    income = int(survey[dest]["mean_monthly_income_tk"])
    rows.append({
        "group": label,
        "average_paid_tk": paid,
        "cap_2017_tk": cap,
        "paid_above_cap_tk": paid - cap,
        "times_the_cap": round(paid / cap, 1) if cap else "",
        "extra_months_of_income": round((paid - cap) / income, 1),
    })

out = root / "data/clean/cap_vs_paid.csv"
w = csv.DictWriter(open(out, "w", encoding="utf-8", newline=""), fieldnames=list(rows[0]))
w.writeheader(); w.writerows(rows)
for r in rows:
    print(r)

# Chart: average paid vs cap, horizontal bars (labels stay readable on a phone).
labels = [r["group"] for r in rows][::-1]
paid = [r["average_paid_tk"] / 1000 for r in rows][::-1]
cap = [r["cap_2017_tk"] / 1000 for r in rows][::-1]
fig, ax = plt.subplots(figsize=(8, 5.0), dpi=150)
y = range(len(labels))
ax.barh([i + 0.2 for i in y], paid, height=0.38, color="#b5532f", label="Average actually paid")
ax.barh([i - 0.2 for i in y], cap, height=0.38, color="#8a8a82", label="Government cap (2017)")
for i, (p, c) in enumerate(zip(paid, cap)):
    ax.text(p + 6, i + 0.2, f"Tk {p:,.0f}k", va="center", fontsize=8.5, color="#1d1d1b")
    ax.text(c + 6, i - 0.2, f"Tk {c:,.0f}k" if c else "Tk 0", va="center", fontsize=8.5, color="#5f5d57")
ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=9.5)
ax.set_xlabel("Thousand taka", fontsize=9)
ax.set_xlim(0, max(paid) * 1.18)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False, fontsize=9)
ax.set_title("What workers paid to go abroad vs the legal cap", loc="left", fontsize=12, fontweight="bold")
fig.text(0.01, 0.01, "Paid: BBS Cost of Migration Survey 2020 (workers who left 2015-2018). Caps: 2017 revision as reported in news.",
         fontsize=7, color="#5f5d57")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(root / "figures/cap_vs_paid.png")
print("chart saved")
