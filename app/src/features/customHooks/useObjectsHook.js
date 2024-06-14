import { useDispatch, useSelector } from 'react-redux';
import { useCallback, useEffect } from 'react';
import { setObjects, setError } from '../../shared/model/objectsDataSlice.js';
import fetchObjectsDataAPI from '../../shared/API/fetchObjectsDataAPI.js';

const UseObjectsHook = () => {
  const dispatch = useDispatch();
  const objects = useSelector(state => state.objectsData.objects);
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

  useEffect(() => {
    fetchObjectsData();
    return () => {
      dispatch(setObjects([]));
      dispatch(setError(null));
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return { objects, error };
};

export default UseObjectsHook;
