import { useNavigate } from 'react-router-dom'
import ConfidenceBar from './ConfidenceBar.jsx'
import Button from '../common/Button.jsx'

export default function PredictionResult({ result, previewUrl }) {
  const navigate = useNavigate()
  const isHealthy = result.predicted_class === 'Healthy'

  const diseaseIdMap = {
    Potato_Early_blight: 'potato_early_blight',
    Potato_Late_blight: 'potato_late_blight',
    Tomato_Bacterial_spot: 'tomato_bacterial_spot',
    Tomato_Early_blight: 'tomato_early_blight',
    Tomato_Late_blight: 'tomato_late_blight',
  }
  const diseaseId = diseaseIdMap[result.predicted_class]

  return (
    <div className="prediction-result">
      {previewUrl && (
        <img src={previewUrl} alt="Analyzed crop leaf" className="prediction-result__image" />
      )}

      <h3 className={isHealthy ? 'text-success' : 'text-danger'}>
        {result.predicted_class.replaceAll('_', ' ')}
      </h3>

      <ConfidenceBar confidence={result.confidence} />

      <p className="prediction-result__action">
        {isHealthy
          ? 'No signs of disease detected. Continue routine monitoring and good field hygiene.'
          : 'A disease was detected. Review the remedies and prevention steps below, and consider consulting a local expert if symptoms are severe or spreading.'}
      </p>

      {!isHealthy && diseaseId && (
        <div className="prediction-result__actions">
          <Button
            variant="secondary"
            onClick={() => navigate('/remedies', { state: { diseaseId } })}
          >
            View Remedies
          </Button>
          <Button
            variant="secondary"
            onClick={() => navigate('/prevention', { state: { diseaseId } })}
          >
            View Prevention
          </Button>
        </div>
      )}
    </div>
  )
}
