import fetchDataWithTimeout from './timeoutAPI/fetchDataWithTimeout.js';

const fetchMainDataAPI = async () => {
  return await fetchDataWithTimeout('/api/', { method: 'GET' })
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export default fetchMainDataAPI;
