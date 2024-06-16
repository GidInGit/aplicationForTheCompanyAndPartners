import './App.css';
import Navbar from '../widgets/common/navbar/Navbar.jsx';
import { Route, Routes } from 'react-router-dom';
import Objects from '../pages/objects/Objects.jsx';
import Employees from '../pages/employees/Employees.jsx';

function App() {
  return (
    <div className="page-layout">
      <div className="nav">
        <Navbar />
      </div>
      <div className="content">
        <Routes>
          <Route path={'/objects'} element={<Objects />} />
          <Route path={'/employees'} element={<Employees />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
