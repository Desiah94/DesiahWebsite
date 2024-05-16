// Projects.js
import React, { useState, useEffect } from 'react';
import ProjectList from './ProjectList';
import ProjectCard from './ProjectCard';

function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = () => {
    fetch("/projects")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch projects");
        }
        return response.json();
      })
      .then((data) => {
        setProjects(data);
      })
      .catch((error) => {
        console.error("Error fetching projects:", error);
      });
  };

  return (
    <div>
      <h1>Projects</h1>
      <ProjectList projects={projects} />
      <ProjectCard key={project.id} project={project} />
    </div>
  );
}

export default Projects;
