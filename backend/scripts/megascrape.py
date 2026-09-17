from scraper_util import run_scraper, clean_number
from pathlib import Path
import json

############### Mega Millions Static Values ######################

COST = 5
AVGMULTIPLIER = 3 # MM offers a random multiplier on each ticket for non-jackpot prizes
ODDS = {
    'ball': 35, 
    'oneplusball': 86,
    'twoplusball': 665,
    'three': 607,
    'threeplusball': 13965,
    'four': 38859,
    'fourplusball': 893761,
    'five': 12629232,
    'fiveplusball': 290472336}
PRIZES = {
    'ball': 5, 
    'oneplusball': 7,
    'twoplusball': 10,
    'three': 10,
    'threeplusball': 200,
    'four': 1000,
    'fourplusball': 10000,
    'five': 1000000,
    'fiveplusball': 50000000} #jackpot default min value

TAXES = .37

####################### Scrape Lottery #######################################


WEBSITE = "https://www.megamillions.com/" 
TARGET = "span.nextEstVal.js_estJackpot"
ALT_TARGET = "span.nextCashOpt.js_cashOpt"

grand_prize = run_scraper(WEBSITE, TARGET)
grand_prize = clean_number(grand_prize)
PRIZES['fiveplusball'] = grand_prize


####################### Calculations #########################################

m_wins = 0

for win, prize in PRIZES.items():
    prize = int(prize) * AVGMULTIPLIER # Gets actual winnings amount
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

data['mm_num'] = grand_prize
data['mm_ratio'] = ratio
data['mm_worth'] = yesno

with open(NUMBERS_PATH, 'w') as f:
    json.dump(data, f)