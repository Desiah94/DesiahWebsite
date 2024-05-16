import React, { useState, useEffect } from 'react';
import ProjectList from './ProjectList';

function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = () => {
    fetch("http://localhost:5555/projects")
      .then(response => {
        if (!response.ok) {
          throw new Error(`Failed to fetch projects: ${response.status} ${response.statusText}`);
        }
        console.log(projects)
        return response.json();
      })
      .then(data => {
        setProjects(data);
      })
      .catch(error => {
        console.error("Error fetching projects:", error);
      });
  };

  return (
    <div>
      <h1>Projects</h1>
      <ProjectList projects={projects} />
    </div>
  );
}

export default Projects;
