import numpy as np


def run_simulation(
    monthly_income: float,
    monthly_expenses: float,
    current_savings: float,
    monthly_investment: float,
    years: int = 10,
    income_volatility: float = 0.10,
    expense_volatility: float = 0.10,
    annual_return: float = 0.07,
    num_simulations: int = 10000
) -> dict:
    """
    Run a Monte Carlo simulation of personal finances.
    Returns both final percentiles and monthly timeline data for charting.
    """
    months = years * 12
    monthly_return = (1 + annual_return) ** (1/12) - 1

    # Store savings value at each month for every simulation
    # Shape: (num_simulations, months+1) — +1 to include month 0 (starting point)
    all_paths = np.zeros((num_simulations, months + 1))

    for sim in range(num_simulations):
        savings = current_savings
        all_paths[sim, 0] = savings  # record starting value

        for month in range(1, months + 1):
            income_variation = np.random.normal(0, income_volatility)
            expense_variation = np.random.normal(0, expense_volatility)

            actual_income = monthly_income * (1 + income_variation)
            actual_expenses = monthly_expenses * (1 + expense_variation)
            investment_growth = savings * monthly_return

            savings = savings + actual_income - actual_expenses + monthly_investment + investment_growth
            all_paths[sim, month] = savings  # record this month's value

    # Calculate percentiles at each month across all simulations
    pessimistic = np.percentile(all_paths, 10, axis=0)
    likely = np.percentile(all_paths, 50, axis=0)
    optimistic = np.percentile(all_paths, 90, axis=0)

    # Build timeline data for the chart
    # Each entry: { month, year, pessimistic, likely, optimistic }
    timeline = []
    for m in range(months + 1):
        timeline.append({
            "month": m,
            "year": round(m / 12, 1),
            "pessimistic": round(float(pessimistic[m]), 2),
            "likely": round(float(likely[m]), 2),
            "optimistic": round(float(optimistic[m]), 2)
        })

    return {
        "timeline": timeline,
        "summary": {
            "pessimistic_final": round(float(pessimistic[-1]), 2),
            "likely_final": round(float(likely[-1]), 2),
            "optimistic_final": round(float(optimistic[-1]), 2),
            "years": years,
            "num_simulations": num_simulations
        }
    }
