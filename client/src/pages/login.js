// login page
import {useState, useEffect} from 'react'
import {Alert, FormRow, Logo} from '../components'
import Wrapper from '../assets/wrappers/RegisterPage'


const initialState = {
  username: '',
  // email: '',
  password: '',
  isMember: true,
  showAlert: false
}


const Register = () => {
  const [values, setValues] = useState(initialState)
  // gloval state and use navigate

  const toggleMember = () => {
    setValues({...values, isMember:!values.isMember})
  }
  
  const handleChange = (e) => {
    console.log(e.target)
  }
  const onSubmit = (e) => {
    e.preventDefault()
    console.log(e.target)
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
        {values.showAlert && <Alert/>}
      <FormRow type = "username" name = "username" value = {values.name} handleChange = {handleChange}/>
      <FormRow type = "password" name = "password" value = {values.password} handleChange = {handleChange}/>
        <button type = "submit" className="btn btn-block"> submit</button>
        {/* <p>
          <button type="button" onClick={toggleMember} className='member-btn'>Register</button>
        </p> */}
      </form>
    </Wrapper>

  )
}

export default Register
