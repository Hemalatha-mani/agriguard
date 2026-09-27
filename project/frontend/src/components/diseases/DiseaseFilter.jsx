const CROPS = ['All', 'Potato', 'Tomato']

export default function DiseaseFilter({ value, onChange }) {
  return (
    <div className="disease-filter">
      {CROPS.map((crop) => (
        <button
          key={crop}
          type="button"
          className={`chip ${value === crop ? 'chip--active' : ''}`}
          onClick={() => onChange(crop)}
        >
          {crop}
        </button>
      ))}
    </div>
  )
}
