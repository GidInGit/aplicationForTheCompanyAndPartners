import { configureStore } from '@reduxjs/toolkit';
import companyDataSlice from './companyDataSlice.js';
import mainDataSlice from './mainDataSlice.js';
import objectsDataSlice from './objectsDataSlice.js';

const store = configureStore({
  reducer: {
    companyData: companyDataSlice,
    mainData: mainDataSlice,
    objectsData: objectsDataSlice,
  },
});

export default store;
