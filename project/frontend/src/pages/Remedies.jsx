import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { fetchRemedies } from '../api/remediesApi.js'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Card from '../components/common/Card.jsx'

export default function Remedies() {
  const location = useLocation()
  const [remedies, setRemedies] = useState([])
  const [selectedId, setSelectedId] = useState(location.state?.diseaseId || null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchRemedies()
      .then((data) => {
        setRemedies(data)
        if (!selectedId && data.length > 0) {
          setSelectedId(data[0].disease_id)
        }
      })
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load remedies.'))
      .finally(() => setLoading(false))
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const selected = remedies.find((r) => r.disease_id === selectedId)

  return (
    <div className="page remedies-page">
      <h1>💊 Remedies</h1>
      <p>Select a disease to see recommended treatment and management steps.</p>

      {loading && <Loader label="Loading remedies..." />}
      <ErrorBanner message={error} />

      {!loading && remedies.length > 0 && (
        <div className="remedies-layout">
          <div className="remedies-layout__list">
            {remedies.map((r) => (
              <button
                key={r.disease_id}
                type="button"
                className={`chip chip--block ${
                  selectedId === r.disease_id ? 'chip--active' : ''
                }`}
                onClick={() => setSelectedId(r.disease_id)}
              >
                {r.disease_name}
              </button>
            ))}
          </div>

          {selected && (
            <Card className="remedies-layout__detail">
              <h2>{selected.disease_name}</h2>
              <p className="text-muted">Affected crop: {selected.crop}</p>
              <span className="badge">{selected.treatment_category}</span>

              <h3>Immediate Actions</h3>
              <ul>{selected.immediate_actions.map((i) => <li key={i}>{i}</li>)}</ul>

              <h3>Natural Management</h3>
              <ul>{selected.natural_management.map((i) => <li key={i}>{i}</li>)}</ul>

              <h3>Cultural Management</h3>
              <ul>{selected.cultural_management.map((i) => <li key={i}>{i}</li>)}</ul>

              <h3>Safety Information</h3>
              <p>{selected.safety_information}</p>

              <h3>When to Seek Expert Help</h3>
              <p>{selected.when_to_seek_expert_help}</p>
            </Card>
          )}
        </div>
      )}
    </div>
  )
}
