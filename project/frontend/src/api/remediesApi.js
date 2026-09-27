import axiosClient from './axiosClient.js'

export async function fetchRemedies() {
  const res = await axiosClient.get('/api/remedies')
  return res.data
}

export async function fetchRemedyByDiseaseId(diseaseId) {
  const res = await axiosClient.get(`/api/remedies/${diseaseId}`)
  return res.data
}
