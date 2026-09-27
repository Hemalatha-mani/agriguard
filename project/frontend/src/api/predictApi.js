import axiosClient from './axiosClient.js'

export async function predictImage(file) {
  const formData = new FormData()
  formData.append('file', file)

  const res = await axiosClient.post('/api/predict', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return res.data
}

export async function fetchPredictionHistory() {
  const res = await axiosClient.get('/api/predictions')
  return res.data
}
