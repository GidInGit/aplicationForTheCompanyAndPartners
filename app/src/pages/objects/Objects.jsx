import useObjectsHook from '../../features/customHooks/useObjectsHook.js';
import classes from './Objects.module.css';

const Objects = () => {
  const { objects, violations, error, fetchObjectsViolations } =
    useObjectsHook();

  return error ? (
    <div>{error}</div>
  ) : (
    objects.length > 0 && (
      <div>
        <div className={classes.objects}>
          {objects.map(object => (
            <div
              className={classes.item}
              key={object.id}
              onClick={() => fetchObjectsViolations(object.id)}
            >
              <span>{object.name}</span>
              <span>{object.address}</span>
            </div>
          ))}
        </div>
        <div className={classes.violation}>
          {violations.length > 0 && (
            <div>
              {violations.map(violation => (
                <div key={violation.id}>
                  <span>{violation.data1}</span>
                  <span>{violation.data2}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    )
  );
};

export default Objects;
