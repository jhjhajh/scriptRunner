import { Alert } from '../../components'
import { useAppContext } from '../../context/appContext'
import Wrapper from '../../assets/wrappers/DashboardFormPage'
import { useState } from 'react'


const exec = () => {
  exec("ls -la", (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});
}
const AddJob = () => {
  const {showAlert} = useAppContext()

  const [showstart, setstart] = useState(false)

  return (
    <Wrapper>
      <form className='form'>
        <h3>{'Carbanak Scenario 2 Test 1'}</h3>
        {showAlert && <Alert />}
        <div className='form-center'>
          <div className='btn-container'>
            <button
              type='submit'
              className={
                showstart ? 'btn btn-block submit-btn ' : 'btn btn-block clear-btn'
              }
              onClick={(e) => {e.preventDefault() 
                setstart(!showstart)}}
            >
              {showstart ? 'Start' : 'Stop'}
            </button>

          </div>
        </div>
      </form>
    </Wrapper>
  )
}

export default AddJob
