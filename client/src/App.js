import {BrowserRouter, Routes, Route, Link} from 'react-router-dom';
import {Landing, Error, Register} from './pages';
import {AllJobs, AddJob, Profile, SharedLayout, Stats} from './pages/dashboard';

function App() {
  return (
    <BrowserRouter>
      <Routes>
      <Route path="/" element = {<Landing />}/>
        <Route path="/dashboard" element ={<SharedLayout/>}>
        {/* <Route path="stats" element = {<Stats/>}/> */}
        <Route path="overview" element = {<Stats/>}/>
        {/* <Route path="all-jobs" element = {<AllJobs/>}/> */}
        {/* <Route path="addjob" element = {<AddJob/>}/> */}
        {/* <Route path="profile" element = {<Profile/>}/> */}
        {/* <Route path="stats" element = {<p> test </p>}/> */}
        <Route path="addsession" element = {<AddJob/>}/>
        {/* <Route path="alljobs" element = {<p> alljobs </p>}/> */}
        </Route>

        <Route path="/getStarted" element = {<Landing />}/>
        <Route path="/login" element = {<Register />}/>
        <Route path="*" element = {<Error />}/>
      </Routes>
    </BrowserRouter>
   

  );
}

export default App;
