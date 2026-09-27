import { useEffect, useState } from 'react'
import { fetchCropManagementList } from '../api/cropManagementApi.js'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Card from '../components/common/Card.jsx'

const CROP_IMAGES = {
  Potato: 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=600&q=60',
  Tomato: 'https://images.unsplash.com/photo-1524593689594-aae2f26b75ab?auto=format&fit=crop&w=600&q=60',
}

export default function CropManagement() {
  const [crops, setCrops] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchCropManagementList()
      .then(setCrops)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load crop data.'))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="page crop-management-page">
      <h1>🌾 Crop Management</h1>
      <p>Practical guidance for growing healthy, high-yield crops.</p>

      {loading && <Loader label="Loading crop management data..." />}
      <ErrorBanner message={error} />

      <div className="crop-management-grid">
        {crops.map((crop) => (
          <Card key={crop.crop_name} className="crop-card">
            <img
              src={CROP_IMAGES[crop.crop_name] || CROP_IMAGES.Tomato}
              alt={crop.crop_name}
              className="crop-card__image"
            />
            <h3>{crop.crop_name}</h3>
            <p><strong>Ideal Conditions:</strong> {crop.ideal_conditions}</p>
            <p><strong>Watering:</strong> {crop.watering}</p>
            <p><strong>Fertilization:</strong> {crop.fertilization}</p>
            <p><strong>Common Pests:</strong> {crop.common_pests.join(', ')}</p>
            <p><strong>Harvesting:</strong> {crop.harvesting_tips}</p>
          </Card>
        ))}
      </div>
    </div>
  )
}
