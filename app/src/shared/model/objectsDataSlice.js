import { createSlice } from '@reduxjs/toolkit';

const objectsDataSlice = createSlice({
  name: 'objectsData',
  initialState: {
    objects: [],
    violations: [],
    error: null,
  },
  reducers: {
    setObjects: (state, action) => {
      state.objects = action.payload;
    },
    setViolations: (state, action) => {
      state.violations = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const { setObjects, setViolations, setError } = objectsDataSlice.actions;
export default objectsDataSlice.reducer;
