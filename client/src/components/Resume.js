// Resume.js
import React from 'react';


function Resume() {
  return (
    <div className="resume-container">
      <h1 className="resume-header">Thanks for connecting</h1>
      <img className="resume-image" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715989530/IMG_1497_scbrk3.jpg" alt="Your Image" />
      <div>
        <a href="https://drive.google.com/file/d/15eo4LSfzTdI9a-4h4d67PdtH1L7cnjJY/view?usp=drive_link" target="_blank" rel="noopener noreferrer">
          <button className="resume-button">Resume</button>
        </a>
      </div>
    </div>
  );
}

export default Resume;
