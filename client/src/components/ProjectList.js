import React from 'react';
import ProjectCard from './ProjectCard';

function ProjectList({ projects }) {
  return (
    <div className="project-list">
      <h2>Projects</h2>
      <div className="projects">
        {projects.map(project => (
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </div>
  );
}

export default ProjectList;
