import './App.css';
import Navbar from '../widgets/common/navbar/Navbar.jsx';
import Header from '../widgets/common/header/Header.jsx';
import { Route, Routes } from 'react-router-dom';
import Main from '../pages/main/Main.jsx';

function App() {
  return (
    <div className="page-layout">
      <div className="nav">
        <Navbar />
      </div>
      <div className="header">
        <Header />
      </div>
      <div className="content">
        <Routes>
          <Route path={'/'} element={<Main />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
