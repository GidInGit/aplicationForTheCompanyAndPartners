import { configureStore } from '@reduxjs/toolkit';
import companyDataSlice from './companyDataSlice.js';
import mainDataSlice from './mainDataSlice.js';

const store = configureStore({
  reducer: {
    companyData: companyDataSlice,
    mainData: mainDataSlice,
  },
});

export default store;
