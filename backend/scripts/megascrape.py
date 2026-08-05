import requests
from bs4 import BeautifulSoup

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


PRIZES['fiveplusball'] = 987654321

####################### Calculations #########################################

m_wins = 0

for win, prize in PRIZES.items():
    m_wins += prize * (1 / ODDS[win]) * AVGMULTIPLIER

ratio = m_wins / COST

if ratio >= 1:
    print("YES", ratio)
else:
    print("NO", ratio)