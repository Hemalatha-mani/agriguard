import { useState } from 'react'
import ImageUploader from '../components/ai-detect/ImageUploader.jsx'
import PredictionResult from '../components/ai-detect/PredictionResult.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Loader from '../components/common/Loader.jsx'
import { predictImage } from '../api/predictApi.js'

export default function AIDetect() {
  const [file, setFile] = useState(null)
  const [previewUrl, setPreviewUrl] = useState(null)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  function handleFileSelected(selectedFile) {
    setFile(selectedFile)
    setPreviewUrl(URL.createObjectURL(selectedFile))
    setResult(null)
    setError('')
  }

  function handleRemove() {
    setFile(null)
    setPreviewUrl(null)
    setResult(null)
    setError('')
  }

  async function handleDetect() {
    if (!file) return
    setLoading(true)
    setError('')
    try {
      const data = await predictImage(file)
      setResult(data)
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          'Prediction failed. Please check your connection and try again.'
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page ai-detect-page">
      <h1>🔬 AI Disease Detection</h1>
      <p>Upload a clear photo of a crop leaf to check for disease using our trained AI model.</p>

      <div className="ai-detect-grid">
        <div className="card ai-detect-grid__left">
          <h2>1. Upload Image</h2>
          <ImageUploader
            onFileSelected={handleFileSelected}
            previewUrl={previewUrl}
            onRemove={handleRemove}
          />
          <button
            type="button"
            className="btn btn--primary btn--full"
            disabled={!file || loading}
            onClick={handleDetect}
          >
            {loading ? 'Analyzing...' : '🔍 Detect Disease'}
          </button>
        </div>

        <div className="card ai-detect-grid__right">
          <h2>2. Result</h2>
          {loading && <Loader label="Running AI analysis..." />}
          <ErrorBanner message={error} />
          {!loading && !result && !error && (
            <p className="ai-detect-grid__placeholder">
              Your prediction results will appear here after you upload an image and click
              "Detect Disease".
            </p>
          )}
          {result && <PredictionResult result={result} previewUrl={previewUrl} />}
        </div>
      </div>
    </div>
  )
}
