DROP TABLE IF EXISTS droids;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS technicians;

CREATE TABLE technicians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    speciality VARCHAR (255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_details VARCHAR(255)
);

CREATE TABLE droids (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    registration_date VARCHAR(255),
    repair_notes TEXT,
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    technician_id INT NOT NULL REFERENCES technicians(id) ON DELETE CASCADE
);
-- 
INSERT INTO technicians (name, speciality) VALUES ('Eslor Keggle', 'Medical'); -- 1
INSERT INTO technicians (name, speciality) VALUES ('Grida Reeven', 'Protocol'); -- 2
INSERT INTO technicians (name, speciality) VALUES ('Noma Raki', 'Battle'); -- 3
INSERT INTO technicians (name, speciality) VALUES ('Bo Sund', 'Astromech'); -- 4
INSERT INTO technicians (name, speciality) VALUES ('Jallo Aren', 'Maintenance'); -- 5
INSERT INTO technicians (name, speciality) VALUES ('Kandri Beren', 'Battle'); -- 6

INSERT INTO owners (name, contact_details) VALUES ('Luke Skywalker', 'Alderaan'); -- 1
INSERT INTO owners (name, contact_details) VALUES ('Poe Dameron', 'Yavin 4'); -- 2
-- INSERT INTO owners (name, contact_details) VALUES (); -- 3
-- INSERT INTO owners (name, contact_details) VALUES (); -- 4
-- INSERT INTO owners (name, contact_details) VALUES (); -- 5
-- INSERT INTO owners (name, contact_details) VALUES (); -- 6
-- INSERT INTO owners (name, contact_details) VALUES (); -- 7
-- INSERT INTO owners (name, contact_details) VALUES (); -- 8

INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ('C-3PO', 'Protocol', 'XXXX', 'None', 1, 2);
INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ('R2-D2', 'Astromech', 'XXXX', 'None', 1, 4);
INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ('BB-8', 'Astromech', 'XXXX', 'None', 2, 4);
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES ();

