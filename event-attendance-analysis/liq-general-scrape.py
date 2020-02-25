import requests
from bs4 import BeautifulSoup
import csv

#get the website and parse the data with beautifulsoup
site = 'https://liquipedia.net/smash/Portal:Tournaments/All/Melee'
page = requests.get(site)
soup = BeautifulSoup(page.text, 'html.parser')

#lists that contain headings for our output
list_of_tournaments = ['Tournament_Name', ]
list_of_dates = ['Date', ]
list_of_prizes = ['Prize', ]
list_of_entrants = ['Entrants', ]
list_of_locs = ['Location', ]
list_of_winners = ['Winner', ]

#find and relay each tournament head...
tournament_heads = soup.find_all(class_='divCell Tournament Header')
for tournament in tournament_heads:
    cleaned = tournament.getText().strip()
    list_of_tournaments.append(cleaned)

#and every date...
date_heads = soup.find_all(class_='divCell EventDetails-Left-55 Header')
for date in date_heads:
    cleaned = date.getText().strip()
    list_of_dates.append(cleaned)

#prize-pool, etc...
prize_heads = soup.find_all(class_='divCell EventDetails-Right-45 Header')
for prize in prize_heads:
    cleaned = prize.getText().strip()
    list_of_prizes.append(cleaned)

entrants_heads = soup.find_all(class_='divCell EventDetails-Left-40 Header')
for entrant in entrants_heads:
    cleaned = entrant.getText().strip()
    list_of_entrants.append(cleaned)

loc_heads = soup.find_all(class_='divCell EventDetails-Right-60 Header')
for location in loc_heads:
    cleaned = location.getText().strip()
    list_of_locs.append(cleaned)

winner_heads = soup.find_all(class_='divCell Placement FirstPlace')
for winner in winner_heads:
    cleaned = winner.getText().strip()
    list_of_winners.append(cleaned)

#convert the lists into columns
rows = zip(list_of_tournaments, list_of_dates, list_of_prizes, list_of_entrants, list_of_locs, list_of_winners)

#write each row to our output file
with open('general-tournament-data.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
