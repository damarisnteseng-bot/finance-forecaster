import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.simulation.engine import run_simulation

def test_returns_correct_structure():
    result = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=50000,
        monthly_investment=2000,
        years=5
    )
    assert "timeline" in result
    assert "summary" in result
    assert "pessimistic_final" in result["summary"]
    assert "likely_final" in result["summary"]
    assert "optimistic_final" in result["summary"]
    print("PASS: result has correct structure")

def test_timeline_length_correct():
    result = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=50000,
        monthly_investment=2000,
        years=5
    )
    # 5 years = 60 months + 1 for month 0 = 61 entries
    assert len(result["timeline"]) == 61
    print("PASS: timeline has correct length (61 entries for 5 years)")

def test_starts_at_current_savings():
    result = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=50000,
        monthly_investment=2000,
        years=5
    )
    first = result["timeline"][0]
    assert first["pessimistic"] == 50000.0
    assert first["likely"] == 50000.0
    assert first["optimistic"] == 50000.0
    print("PASS: all three lines start at current savings (R50,000)")

def test_optimistic_greater_than_pessimistic():
    result = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=50000,
        monthly_investment=2000,
        years=10
    )
    summary = result["summary"]
    assert summary["optimistic_final"] > summary["likely_final"]
    assert summary["likely_final"] > summary["pessimistic_final"]
    print("PASS: optimistic > likely > pessimistic (correct ordering)")

def test_more_savings_means_higher_outcome():
    result_low = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=10000,
        monthly_investment=2000,
        years=10
    )
    result_high = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=100000,
        monthly_investment=2000,
        years=10
    )
    assert result_high["summary"]["likely_final"] > result_low["summary"]["likely_final"]
    print("PASS: starting with more savings leads to higher outcome")

def test_higher_investment_means_higher_outcome():
    result_low = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=50000,
        monthly_investment=500,
        years=10
    )
    result_high = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=50000,
        monthly_investment=5000,
        years=10
    )
    assert result_high["summary"]["likely_final"] > result_low["summary"]["likely_final"]
    print("PASS: investing more monthly leads to higher outcome")

def test_zero_savings_still_works():
    result = run_simulation(
        monthly_income=20000,
        monthly_expenses=15000,
        current_savings=0,
        monthly_investment=2000,
        years=10
    )
    assert result["summary"]["likely_final"] > 0
    print("PASS: works correctly when starting with zero savings")

if __name__ == "__main__":
    test_returns_correct_structure()
    test_timeline_length_correct()
    test_starts_at_current_savings()
    test_optimistic_greater_than_pessimistic()
    test_more_savings_means_higher_outcome()
    test_higher_investment_means_higher_outcome()
    test_zero_savings_still_works()
    print("\nAll 7 tests passed!")
