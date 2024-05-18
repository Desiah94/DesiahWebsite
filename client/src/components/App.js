import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import NavBar from './NavBar';
import Home from './Home';
import Projects from './Projects';
import Resume from './Resume';
import Footer from './Footer'; // Make sure to import Footer

function App() {
  return (
    <Router>
      <div>
        <NavBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/projects" component={Projects} />
          <Route path="/resume" render={(props) => <Resume {...props} showFooter={true} />} />
        </Switch>
        <Footer /> {/* Include Footer outside the Switch */}
      </div>
    </Router>
  );
}


export default App;
