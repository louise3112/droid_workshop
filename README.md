## Background

This file contains code for a project to create a web application to help a droid repair workshop manage the technicians they employ and the droids registered with the workshop. Technicians specialise in a specific droid type and can only be assigned to work on droids of this type. The web application needed to be able to:
* show all technicians;
* edit / delete an existing technician;
* add a new technician;
* show all registered droids;
* show droids who are not currently assigned to a technician;
* edit / delete existing droids, including their repair notes and owners' details;
* register a new droid, including assigning a technician and adding owners' details where appropriate.

The application was then extended to display, edit, delete and add services provided at the repair workshop.


## To Run

This file requires flask and psycopg to be installed prior to running.

To run the web application, type the following into the terminal:
* "createdb droid_workshop" [creates the database]
* "psql -d droid_workshop -f droid_workshop.sql" [populates the database]
* "flask run" [runs the web application locally]

The web applicaiton can then be viewed in the browser by navigating to http://localhost:4999.

Note: The console.py file is available for testing and can be run by typing "python3 console.py" in the terminal.


## Future Development

Potential areas for future development of this project include:
* Add filters / search functionality to the pages showing all droids, technicians and services to allow individual items to be more easily located.
* Add payment charges to droids' notes based on service type and a total income generated from each droid on the droid's page.
* Develop calendar / planning element to the app to allow scheduling of upcoming services.

