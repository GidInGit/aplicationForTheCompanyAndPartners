import { useDispatch, useSelector } from 'react-redux';
import { useCallback, useEffect } from 'react';
import {
  setObjects,
  setError,
  setViolations,
} from '../../shared/model/objectsDataSlice.js';
import fetchObjectsDataAPI from '../../shared/API/fetchObjectsDataAPI.js';
import fetchObjectsViolationsAPI from '../../shared/API/fetchObjectsViolationsAPI.js';

const UseObjectsHook = () => {
  const dispatch = useDispatch();
  const objects = useSelector(state => state.objectsData.objects);
  const violations = useSelector(state => state.objectsData.violations);
  const error = useSelector(state => state.objectsData.error);

  const fetchObjectsData = useCallback(() => {
    fetchObjectsDataAPI()
      .then(response => {
        dispatch(setObjects(response.data));
      })
      .catch(error => {
        dispatch(setError(error.message));
      });
  }, [dispatch]);

  const fetchObjectsViolations = useCallback(
    id => {
      fetchObjectsViolationsAPI(id)
        .then(response => {
          dispatch(setViolations(response.data));
        })
        .catch(error => {
          dispatch(setError(error.message));
        });
    },
    [dispatch],
  );

  useEffect(() => {
    fetchObjectsData();
    return () => {
      dispatch(setObjects([]));
      dispatch(setViolations([]));
      dispatch(setError(null));
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return { objects, violations, error, fetchObjectsViolations };
};

export default UseObjectsHook;
