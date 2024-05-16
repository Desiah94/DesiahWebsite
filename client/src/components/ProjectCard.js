import React, { useState } from 'react';

const ProjectCard = ({ project }) => {
  const [showModal, setShowModal] = useState(false);

  const handleCardClick = () => {
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  return (
    <div className="project-card">
      <h3>{project.title}</h3>
      <p>{project.description}</p>
      <div className={`modal ${showModal ? 'show' : ''}`}>
        <div className="modal-content">
          <span className="close" onClick={handleCloseModal}>&times;</span>
          <video controls>
            <source src={project.demo_video} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      </div>
      <button onClick={handleCardClick}>Open Video</button>
    </div>
  );
};

export default ProjectCard;
