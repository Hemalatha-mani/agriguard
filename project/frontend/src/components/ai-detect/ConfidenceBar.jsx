export default function ConfidenceBar({ confidence }) {
  const percent = Math.round(confidence * 100)
  return (
    <div className="confidence-bar">
      <div className="confidence-bar__track">
        <div className="confidence-bar__fill" style={{ width: `${percent}%` }} />
      </div>
      <span className="confidence-bar__label">{percent}% confidence</span>
    </div>
  )
}
