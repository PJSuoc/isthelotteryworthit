import './App.css'
import { useAppData } from './util.tsx'

export function Powerball() {

    const appdata = useAppData();

    if (!appdata) {
        return <div className="lotto-box">Loading...</div>;
    }

    const pb_jackpot = "$" + String(appdata.pb_num);
    const pb_ratio = "$" + String(appdata.pb_ratio) + " back";

    return (
        <div className="lotto-box">
            <div className="single-lotto jack-box">
                <h3 className="lotto-title">Powerball Jackpot:</h3>
                <h2 className="jackpot"> { pb_jackpot } </h2>
            </div>
            <div className="single-lotto mega-box">
                <h4 className="lotto-title">Return on Investment</h4>
                <h5 className="lotto-return">For every dollar spent, you get:</h5>
                <h5 className="lotto-ratio"> {pb_ratio} </h5>
            </div>
        </div>
    )
}




export function Megamillions() {

    const appdata = useAppData();

    if (!appdata) {
        return <div className="lotto-box">Loading...</div>;
    }

    const mm_jack = "$" + String(appdata.mm_num);
    const mm_ratio = "$" + String(appdata.mm_ratio) + " back";

    return (
        <div className="lotto-box">
            <div className="single-lotto jack-box">
                <h3 className="lotto-title">Mega Millions Jackpot:</h3>
                <h2 className="jackpot"> {mm_jack} </h2>
            </div>
            <div className="single-lotto mega-box">
                <h4 className="lotto-title">Return on Investment</h4>
                <h5 className="lotto-return">For every dollar spent, you get:</h5>
                <h5 className="lotto-ratio"> {mm_ratio} </h5>
            </div>
        </div>
    )
}


