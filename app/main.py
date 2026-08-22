from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.simulation.engine import run_simulation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SimulationRequest(BaseModel):
    monthly_income: float
    monthly_expenses: float
    current_savings: float
    monthly_investment: float
    years: int = 10
    income_volatility: float = 0.10
    expense_volatility: float = 0.10
    annual_return: float = 0.07

@app.get("/")
def root():
    return {"status": "Finance Forecaster API is running"}

@app.post("/simulate")
def simulate(request: SimulationRequest):
    result = run_simulation(
        monthly_income=request.monthly_income,
        monthly_expenses=request.monthly_expenses,
        current_savings=request.current_savings,
        monthly_investment=request.monthly_investment,
        years=request.years,
        income_volatility=request.income_volatility,
        expense_volatility=request.expense_volatility,
        annual_return=request.annual_return
    )
    return result
