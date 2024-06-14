import { useDispatch, useSelector } from 'react-redux';
import { useCallback, useEffect } from 'react';
import {
  setActiveBrigades,
  setActiveMachinery,
  setActiveUsers,
  setError,
} from '../../shared/model/mainDataSlice.js';
import fetchMainDataAPI from '../../shared/API/fetchMainDataAPI.js';

const useMainDataHook = () => {
  const dispatch = useDispatch();

  const activeUsers = useSelector(state => state.mainData.activeUsers);
  const activeMachinery = useSelector(state => state.mainData.activeMachinery);
  const activeBrigades = useSelector(state => state.mainData.activeBrigades);
  const error = useSelector(state => state.mainData.error);

  const fetchMainData = useCallback(() => {
    fetchMainDataAPI()
      .then(response => {
        dispatch(setActiveUsers(response.activeUsers));
        dispatch(setActiveMachinery(response.activeMachinery));
        dispatch(setActiveBrigades(response.activeBrigades));
      })
      .catch(error => dispatch(setError(error.message)));
  }, []);

  useEffect(() => {
    fetchMainData();
    return () => {
      dispatch(setActiveUsers(null));
      dispatch(setActiveMachinery(null));
      dispatch(setActiveBrigades(null));
    };
  }, []);

  return { activeUsers, activeMachinery, activeBrigades, error };
};

export default useMainDataHook;
