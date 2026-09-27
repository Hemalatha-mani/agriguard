export default function DiseaseSearch({ value, onChange }) {
  return (
    <input
      type="text"
      className="input"
      placeholder="Search diseases by name..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  )
}
