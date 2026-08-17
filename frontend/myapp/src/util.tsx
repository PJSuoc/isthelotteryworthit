import { useState, useEffect } from 'react';

// I know this is not the most efficient way to get this data
// but I am using it to test building with many components vs 1

interface AppData {
    yesno: string;
    pb_num: number;
    pb_ratio: number;
    mm_num: number;
    mm_ratio: number;
}

function AppDataGet() {

    const [appdata, setData] = useState<AppData | null>(null);


    useEffect(() => {
        fetch('/numbers.json', { cache: 'no-store' })
            .then((res) => res.json())
            .then(setData)
    }, []);

    return appdata
}


function YesNoGet({ yesno }: AppData) {
    return <p className='yesno'> { yesno } </p>
}

function PowerballJackpotGet({ pb_num }: AppData) {
    return <p className='jackpot'> { pb_num } </p>
}

function PowerballRatioGet({ pb_ratio }: AppData) {
    return <p className='ratio'> { pb_ratio } </p>
}

function MegaMillionJackpotGet({ mm_num }: AppData) {
    return <p className='jackpot'> { mm_num } </p>
}

function MegaMillionRatioGet({ mm_ratio }: AppData) {
    return <p className='ratio'> { mm_ratio } </p>
}


export {
    AppDataGet, 
    YesNoGet, 
    PowerballJackpotGet, 
    PowerballRatioGet, 
    MegaMillionJackpotGet, 
    MegaMillionRatioGet
}