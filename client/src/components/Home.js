import React from "react";





function Home() {
  return (
    <div>
      <div className="home-container">
        <div className="left">
          <div className="img-container">
            <img src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715819615/IMG_1123_km74af.jpg" alt="Your Image" />
          </div>
        </div>
        <div className="right">
          <h1>Hi, I'm Desiah Barnett</h1>
          <p>
            Hey there! I'm Desiah, and I'm passionate about crafting engaging web experiences. My journey into coding began when I discovered the Flatiron School bootcamp. Starting with basic web development, my skills quickly grew as I delved into more complex projects and challenges.
          </p>
          <p>
            Now, as a graduate of Flatiron School, I'm excited to apply my skills as a software developer. I love the creativity and problem-solving that coding allows, and I'm constantly seeking new ways to innovate and improve user experiences.
          </p>
          <p>
            When I'm not coding, you can find me enjoying a cup of tea, reading fantasy genre books, or producing music. I also enjoy solving puzzles and building things, always looking for ways to bring my ideas to life.
          </p>
          <p>
            I'm thrilled to continue growing and learning in the ever-evolving world of programming, and I can't wait to see where this journey takes me next!
          </p>
        </div>
        <div className="skills-container"></div>
        <h2 className="header">Skills</h2> 
      </div>
      <div className="icon-container">
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817021/Untitled_design_1_f6kdkg.png" alt="React" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817160/download_jpcrkf.jpg" alt="Python" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817215/b59a78e2ed76c705f3c0dcb300f3f222aefdcd99_qsgbrc.png" alt="JavaScript" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817251/download_zstuns.png" alt="Flask" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817323/download_apl9af.jpg" alt="SQL Alchemy.js" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817365/download_1_q6f85v.jpg" alt="Formik" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817534/download_1_v5iupa.png" alt="Redux" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817536/download_5_jihsuq.png" alt="REST" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817543/download_3_swkmxk.png" alt="Git" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817539/download_4_nc11ry.png" alt="Github" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817533/download_2_xwijcq.jpg" alt="SQLite3" />
        <img className="icon" src="https://res.cloudinary.com/doyp4tk82/image/upload/v1715817532/download_2_jiqe34.png" alt="PostgreSQL" />
        {/* Add more icons for other libraries and frameworks */}
        {/* <Footer /> */}
      </div>
    </div>
  );
}

export default Home;
