// login page
import {useState, useEffect} from 'react'
import {Alert, FormRow, Logo} from '../components'
import Wrapper from '../assets/wrappers/RegisterPage'
import { useAppContext } from '../context/appContext'
import {Link, Navigate} from 'react-router-dom'



const initialState = {
  username: '',
  // email: '',
  password: '',
  isMember: true,
  // showAlert: false
}


const Register = () => {
  const [values, setValues] = useState(initialState)
  // gloval state and use navigate
const {isLoading, showAlert, displayAlert} = useAppContext()

  const toggleMember = () => {
    setValues({...values, isMember:!values.isMember})
  }
  
  const handleChange = (e) => {
    setValues({...values,[e.target.name]:e.target.value})
    console.log(e.target)
  }
  const onSubmit = (e) => {
    e.preventDefault()
    const {username, password, isMember} = values
    if (!username || !password || (!isMember && !username)) {
      displayAlert()
      return
    }
    if (username === "admin" && password === "admin") {
      // change this so that it wont reload the whole page
      window.location.href='/dashboard'
      console.log("correct")
    } else {
      displayAlert()
    }
    // console.log(values)
  }
  return (
    <Wrapper className = 'full-page'>
      <form className = 'form' onSubmit={onSubmit}>
        {/* switching tabs */}
        <h3>Login</h3>
        {/* <h3>{values.isMember ? 'login' :'register'}</h3> */}
        {/* {!values.isMember && (
                <FormRow type = "username" name = "test" value = {values.name} handleChange = {handleChange}/>

        )} */}
        {showAlert && <Alert/>}
      <FormRow type = "username" name = "username" value = {values.name} handleChange = {handleChange}/>
      <FormRow type = "password" name = "password" value = {values.password} handleChange = {handleChange}/>
        <button type = "submit" className="btn btn-block" onClick ={onSubmit}> submit</button>
        {/* <p>
          <button type="button" onClick={toggleMember} className='member-btn'>Register</button>
        </p> */}
      </form>
    </Wrapper>

  )
}

export default Register
