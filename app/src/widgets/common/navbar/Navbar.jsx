import { Link } from 'react-router-dom';
import classes from './Navbar.module.css';

const Navbar = () => {
  return (
    <nav className={classes.navbar}>
      <Link to={'/'}>
        <span>Главная</span>
      </Link>
      <Link to={'/analytics'}>
        <span>Аналитика</span>
      </Link>
      <Link to={'/objects'}>
        <span>Объекты</span>
      </Link>
      <Link to={'/brigades'}>
        <span>Бригады</span>
      </Link>
      <Link to={'/employees'}>
        <span>Сотрудники</span>
      </Link>
      <Link to={'/machinery'}>
        <span>Техника</span>
      </Link>
      <Link to={'/bracelets'}>
        <span>Браслеты</span>
      </Link>
      <Link to={'/controllers'}>
        <span>Датчики</span>
      </Link>
      <Link to={'/partners'}>
        <span>Партнеры</span>
      </Link>
      <Link to={'/applications'}>
        <span>Заявки</span>
      </Link>
    </nav>
  );
};

export default Navbar;
