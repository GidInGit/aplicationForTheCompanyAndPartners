import { createSlice } from '@reduxjs/toolkit';

const companyDataSlice = createSlice({
  name: 'companyData',
  initialState: {
    companyName: null,
    error: null,
  },
  reducers: {
    setCompanyName(state, action) {
      state.companyName = action.payload;
    },
    setError(state, action) {
      state.error = action.payload;
    },
  },
});

export const { setCompanyName, setError } = companyDataSlice.actions;
export default companyDataSlice.reducer;
