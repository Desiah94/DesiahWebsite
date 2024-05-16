import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import NavBar from './NavBar';
import Home from './Home';
// import Resume from './Resume';
// import Register from './Register';
// import Logout from './Logout';
// import UserProfile from './UserProfile';

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/" exact component={Home} />
        {/* <Route path="/resume" component={Resume} /> */}
        {/* <Route path="/register" component={Register} />
        <Route path="/logout" component={Logout} />
        <Route path="/profile" component={UserProfile} /> */}
      </Switch>
    </Router>
  );
}

export default App;
