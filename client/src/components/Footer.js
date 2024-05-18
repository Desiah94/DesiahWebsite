import React from "react";


function Footer() {
  return (
    <footer className="footer">
      <div className="social-icons">
        <a
          href="http://linkedin.com/in/desiahbarnett/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Linkedin.svg"
            alt="LinkedIn"
          />
        </a>
        <a
          href="https://github.com/Desiah94"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"
            alt="GitHub"
          />
        </a>
        <a
          href="https://desiahbarnett.hashnode.dev/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img
            src="data:image/jpeg;base64,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"
            alt="Hashnode"
          />
        </a>
      </div>
      <p className="copyright">&copy; 2024 Desiah Barnett</p>
    </footer>
  );
}

export default Footer;
