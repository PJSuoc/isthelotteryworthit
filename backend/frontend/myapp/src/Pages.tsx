import { useState } from 'react'
import './App.css'

type Section = 'math' | 'disclaimer'

function MathContent() {
    return (
        <section className="page-content">
            <h2>The Math</h2>
            <p>For each lottery, you win a prize based on how many numbers match the winning ticket.</p>
            <p>This website takes into account all of the winning possibilities that could return some money, and calculates the average return.</p>
            <p>It also accounts for the inevitable federal taxes that come with a big win, although for small wins we assume that you, foolishly purchasing lottery tickets,
                 have no other income or are a perpetual tax dodger. It also currently uses the grand prize- however, the standing recommended advice unless you are terrible with money
                 (which you may be, having purchased a lottery ticket) is that you should take the lump sum, which is much smaller. I may add or switch to this value in the future.</p>
            <p>I am not accounting for the possibility of multiple winners. Pick your numbers accordingly.</p>
        </section>
    )
}

function DisclaimerContent() {
    return (
        <section className="page-content">
            <h2>Legal</h2>
            <p>All Trademarks belong to the Multi-State Lottery Associate or Mega Millions.</p>
            <p>THIS IS NOT FINANCIAL ADVICE. </p>
        </section>
    )
}

function Pages() {
    const [open, setOpen] = useState<Section | null>(null)

    const toggle = (section: Section) =>
        setOpen(current => (current === section ? null : section))

    return (
        <div className="other-pages">
            <div className="page-btns">
                <button
                    type="button"
                    className="page-btn"
                    aria-expanded={open === 'math'}
                    onClick={() => toggle('math')}
                >
                    The Math
                </button>
                <button
                    type="button"
                    className="page-btn"
                    aria-expanded={open === 'disclaimer'}
                    onClick={() => toggle('disclaimer')}
                >
                    Disclaimer
                </button>
            </div>

            {open === 'math' && <MathContent />}
            {open === 'disclaimer' && <DisclaimerContent />}
        </div>
    )
}

export default Pages