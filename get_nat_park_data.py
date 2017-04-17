import requests
import sqlite3  # Replace with Postgres

from keys import keys

# Create database, if it does not exist
db = sqlite3.connect('db.sqlite3')

all_parks_url = 'https://ridb.recreation.gov/api/v1/organizations/128/recareas.json'
params = { 'apikey' : keys['RECREATION']}

response = requests.get(all_parks_url, params=params).json()

park_list = response['RECDATA']

for park in park_list:
    park_name = park['RecAreaName']

    sql_insert = 'INSERT INTO national_parks_park (name, visited) VALUES (?, ?)'
    db.execute(sql_insert, (park_name, False ))

db.commit()
db.close()
