import fetchDataWithTimeout from './timeoutAPI/fetchDataWithTimeout.js';

const fetchObjectsDataAPI = async () => {
  return await fetchDataWithTimeout('/api/objects', { method: 'GET' })
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export default fetchObjectsDataAPI;
