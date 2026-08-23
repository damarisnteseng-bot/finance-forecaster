import { useState } from 'react'
import './App.css'
import FanChart from './components/FanChart'
import StatsPanel from './components/StatsPanel'

const API_URL = 'http://127.0.0.1:8002'

function App() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [form, setForm] = useState({
    monthly_income: 20000,
    monthly_expenses: 15000,
    current_savings: 50000,
    monthly_investment: 2000,
    years: 10,
    income_volatility: 0.10,
    expense_volatility: 0.10,
    annual_return: 0.07
  })

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: parseFloat(e.target.value) })
  }

  async function handleSubmit() {
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      const response = await fetch(API_URL + '/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError('Could not reach the API. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <h1>Finance Forecaster</h1>
      <p className="subtitle">
        See your financial future as a realistic range of possibilities.
      </p>
      <div className="form-grid">
        <div className="form-group">
          <label>Monthly Income (R)</label>
          <input type="number" name="monthly_income" value={form.monthly_income} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Monthly Expenses (R)</label>
          <input type="number" name="monthly_expenses" value={form.monthly_expenses} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Current Savings (R)</label>
          <input type="number" name="current_savings" value={form.current_savings} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Monthly Investment (R)</label>
          <input type="number" name="monthly_investment" value={form.monthly_investment} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Years to Forecast</label>
          <input type="number" name="years" value={form.years} onChange={handleChange} min="1" max="30" />
        </div>
        <div className="form-group">
          <label>Income Variability</label>
          <input type="range" name="income_volatility" value={form.income_volatility} onChange={handleChange} min="0.01" max="0.50" step="0.01" />
        </div>
        <div className="form-group">
          <label>Expense Variability</label>
          <input type="range" name="expense_volatility" value={form.expense_volatility} onChange={handleChange} min="0.01" max="0.50" step="0.01" />
        </div>
        <div className="form-group">
          <label>Annual Return</label>
          <input type="range" name="annual_return" value={form.annual_return} onChange={handleChange} min="0.01" max="0.20" step="0.01" />
        </div>
      </div>
      <button onClick={handleSubmit} disabled={loading} className="simulate-btn">
        {loading ? 'Running simulations...' : 'Forecast My Future'}
      </button>
      {error && <div className="error-box">{error}</div>}
      {result && (
        <div className="results">
          <StatsPanel summary={result.summary} />
          <FanChart timeline={result.timeline} />
        </div>
      )}
    </div>
  )
}

export default App