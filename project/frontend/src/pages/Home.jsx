import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { fetchDashboardStats } from '../api/dashboardApi.js'
import { useAuth } from '../context/AuthContext.jsx'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Card from '../components/common/Card.jsx'

const QUICK_LINKS = [
  { to: '/ai-detect', label: 'AI Detect', icon: '🔬', desc: 'Upload a leaf photo for instant analysis' },
  { to: '/diseases', label: 'Diseases', icon: '🦠', desc: 'Browse known crop diseases' },
  { to: '/farming-guide', label: 'Farming Guide', icon: '📖', desc: 'Stage-by-stage best practices' },
  { to: '/chatbot', label: 'AI Chatbot', icon: '💬', desc: 'Ask farming questions anytime' },
]

export default function Home() {
  const { user } = useAuth()
  const [stats, setStats] = useState(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchDashboardStats()
      .then(setStats)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load dashboard stats.'))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="page home-page">
      <section className="home-hero">
        <div className="home-hero__text">
          <h1>Welcome back{user ? `, ${user.username}` : ''} 🌾</h1>
          <p>
            Detect crop diseases early, get science-backed remedies, and manage your
            farm with confidence.
          </p>
          <Link to="/ai-detect" className="btn btn--primary">
            Start AI Detection →
          </Link>
        </div>
        <img
          className="home-hero__image"
          src="https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?auto=format&fit=crop&w=1200&q=60"
          alt="Green farm field"
        />
      </section>

      <section>
        <h2>Your Activity</h2>
        {loading && <Loader label="Loading your stats..." />}
        <ErrorBanner message={error} />
        {stats && (
          <div className="stats-grid">
            <Card className="stat-card">
              <span className="stat-card__value">{stats.total_predictions}</span>
              <span className="stat-card__label">Total Scans</span>
            </Card>
            <Card className="stat-card">
              <span className="stat-card__value">{stats.healthy_predictions}</span>
              <span className="stat-card__label">Healthy Results</span>
            </Card>
            <Card className="stat-card">
              <span className="stat-card__value">{stats.disease_predictions}</span>
              <span className="stat-card__label">Diseases Detected</span>
            </Card>
            <Card className="stat-card">
              <span className="stat-card__value">{stats.total_chat_messages}</span>
              <span className="stat-card__label">Chat Questions Asked</span>
            </Card>
          </div>
        )}
      </section>

      <section>
        <h2>Quick Links</h2>
        <div className="quick-links-grid">
          {QUICK_LINKS.map((link) => (
            <Link to={link.to} key={link.to} className="card quick-link-card">
              <span className="quick-link-card__icon">{link.icon}</span>
              <h3>{link.label}</h3>
              <p>{link.desc}</p>
            </Link>
          ))}
        </div>
      </section>
    </div>
  )
}
