import React from 'react';
import useMainDataHook from '../../features/customHooks/useMainDataHook.js';

const Main = () => {
  const { activeUsers, activeMachinery, activeBrigades, error } =
    useMainDataHook();
  return error ? (
    <div>{error}</div>
  ) : (
    (activeUsers || activeMachinery || activeBrigades) && (
      <div>
        <p>{activeUsers}</p>
        <p>{activeMachinery}</p>
        <p>{activeBrigades}</p>
      </div>
    )
  );
};

export default Main;
