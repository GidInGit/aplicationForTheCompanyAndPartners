import { createSlice } from '@reduxjs/toolkit';

const objectsDataSlice = createSlice({
  name: 'objectsData',
  initialState: {
    objects: [],
    error: null,
  },
  reducers: {
    setObjects: (state, action) => {
      state.objects = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const { setObjects, setError } = objectsDataSlice.actions;
export default objectsDataSlice.reducer;
