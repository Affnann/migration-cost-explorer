// True cost of going abroad for work: how many months of savings it takes
// to earn back the recruitment fee, including interest on any loan.
//
// Inputs (all money in taka):
//   fee           total amount paid to go abroad
//   borrowed      part of the fee paid with a loan (0 if none)
//   monthlyRate   loan interest per month, as a fraction (0.02 = 2% a month)
//   wage          expected monthly wage abroad
//   livingCost    monthly spending abroad (food, housing not covered by employer)
//   cap           legal maximum for this destination, or null if not confirmed
//
// Method: each month the worker saves (wage - livingCost). Savings first pay
// off the loan, with interest charged on what is still owed; after that they
// earn back the part of the fee paid from the worker's own money.

function trueCost({ fee, borrowed = 0, monthlyRate = 0, wage, livingCost = 0, cap = null }) {
  const errors = [];
  if (!(fee > 0)) errors.push("fee must be more than 0");
  if (borrowed < 0 || borrowed > fee) errors.push("borrowed must be between 0 and the fee");
  if (monthlyRate < 0) errors.push("interest rate cannot be negative");
  if (!(wage > 0)) errors.push("wage must be more than 0");
  if (livingCost < 0) errors.push("living cost cannot be negative");
  if (errors.length) return { ok: false, errors };

  const saving = wage - livingCost;
  const ownMoney = fee - borrowed;
  const overCap = cap == null ? null : Math.max(0, fee - cap);

  if (saving <= 0) {
    return { ok: true, neverRepaid: true, reason: "monthly savings are zero or less", overCap };
  }

  // Loan: interest is charged each month on what is still owed.
  let owed = borrowed;
  let interestPaid = 0;
  let months = 0;
  const LIMIT = 600; // 50 years: treat as never repaid
  while (owed > 0.005 && months < LIMIT) {
    const interest = owed * monthlyRate;
    if (saving <= interest) {
      return { ok: true, neverRepaid: true, reason: "monthly savings do not cover the interest", overCap };
    }
    interestPaid += interest;
    owed = owed + interest - saving;
    months += 1;
  }
  // The loan is paid off part-way through its last month; from that moment
  // all savings go to earning back the worker's own money.
  const leftover = owed < 0 ? -owed : 0;
  const loanMonthsExact = borrowed > 0 ? months - leftover / saving : 0;
  const ownMonths = ownMoney / saving;

  const totalMonths = loanMonthsExact + ownMonths;
  return {
    ok: true,
    neverRepaid: false,
    totalCost: fee + interestPaid,
    interestPaid,
    monthsToBreakEven: totalMonths,
    overCap,
    capMonths: cap == null ? null : cap / saving,
  };
}

if (typeof module !== "undefined") module.exports = { trueCost };
