// src/components/Bottone.jsx

const Bottone = ({ etichetta, tipo, onClick }) => {
  const classeCss = tipo === 'operatore' ? 'bottone operatore' : 'bottone';
  
  return (
    <button
      className={classeCss}
      // Quando il bottone viene cliccato, eseguiamo la funzione
      // ricevuta tramite props, passandole la nostra etichetta.
      onClick={() => onClick(etichetta)}
    >
      {etichetta}
    </button>
  );
};

export default Bottone;