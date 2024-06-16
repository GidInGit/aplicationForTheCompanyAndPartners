import { Link } from 'react-router-dom';
import classes from './Navbar.module.css';

const Navbar = () => {
  return (
    <nav className={classes.navbar}>
      <div>Меню</div>
      <Link to={'/objects'}>
        <span>Объекты</span>
      </Link>
      <Link to={'/employees'}>
        <span>Сотрудники</span>
      </Link>
    </nav>
  );
};

export default Navbar;
