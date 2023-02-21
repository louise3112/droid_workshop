# Droid Repair Workshop

Solo project from Week 5 of the CodeClan Professional Software Development course. This is a full-stack Python app utilisng a Flask / HTML / CSS front-end and a PostgreSQL database in the back-end.


## Brief
Create a web application to help a droid repair workshop manage CRUD actions for technicians, droids and droid owners with a one-to-many relationship between droids and technicians.
![Screenshot of the technician and droid pages](readme_images/droids_technicians.png?raw=true "Title")

Within the 1 week timeframe for this project, I extended the above brief to incorporate CRUD actions for services available at the workshop.
![Screenshot of the services page](readme_images/services.png?raw=true "Title")


## Getting Started
These instructions should get you a copy of the project up and running on your local machine for development purposes.

Install flask and psycopg:
```
pip3 install Flask
pip3 install psycopg2
```

Create and seed the database:
```
createdb droid_workshop
psql -d droid_workshop -f db/droid_workshop.sql
```

Run the app:
```
flask run
```

The web applicaiton can then be viewed in the browser by navigating to http://localhost:4999.


Note: The console.py file is available for testing and can be run in the terminal using:
```
python3 console.py
```


## Future Development
Potential areas for future development of this project include:
* Add filters / search functionality to the pages showing all droids, technicians and services to allow individual items to be more easily located.
* Add payment charges to droids' notes based on service type and a total income generated from each droid on the droid's page.
* Develop calendar / planning element to the app to allow scheduling of upcoming services.

