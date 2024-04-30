import React from "react";


function Home() {
  return (
    <div className="home-container">
      <div className="left">
        <img src="path_to_your_image" alt="Your Image" />
      </div>
      <div className="right">
        <h1>Welcome to My Portfolio</h1>
        <p>
          This is a paragraph describing yourself or your portfolio. You can
          add some information about your skills, experience, or anything else
          you'd like to highlight.
        </p>
        <ul>
          <li><a href="#">Link 1</a></li>
          <li><a href="#">Link 2</a></li>
          <li><a href="#">Link 3</a></li>
          <li><a href="#">Link 4</a></li>
        </ul>
      </div>
    </div>
  );
}

export default Home;
