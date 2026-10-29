// Hand-worked checks for calc.js. Run: node code/calc.test.js
const assert = require("assert");
const { trueCost } = require("./calc.js");
const near = (a, b, tol = 0.01) => assert.ok(Math.abs(a - b) <= tol, `${a} != ${b}`);

// 1. No loan: fee 300,000, saves 30,000 a month -> exactly 10 months.
let r = trueCost({ fee: 300000, wage: 40000, livingCost: 10000 });
near(r.monthsToBreakEven, 10);
near(r.interestPaid, 0);

// 2. Loan with 0% interest behaves like no loan.
r = trueCost({ fee: 300000, borrowed: 300000, monthlyRate: 0, wage: 40000, livingCost: 10000 });
near(r.monthsToBreakEven, 10);

// 3. Loan 100,000 at 10%/month, saving 60,000/month.
// Month 1: owed 100,000 + 10,000 - 60,000 = 50,000 (interest 10,000)
// Month 2: owed 50,000 + 5,000 - 60,000 = -5,000 (interest 5,000)
// Interest 15,000; loan done after 2 - 5,000/60,000 months.
r = trueCost({ fee: 100000, borrowed: 100000, monthlyRate: 0.10, wage: 60000 });
near(r.interestPaid, 15000);
near(r.totalCost, 115000);
near(r.monthsToBreakEven, 2 - 5000 / 60000, 1e-9);

// 4. Mixed: fee 200,000, 100,000 borrowed as in case 3, rest own money.
// Loan done after 2 - 5,000/60,000 months, then 100,000/60,000 months for own money
// (same as: 2 full months, with the 5,000 left over going to own money).
r = trueCost({ fee: 200000, borrowed: 100000, monthlyRate: 0.10, wage: 60000 });
near(r.monthsToBreakEven, 2 + 95000 / 60000, 1e-9);

// 9. Real-size case, checked with the loan formula n = -ln(1 - rL/S) / ln(1 + r):
// loan 300,000 at 3%/month, saving 30,000 -> about 12.07 months, then 150,000/30,000 = 5.
r = trueCost({ fee: 450000, borrowed: 300000, monthlyRate: 0.03, wage: 40000, livingCost: 10000 });
near(r.monthsToBreakEven, -Math.log(1 - 0.03 * 300000 / 30000) / Math.log(1.03) + 5, 0.01);

// 5. Savings smaller than the interest: never repaid.
r = trueCost({ fee: 500000, borrowed: 500000, monthlyRate: 0.05, wage: 30000, livingCost: 10000 });
assert.strictEqual(r.neverRepaid, true);

// 6. Cap comparison: fee 450,000 vs cap 165,000 -> 285,000 over.
r = trueCost({ fee: 450000, wage: 40000, livingCost: 10000, cap: 165000 });
near(r.overCap, 285000);
near(r.capMonths, 5.5);

// 7. No cap known -> overCap is null, not 0.
r = trueCost({ fee: 450000, wage: 40000 });
assert.strictEqual(r.overCap, null);

// 8. Bad input is rejected.
assert.strictEqual(trueCost({ fee: 0, wage: 1 }).ok, false);
assert.strictEqual(trueCost({ fee: 100, borrowed: 200, wage: 1 }).ok, false);

console.log("all 9 checks passed");
