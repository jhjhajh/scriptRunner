import {useState, useEffect} from 'react'
import {Logo} from '../components'
import Wrapper from '../assets/wrappers/RegisterPage'

const initialState = {
  name: '',
  email: '',
  password: '',
  isMember: true,
}

const Register = () => {
  const [values, setValues] = useState(initialState)
  // gloval state and use navigate


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
        <Logo />
      </form>
    </Wrapper>

  )
}

export default Register
