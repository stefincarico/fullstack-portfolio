// src/App.jsx
import Display from './components/Display'; // Importiamo i componenti
import Bottone from './components/Bottone';

function App() {
  return (
    <div>
      <h1>La mia Calcolatrice React</h1>
      <Display valore="0" />
      <div className="tastiera">
        <Bottone etichetta="7" />
        <Bottone etichetta="8" />
        <Bottone etichetta="9" />
        <Bottone etichetta="+" />
        {/* ... e così via per gli altri bottoni ... */}
      </div>
    </div>
  );
}
export default App;