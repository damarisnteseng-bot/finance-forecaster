function formatRand(value) {
  if (value >= 1000000) return 'R' + (value / 1000000).toFixed(2) + 'M'
  if (value >= 1000) return 'R' + (value / 1000).toFixed(1) + 'K'
  return 'R' + value.toFixed(0)
}

function StatsPanel({ summary }) {
  return (
    <div className="stats-panel">
      <div className="stat-card pessimistic">
        <div className="stat-label">Pessimistic</div>
        <div className="stat-value">{formatRand(summary.pessimistic_final)}</div>
        <div className="stat-desc">10% of scenarios end below this</div>
      </div>
      <div className="stat-card likely">
        <div className="stat-label">Most Likely</div>
        <div className="stat-value">{formatRand(summary.likely_final)}</div>
        <div className="stat-desc">The median outcome across all simulations</div>
      </div>
      <div className="stat-card optimistic">
        <div className="stat-label">Optimistic</div>
        <div className="stat-value">{formatRand(summary.optimistic_final)}</div>
        <div className="stat-desc">10% of scenarios end above this</div>
      </div>
    </div>
  )
}

export default StatsPanel