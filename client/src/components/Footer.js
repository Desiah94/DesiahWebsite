import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFilePdf } from '@fortawesome/free-solid-svg-icons';



function Footer() {
  return (
    <footer>
      <div className="social-icons">
        <a href="https://www.linkedin.com/in/desiah-barnett" target="_blank" rel="noopener noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Linkedin.svg" alt="LinkedIn" /></a>
        <a href="https://github.com/DesiahBarnett" target="_blank" rel="noopener noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" /></a>
        <a href="https://twitter.com/desiahbarnett" target="_blank" rel="noopener noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Twitter_logo.svg" alt="Twitter" /></a>
        <a href="https://drive.google.com/file/d/15eo4LSfzTdI9a-4h4d67PdtH1L7cnjJY/view?usp=drive_link" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faFilePdf} /></a>
      </div>
      <p>&copy; 2024 Desiah Barnett</p>
    </footer>
  );
}

export default Footer;
