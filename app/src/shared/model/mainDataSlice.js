import { createSlice } from '@reduxjs/toolkit';

const mainDataSlice = createSlice({
  name: 'mainData',
  initialState: {
    activeUsers: null,
    activeMachinery: null,
    activeBrigades: null,
    error: null,
  },
  reducers: {
    setActiveUsers(state, action) {
      state.activeUsers = action.payload;
    },
    setActiveMachinery(state, action) {
      state.activeMachinery = action.payload;
    },
    setActiveBrigades(state, action) {
      state.activeBrigades = action.payload;
    },
    setError(state, action) {
      state.error = action.payload;
    },
  },
});

export const {
  setActiveUsers,
  setActiveMachinery,
  setActiveBrigades,
  setError,
} = mainDataSlice.actions;
export default mainDataSlice.reducer;
