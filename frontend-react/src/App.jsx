// src/App.jsx
import { useState } from 'react'; // <-- IMPORTIAMO L'HOOK
import Display from './components/Display';
import Bottone from './components/Bottone';

function App() {
  const [input, setInput] = useState('0');

  // Funzione per gestire il click di un bottone
  const handleButtonClick = (etichetta) => {
    console.log(`Bottone cliccato: ${etichetta}`);
    // Per ora, concateniamo semplicemente l'etichetta all'input
    // (con una logica per gestire lo '0' iniziale)
    if (input === '0') {
      setInput(etichetta);
    } else {
      setInput(input + etichetta);
    }
  };


  return (
    <div className="calculator">
      <h1 style={{ color: 'white' }}>La mia Calcolatrice React</h1>
      <Display valore={input} />
      <div className="tastiera">
        {/* Riga 1 */}
        <Bottone etichetta="7" onClick={handleButtonClick}/>
        <Bottone etichetta="8" onClick={handleButtonClick}/>
        <Bottone etichetta="9" onClick={handleButtonClick}/>
        <Bottone etichetta="/" tipo="operatore" onClick={handleButtonClick}/> {/* <-- AGGIUNTA PROP */}

        {/* Riga 2 */}
        <Bottone etichetta="4" onClick={handleButtonClick}/>
        <Bottone etichetta="5" onClick={handleButtonClick}/>
        <Bottone etichetta="6" onClick={handleButtonClick}/>
        <Bottone etichetta="*" tipo="operatore" onClick={handleButtonClick}/> {/* <-- AGGIUNTA PROP */}

        {/* Continua per gli altri bottoni... */}
        <Bottone etichetta="1" onClick={handleButtonClick}/>
        <Bottone etichetta="2" onClick={handleButtonClick}/>
        <Bottone etichetta="3" onClick={handleButtonClick}/>
        <Bottone etichetta="-" tipo="operatore" onClick={handleButtonClick}/> {/* <-- AGGIUNTA PROP */}

        <Bottone etichetta="0" onClick={handleButtonClick}/>
        <Bottone etichetta="." />
        <Bottone etichetta="=" tipo="operatore" onClick={handleButtonClick}/> {/* <-- AGGIUNTA PROP */}
        <Bottone etichetta="+" tipo="operatore" onClick={handleButtonClick}/> {/* <-- AGGIUNTA PROP */}
      </div>
    </div>
  );
}

export default App;