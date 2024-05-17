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
      <button onClick={handleCardClick}>Open Video</button>
      {showModal && (
        <div className="custom-modal-overlay">
          <div className="custom-modal">
            <span className="custom-close" onClick={handleCloseModal}>&times;</span>
            <iframe
              title={project.title}
              width="560"
              height="315"
              src={project.loom_embed_url}
              frameBorder="0"
              allowFullScreen
            ></iframe>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProjectCard;
