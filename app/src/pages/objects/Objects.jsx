import useObjectsHook from '../../features/customHooks/useObjectsHook.js';

const Objects = () => {
  const { objects, error } = useObjectsHook();

  return error ? (
    <div>{error}</div>
  ) : (
    objects.length > 0 && (
      <div>
        {objects.map(object => (
          <div key={object.id}>
            <span>{object.name}</span>
            <span>{object.address}</span>
            <span>{object.start_time}</span>
            <span>{object.end_time}</span>
          </div>
        ))}
      </div>
    )
  );
};

export default Objects;
