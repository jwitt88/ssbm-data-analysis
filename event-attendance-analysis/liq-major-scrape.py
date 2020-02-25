import requests
from bs4 import BeautifulSoup
import csv

#get the website and parse the data with beautifulsoup
site = 'https://liquipedia.net/smash/Major_Tournaments/Melee'
page = requests.get(site)
soup = BeautifulSoup(page.text, 'html.parser')

#lists that contain headings for our output
list_of_tournaments = ['Tournament_Name', ]
list_of_dates = ['Date', ]
list_of_prizes = ['Prize', ]
list_of_entrants = ['Entrants', ]
list_of_locs = ['Location', ]
list_of_winners = ['Winner', ]
list_of_runners = ['RunnerUp', ]

#for each <DIV> that matches the class.....
for premier_row in soup.find_all('div', attrs={'class':'divRow tournament-card-premier tournament-card-premier'}):

    #grab the tournament name from a sub div and put it on a list...
    tournaments = premier_row.find('div', attrs={'class':'divCell Tournament Header-Premier'})
    clean_tournament = tournaments.getText().strip()
    list_of_tournaments.append(clean_tournament)

    #and the date...
    dates = premier_row.find('div', attrs={'class':'divCell EventDetails-Left-55 Header-Premier'})
    clean_date = dates.getText().strip()
    list_of_dates.append(clean_date)

    #and the prize pool... (etc)
    prizes = premier_row.find('div', attrs={'class':'divCell EventDetails-Right-45 Header-Premier'})
    clean_prize = prizes.getText().strip()
    list_of_prizes.append(clean_prize)

    entrants = premier_row.find('div', attrs={'class':'divCell EventDetails-Left-40 Header-Premier'})
    clean_entrants = entrants.getText().strip()
    list_of_entrants.append(clean_entrants)

    location = premier_row.find('div', attrs={'class':'divCell EventDetails-Right-60 Header-Premier'})
    clean_location = location.getText().strip()
    list_of_locs.append(clean_location)

    first_place = premier_row.find('div', attrs={'class':'divCell Placement FirstPlace'})
    clean_winner = first_place.getText().strip()
    list_of_winners.append(clean_winner)

    second_place = premier_row.find('div', attrs={'class':'divCell Placement SecondPlace'})
    clean_runner = second_place.getText().strip()
    list_of_runners.append(clean_runner)

#convert the lists into columns
rows = zip(list_of_tournaments, list_of_dates, list_of_prizes, list_of_entrants, list_of_locs, list_of_winners, list_of_runners)

#write each row to our output file
with open('major-tournament-data.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
