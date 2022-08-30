// import logo from '../assets/images/favicon.ico'
import main from '../assets/images/main.svg'
import Wrapper from '../assets/wrappers/Testing'
// import Logo from '../components/logo'
// import {Logo} from '../components'
import {Link} from 'react-router-dom'


const Landing = () => {
  return (
    
    <Wrapper>
        <nav>
            {/* <Logo/> */}
        </nav>
    {/* <main> */}
        {/* <nav><span><img src={logo} alt = 'dso' className = 'image' /></span>
            
        </nav> */}
         {/* <div className ="container page"> 
         <h1>  </h1>
        </div> */}
        <div className ="container page"> 
            <div className="info"> 
            {/* <img src={logo} alt = 'dso' className = 'image' /> */}
            <h1>  <span> adversary </span> emulation</h1>
            <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
            <Link to='/login' className = 'btn btn-hero'> Get Started!</Link>
            </div>
            <img src = {main} alt = "job hunt" className="img "/>
        </div>
        </Wrapper>
    // </main>
  )
}

export default Landing
