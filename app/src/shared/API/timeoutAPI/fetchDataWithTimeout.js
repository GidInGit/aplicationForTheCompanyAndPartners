import axios from 'axios';

const FetchDataWithTimeout = (url, options, timeout = 10000) => {
  const source = axios.CancelToken.source();

  const axiosPromise = axios({
    ...options,
    url,
    cancelToken: source.token,
  });

  const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => {
      const error = new Error('Request timeout');
      error.name = 'TimeoutError'; // Добавляем имя ошибки для идентификации
      error.response = {
        status: 408,
        statusText: 'Request Timeout',
        message: 'The request took too long to process',
      };
      reject(error);
      source.cancel('Request timeout');
    }, timeout),
  );

  return Promise.race([axiosPromise, timeoutPromise]);
};

export default FetchDataWithTimeout;
