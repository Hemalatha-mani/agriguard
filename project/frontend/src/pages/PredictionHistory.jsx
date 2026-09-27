import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { fetchPredictionHistory } from '../api/predictApi.js'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'

export default function PredictionHistory() {
  const [predictions, setPredictions] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchPredictionHistory()
      .then(setPredictions)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load history.'))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="page history-page">
      <h1>📊 Prediction History</h1>
      <p>Every image you've analyzed with AI Detect, saved to your account.</p>

      {loading && <Loader label="Loading history..." />}
      <ErrorBanner message={error} />

      {!loading && predictions.length === 0 && !error && (
        <p>
          No predictions yet. <Link to="/ai-detect">Try AI Detect →</Link>
        </p>
      )}

      {predictions.length > 0 && (
        <table className="table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Predicted Class</th>
              <th>Confidence</th>
            </tr>
          </thead>
          <tbody>
            {predictions.map((p) => (
              <tr key={p.id}>
                <td>{new Date(p.created_at).toLocaleString()}</td>
                <td>{p.predicted_class.replaceAll('_', ' ')}</td>
                <td>{Math.round(p.confidence * 100)}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}
