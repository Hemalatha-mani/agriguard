import { useEffect, useState } from 'react'
import { fetchFarmingGuide } from '../api/farmingGuideApi.js'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Card from '../components/common/Card.jsx'

export default function FarmingGuide() {
  const [guide, setGuide] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchFarmingGuide()
      .then(setGuide)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load farming guide.'))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="page farming-guide-page">
      <h1>📖 Farming Guide</h1>
      <p>A stage-by-stage walkthrough of best practices from soil prep to harvest.</p>

      {loading && <Loader label="Loading guide..." />}
      <ErrorBanner message={error} />

      <div className="timeline">
        {guide.map((entry, idx) => (
          <Card key={entry.title} className="timeline__item">
            <span className="badge">{entry.stage}</span>
            <h3>
              {idx + 1}. {entry.title}
            </h3>
            <ul>
              {entry.content.map((c) => (
                <li key={c}>{c}</li>
              ))}
            </ul>
          </Card>
        ))}
      </div>
    </div>
  )
}
