import { Outlet, Link } from 'react-router-dom';
const Layout = () => (
  <div>
    <header>
      <h1><Link to="/">Task Manager</Link></h1>
    </header>
    <main>
      <Outlet /> {/* <-- Le rotte figlie verranno renderizzate qui */}
    </main>
    <footer><p>&copy; 2025</p></footer>
  </div>
);

export default Layout; // <-- Aggiungo l'esportazione