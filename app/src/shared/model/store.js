import { configureStore } from '@reduxjs/toolkit';
import objectsDataSlice from './objectsDataSlice.js';
import employeesDataSlice from './employeesDataSlice.js';

const store = configureStore({
  reducer: {
    objectsData: objectsDataSlice,
    employeesData: employeesDataSlice,
  },
});

export default store;
