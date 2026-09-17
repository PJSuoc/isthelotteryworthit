from scraper_util import run_scraper, clean_number
from pathlib import Path
import json


############### Powerball Static Values ######################

COST = 2
ODDS = {
    'ball': 38.32, 
    'oneplusball': 91.98,
    'twoplusball': 701.33,
    'three': 579.76,
    'threeplusball': 14494.11,
    'four': 36525.17,
    'fourplusball': 913129.18,
    'five': 11688053.52,
    'fiveplusball': 292201338}
PRIZES = {
    'ball': 4, 
    'oneplusball': 4,
    'twoplusball': 7,
    'three': 7,
    'threeplusball': 100,
    'four': 100,
    'fourplusball': 50000,
    'five': 1000000,
    'fiveplusball': 20000000} # jackpot default min value


TAXES = .37

####################### Scrape Lottery #######################################

WEBSITE = "https://www.powerball.com/" 
TARGET = "span.game-jackpot-number.text-xxxl.lh-1.text-center"
ALT_TARGET = "span.game-jackpot-number.text-lg.lh-1.text-center"

grand_prize = run_scraper(WEBSITE, TARGET)
grand_prize = clean_number(grand_prize)
PRIZES['fiveplusball'] = grand_prize

####################### Calculations #########################################

m_wins = 0

for win, prize in PRIZES.items():
    if prize >= 600000: # Applies taxes if relevant
        prize = prize * (1-TAXES)
    m_wins += prize * (1 / ODDS[win]) # Adds mean winnings to pool from prize type win

ratio = m_wins / COST

if ratio >= 1:
    yesno = True
else:
    yesno = False

####################### Save to File ########################################
BASE_DIR = Path(__file__).resolve().parent.parent.parent
NUMBERS_PATH = BASE_DIR / 'frontend' / 'myapp' / 'public' / 'numbers.json'

print(grand_prize, ratio, yesno)

with open(NUMBERS_PATH) as f:
    data = json.load(f)

data['pb_num'] = grand_prize
data['pb_ratio'] = ratio
data['pb_worth'] = yesno

with open(NUMBERS_PATH, 'w') as f:
    json.dump(data, f)