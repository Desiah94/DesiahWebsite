import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import NavBar from './NavBar';
import Home from './Home';
import Login from './Login';
import Register from './Register';
import Logout from './Logout';
import UserProfile from './UserProfile';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="/navbar" element={<NavBar />} />
      </Routes>
    </Router>
  );
}
export default App;
