import React, { useReducer, useContext } from 'react'
import reducer from './reducer'
import { 
  DISPLAY_ALERT, 
  CLEAR_ALERT,
  TOGGLE_SIDEBAR,
  TOGGLE_RUN,
} from './actions'


const initialState = {
  isLoading: false,
  showAlert: false,
  alertText: '',
  alertType:'',
  showSidebar: false,
  running: false,
}

const AppContext = React.createContext()

const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState)

  const displayAlert = () => {
    dispatch({type:DISPLAY_ALERT})
    clearAlert()
  }

  const clearAlert = () => {
    setTimeout(()=> {
      dispatch({type:CLEAR_ALERT})
    }, 3000)
  }

  const toggleSidebar = () => {
    dispatch({type: TOGGLE_SIDEBAR})
  }

  const toggleRun = () => {
    dispatch({type: TOGGLE_RUN})
  }


  return (
    <AppContext.Provider value= {{...state, displayAlert, toggleSidebar, toggleRun}}>{children} </AppContext.Provider>
  )
}

const useAppContext = () => {
  return useContext(AppContext)
}
    export {AppProvider, initialState, useAppContext}