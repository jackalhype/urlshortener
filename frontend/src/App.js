import logo from './logo.svg';
import './App.css';
import ShorteningForm from './components/ShorteningForm'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Free Url Shortener</h1>
        <div className="app-descr">This is a free tool to shorten URLs. Create short & memorable links in seconds.</div>
        <ShorteningForm />
      </header>
    </div>
  );
}

export default App;
