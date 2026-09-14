import './App.css'
import { useAppData, AppDataProvider, YesNoGet } from './util.tsx'
import { Powerball, Megamillions } from './Lotteries.tsx'


export function YesNoApp() {
  /*
  Sets important information for the background of the frontpage and text
  holds the specific lotteries inside it to give them access to this info
  */

  const appdata = useAppData();

  if (!appdata) {
    return <p>Loading...</p>
  }

  if (YesNoGet(appdata)) {
    return (
      <div className="yes">
        <p className="yes-text"> YES </p>
        <div id="lotteries" className="lotto-boxes">
          <Powerball />
          <Megamillions />
        </div>
      </div>
    )
  } else {
    return (
      <div className="no">
        <p className="no-text"> NO </p>
        <div id="lotteries" className="lotto-boxes">
          <Powerball />
          <Megamillions />
        </div>
      </div>
    )
    }  


}

export function App() {
  // Wraps the whole shebang in a context that feeds the data points of all the relevant bits of the website
  return (
    <AppDataProvider>
      <YesNoApp></YesNoApp>
    </AppDataProvider>
  )
}