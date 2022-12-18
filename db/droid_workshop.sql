DROP TABLE IF EXISTS droids;
DROP TABLE IF EXISTS technicians;
DROP TABLE IF EXISTS types;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    home_planet VARCHAR(255),
    comlink_frequency INT
);

CREATE TABLE types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    picture VARCHAR(255)
);

CREATE TABLE technicians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    picture VARCHAR (255),
    bio TEXT,
    type_id INT NOT NULL REFERENCES types(id) ON DELETE CASCADE
);

CREATE TABLE droids (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type_id INT NOT NULL REFERENCES types(id) ON DELETE CASCADE,
    registration_date VARCHAR(255),
    repair_notes TEXT,
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    technician_id INT NOT NULL REFERENCES technicians(id) ON DELETE CASCADE
);


INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Luke Skywalker', 'Tatooine', 1456); -- 1
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Poe Dameron', 'Yavin 4', 2398); -- 2
-- INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (); -- 3
-- INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (); -- 4
-- INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (); -- 5
-- INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (); -- 6
-- INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (); -- 7
-- INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (); -- 8

INSERT INTO types (name, picture) VALUES ('Medical', 'hold.jpeg'); -- 1
INSERT INTO types (name, picture) VALUES ('Protocol', 'hold.jpeg'); -- 2
INSERT INTO types (name, picture) VALUES ('Battle', 'hold.jpeg'); -- 3
INSERT INTO types (name, picture) VALUES ('Astromech', 'hold.jpeg'); -- 4
INSERT INTO types (name, picture) VALUES ('Maintenance', 'hold.jpeg'); -- 5

INSERT INTO technicians (name, picture, bio, type_id) VALUES ('Eslor Keggle', 'hold.jpeg', 'hold for bio text', 1); -- 1
INSERT INTO technicians (name, picture, bio, type_id) VALUES ('Grida Reeven','hold.jpeg', 'hold for bio text', 2); -- 2
INSERT INTO technicians (name, picture, bio, type_id) VALUES ('Noma Raki','hold.jpeg', 'hold for bio text', 3); -- 3
INSERT INTO technicians (name, picture, bio, type_id) VALUES ('Bo Sund','hold.jpeg', 'hold for bio text', 4); -- 4
INSERT INTO technicians (name, picture, bio, type_id) VALUES ('Jallo Aren','hold.jpeg', 'hold for bio text', 5); -- 5
INSERT INTO technicians (name, picture, bio, type_id) VALUES ('Kandri Beren','hold.jpeg', 'hold for bio text', 3); -- 6

INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('C-3PO', 2, 'XXXX', 'None', 1, 2);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('R2-D2', 4, 'XXXX', 'None', 1, 4);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('BB-8', 4, 'XXXX', 'None', 2, 4);
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();
-- INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ();


