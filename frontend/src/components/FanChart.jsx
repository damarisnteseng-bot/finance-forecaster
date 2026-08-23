import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

function formatRand(value) {
  if (value >= 1000000) return 'R' + (value / 1000000).toFixed(1) + 'M'
  if (value >= 1000) return 'R' + (value / 1000).toFixed(0) + 'K'
  return 'R' + value.toFixed(0)
}

function FanChart({ timeline }) {
  const yearlyData = timeline.filter(d => d.month % 12 === 0)

  return (
    <div className="chart-container">
      <h2>Your Financial Future</h2>
      <p className="chart-subtitle">
        Based on 10,000 simulated scenarios — the shaded area shows your realistic range of outcomes.
      </p>
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={yearlyData} margin={{ top: 10, right: 30, left: 20, bottom: 10 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis
            dataKey="year"
            tickFormatter={v => "Year " + v}
            tick={{ fontSize: 12 }}
          />
          <YAxis tickFormatter={formatRand} tick={{ fontSize: 12 }} />
          <Tooltip
            formatter={(value, name) => [formatRand(value), name]}
            labelFormatter={label => "Year " + label}
          />
          <Legend />
          <Area
            type="monotone"
            dataKey="optimistic"
            name="Optimistic (90th %)"
            stroke="#16a34a"
            fill="#bbf7d0"
            fillOpacity={0.6}
          />
          <Area
            type="monotone"
            dataKey="likely"
            name="Most Likely (50th %)"
            stroke="#2563eb"
            fill="#bfdbfe"
            fillOpacity={0.8}
          />
          <Area
            type="monotone"
            dataKey="pessimistic"
            name="Pessimistic (10th %)"
            stroke="#dc2626"
            fill="#fee2e2"
            fillOpacity={0.6}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  )
}

export default FanChart