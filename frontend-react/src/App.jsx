// src/App.jsx
import './App.css';
import TaskList from './components/TaskList'; // <-- Importa il componente

function App() {
  return (
    <div className="App">
      <h1>Task Manager React</h1>
      <TaskList /> {/* <-- Usalo qui */}
    </div>
  );
}
export default App;