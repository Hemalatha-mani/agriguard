import axiosClient from './axiosClient.js'

export async function fetchDiseases({ crop, search } = {}) {
  const res = await axiosClient.get('/api/diseases', { params: { crop, search } })
  return res.data
}

export async function fetchDiseaseById(diseaseId) {
  const res = await axiosClient.get(`/api/diseases/${diseaseId}`)
  return res.data
}
