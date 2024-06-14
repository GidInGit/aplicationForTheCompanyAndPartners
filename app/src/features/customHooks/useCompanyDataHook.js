import { useDispatch, useSelector } from 'react-redux';
import { useCallback, useEffect } from 'react';
import {
  setCompanyName,
  setError,
} from '../../shared/model/companyDataSlice.js';
import fetchCompanyDataAPI from '../../shared/API/fetchCompanyDataAPI.js';

const useCompanyDataHook = () => {
  const dispatch = useDispatch();
  const companyName = useSelector(state => state.companyData.companyName);
  const error = useSelector(state => state.companyData.error);

  const fetchCompanyData = useCallback(() => {
    fetchCompanyDataAPI()
      .then(response => {
        dispatch(setCompanyName(response.name));
      })
      .catch(error => {
        dispatch(setError(error.message));
      });
  }, [dispatch]);

  useEffect(() => {
    fetchCompanyData();
    return () => {
      dispatch(setCompanyName(null));
      dispatch(setError(null));
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return { companyName, error };
};

export default useCompanyDataHook;
