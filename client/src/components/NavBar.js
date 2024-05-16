import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav className="navbar"> {/* Apply the "navbar" class */}
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/projects">Projects</Link>
        </li>
        <li>
          <Link to="/resume">Resume</Link>
        </li>
        {/* Add more links here if needed */}
      </ul>
    </nav>
  );
}


export default NavBar;
