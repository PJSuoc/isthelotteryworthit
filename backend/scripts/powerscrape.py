import requests
from bs4 import BeautifulSoup

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


PRIZES['fiveplusball'] = 987654321

####################### Calculations #########################################

m_wins = 0

for win, prize in PRIZES.items():
    m_wins += prize * (1 / ODDS[win])

ratio = m_wins / COST

if ratio >= 1:
    print("YES", ratio)
else:
    print("NO", ratio)

####################### Save to File ########################################

