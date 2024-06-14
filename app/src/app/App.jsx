import './App.css';
import Navbar from '../widgets/common/navbar/Navbar.jsx';
import Header from '../widgets/common/header/Header.jsx';

function App() {
  return (
    <div className="page-layout">
      <div className="nav">
        <Navbar />
      </div>
      <div className="header">
        <Header />
      </div>
      <div className="content"></div>
    </div>
  );
}

export default App;
