# migration-cost-explorer

What Bangladeshi workers pay to go abroad for work, compared with the legal caps the government sets on recruitment fees, by destination country, plus a calculator that shows one worker how long it takes to earn that cost back.

**Status:** work in progress. The calculator works. The survey data on what workers actually paid has not been added yet.

## 1. The True Cost Calculator

A web page where a worker enters the destination, the total amount paid to go, how much of it was borrowed and at what monthly interest, the expected wage and monthly spending abroad. It shows:

- how many months of work it takes to earn the cost back, including loan interest;
- the total cost with interest;
- how much more than the reported legal cap was paid, where a cap is known.

Nothing typed into the page is saved or sent anywhere. The page is in `docs/` (served by GitHub Pages); the calculation is in `code/calc.js`.

**How it calculates.** Each month the worker saves wage minus spending. Savings first pay off the loan, with interest charged each month on what is still owed; after that they earn back the part paid from the worker's own money. If monthly savings don't cover the monthly interest, the page says the cost is never paid back. `code/calc.test.js` checks the calculation against hand-worked examples and the standard loan formula (`node code/calc.test.js`).

## 2. Fee caps

`data/clean/fee_caps.csv` lists the maximum migration cost for 16 destinations, with the source of every figure. Most come from the government's 2017 revision as reported by the minister in parliament; Malaysia's was reset in July 2022.

**Limitation:** the official government notices setting these caps could not be found online, so every figure is marked as reported in news. Caps may have changed since. Where two reports disagree (Singapore), the difference is recorded in the `note` column.

## 3. What workers actually paid

To be added: the Bangladesh Bureau of Statistics' 2020 Cost of Migration Survey, by destination, compared with the caps above.

## Repository layout

```
code/01_build_caps.py   copies the caps table into the web page's folder
code/calc.js            the calculation
code/calc.test.js       checks for the calculation
data/README.md          every source: link, date, terms
data/clean/             fee_caps.csv (CC BY 4.0)
docs/                   the calculator web page
figures/                charts
```

## License

Code: MIT (see `LICENSE`). Data compiled for this project: CC BY 4.0. Source documents keep their own terms.
