import React, { useState, useEffect } from 'react';
import ProjectList from './ProjectList';

function Projects() {
  const [projects, setProjects] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = () => {
    fetch("http://localhost:5555/projects")
      .then(response => {
        if (!response.ok) {
          throw new Error("Failed to fetch projects");
        }
        return response.json();
      })
      .then(data => {
        setProjects(data);
        setError(null);
      })
      .catch(error => {
        console.error("Error fetching projects:", error);
        setError("Failed to fetch projects");
      });
  };

  return (
    <div>
      {/* <h1>Latest Work</h1> */}
      {error && <p>{error}</p>}
      <ProjectList projects={projects} />
    </div>
  );
}

export default Projects;
