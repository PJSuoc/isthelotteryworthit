import { useState } from 'react'
import './App.css'
import { AppDataGet, YesNoGet } from './util.tsx'

export function YesNoApp() {

  const appdata = AppDataGet()

  if (!appdata) {
    return <p>Loading...</p>
  }

  if (YesNoGet(appdata)) {
    return (
      <p> YES </p>
    )
  } else {
    return (
      <p> No </p>
    )
    }  


}

export default YesNoApp
