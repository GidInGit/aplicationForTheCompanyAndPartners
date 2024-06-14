import fetchDataWithTimeout from './timeoutAPI/fetchDataWithTimeout.js';

const fetchCompanyDataAPI = async () => {
  return await fetchDataWithTimeout('api/company', { method: 'GET' })
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export default fetchCompanyDataAPI;
