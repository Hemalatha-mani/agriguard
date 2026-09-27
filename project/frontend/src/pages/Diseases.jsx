import { useEffect, useMemo, useState } from 'react'
import { fetchDiseases } from '../api/diseasesApi.js'
import DiseaseCard from '../components/diseases/DiseaseCard.jsx'
import DiseaseSearch from '../components/diseases/DiseaseSearch.jsx'
import DiseaseFilter from '../components/diseases/DiseaseFilter.jsx'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'

export default function Diseases() {
  const [diseases, setDiseases] = useState([])
  const [search, setSearch] = useState('')
  const [crop, setCrop] = useState('All')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchDiseases()
      .then(setDiseases)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load diseases.'))
      .finally(() => setLoading(false))
  }, [])

  const filtered = useMemo(() => {
    return diseases.filter((d) => {
      const matchesCrop = crop === 'All' || d.crop === crop
      const matchesSearch = d.name.toLowerCase().includes(search.toLowerCase())
      return matchesCrop && matchesSearch
    })
  }, [diseases, search, crop])

  return (
    <div className="page diseases-page">
      <h1>🦠 Crop Diseases</h1>
      <p>Browse detailed information on diseases our AI model can detect.</p>

      <div className="diseases-page__controls">
        <DiseaseSearch value={search} onChange={setSearch} />
        <DiseaseFilter value={crop} onChange={setCrop} />
      </div>

      {loading && <Loader label="Loading diseases..." />}
      <ErrorBanner message={error} />

      {!loading && filtered.length === 0 && !error && (
        <p>No diseases match your search/filter.</p>
      )}

      <div className="diseases-grid">
        {filtered.map((disease) => (
          <DiseaseCard key={disease.id} disease={disease} />
        ))}
      </div>
    </div>
  )
}
