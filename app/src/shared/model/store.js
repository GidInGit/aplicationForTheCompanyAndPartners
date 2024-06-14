import { configureStore } from '@reduxjs/toolkit';
import companyDataSlice from './companyDataSlice.js';

const store = configureStore({
  reducer: {
    companyData: companyDataSlice,
  },
});

export default store;
