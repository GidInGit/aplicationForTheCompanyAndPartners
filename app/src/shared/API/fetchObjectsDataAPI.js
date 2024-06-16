import axios from 'axios';

const fetchObjectsDataAPI = async () => {
  return await axios
    // .get('/api/objects')
    .get('/api/objects')
    .then(response => response)
    .catch(error => {
      throw error;
    });
};

export default fetchObjectsDataAPI;
