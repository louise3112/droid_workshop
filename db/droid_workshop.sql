DROP TABLE IF EXISTS droids;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS technicians;

CREATE TABLE technicians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    specialty VARCHAR (255)
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
    date_of_registration VARCHAR(255),
    repair_notes TEXT,
    owner_id INT NOT NULL REFERENCES owners(id),
    technician_id INT NOT NULL REFERENCES technicians(id)
);

INSERT INTO technicians (name, specialty) VALUES ()
INSERT INTO technicians (name, specialty) VALUES ()
INSERT INTO technicians (name, specialty) VALUES ()
INSERT INTO technicians (name, specialty) VALUES ()
INSERT INTO technicians (name, specialty) VALUES ()
INSERT INTO technicians (name, specialty) VALUES ()

INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()
INSERT INTO owners (name, contact_details) VALUES ()

INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
INSERT INTO droids (name, type, date_of_registration, repair_notes, owner_id, technician_id) VALUES ()
