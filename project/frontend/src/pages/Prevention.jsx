import { useEffect, useState } from 'react'
import { fetchPreventionTips } from '../api/preventionApi.js'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Card from '../components/common/Card.jsx'

export default function Prevention() {
  const [tips, setTips] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchPreventionTips()
      .then(setTips)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load prevention tips.'))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="page prevention-page">
      <h1>🛡️ Prevention</h1>
      <p>General and crop-specific practices to keep diseases from taking hold.</p>

      {loading && <Loader label="Loading prevention tips..." />}
      <ErrorBanner message={error} />

      <div className="prevention-grid">
        {tips.map((tip) => (
          <Card key={tip.title} className="prevention-card">
            <span className="badge">{tip.crop}</span>
            <h3>{tip.title}</h3>
            <ul>
              {tip.points.map((p) => (
                <li key={p}>{p}</li>
              ))}
            </ul>
          </Card>
        ))}
      </div>
    </div>
  )
}
