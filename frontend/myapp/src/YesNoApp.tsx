import { useState } from 'react'
import './App.css'
import { AppDataGet, YesNoGet } from './util.tsx'

interface AppData {
  yesno: string,
}

function YesNoApp() {
  const [count, setCount] = useState(0)

  const yesno: string = YesNoGet()

  let color: string = 'red-no'

  if (yesno == 'yes') { 
    return (
      <>
        
      </>
    )
  }
  else {
    return (
      <>
        
      </>
    )
  }


}

export default YesNoApp
