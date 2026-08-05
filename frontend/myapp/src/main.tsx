import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import YesNoApp from './YesNoApp.tsx'
import { Powerball, Megamillions } from './Lotteries.tsx'
import Pages from './Pages.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <YesNoApp />
  </StrictMode>,
)

createRoot(document.getElementById('powerball')!).render(
  <StrictMode>
    <Powerball />
  </StrictMode>,
)

createRoot(document.getElementById('megamillions')!).render(
  <StrictMode>
    <Megamillions />
  </StrictMode>,
)

createRoot(document.getElementById('pages')!).render(
  <StrictMode>
    <Pages />
  </StrictMode>,
)