import { createContext, useContext, useEffect, useState, type ReactNode } from 'react'

export interface AppData {
    pb_worth: boolean;
    pb_num: number;
    pb_ratio: number;
    mm_worth: boolean;
    mm_num: number;
    mm_ratio: number;
}

const AppDataContext = createContext<AppData | null>(null);

export function AppDataProvider({ children }: { children: ReactNode }) {
    const [appdata, setAppdata] = useState<AppData | null>(null);

    useEffect(() => {
        fetch('/numbers.json', { cache: 'no-store' })
            .then((res) => res.json())
            .then(setAppdata)
    }, []);

    return (
        <AppDataContext.Provider value={appdata}>
            {children}
        </AppDataContext.Provider>
    )
}

export function useAppData() {
    return useContext(AppDataContext);
}

export function YesNoGet(appdata: AppData) {

    const { pb_worth, mm_worth } = appdata;

    if (pb_worth || mm_worth) {
        return true;
    } else {
        return false;
    }
}


function PowerballJackpotGet({ pb_num }: AppData) {
    return pb_num
}

function PowerballRatioGet({ pb_ratio }: AppData) {
    return pb_ratio
}

function MegaMillionJackpotGet({ mm_num }: AppData) {
    return <p className='jackpot'> { mm_num } </p>
}

function MegaMillionRatioGet({ mm_ratio }: AppData) {
    return <p className='ratio'> { mm_ratio } </p>
}


export {
    PowerballJackpotGet, 
    PowerballRatioGet, 
    MegaMillionJackpotGet, 
    MegaMillionRatioGet
}
