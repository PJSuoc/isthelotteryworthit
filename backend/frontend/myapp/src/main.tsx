import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import { App } from './YesNoApp.tsx'

import Pages from './Pages.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

createRoot(document.getElementById('pages')!).render(
  <StrictMode>
    <Pages />
  </StrictMode>,
)

