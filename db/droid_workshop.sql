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
    type_id INT NOT NULL REFERENCES types(id)
);

CREATE TABLE droids (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type_id INT NOT NULL REFERENCES types(id),
    -- registration_date VARCHAR(255),
    registration_date DATE,
    -- registration_date DATE, (format YYYY-MM-DD)
    repair_notes TEXT,
    owner_id INT NOT NULL REFERENCES owners(id),
    technician_id INT NOT NULL REFERENCES technicians(id)
);


INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Kyle Kattarn', 'Tatooine', 1456); -- 1
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Kandri Beren', 'Yavin 4', 2398); -- 2
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Temmin Wexley', 'Sinta', 9007); -- 3
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Leru Javik', 'Jakku', 7692); -- 4
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Cran Corrand', 'Takodana', 4085); -- 5
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Peli Motto', 'Dantooine', 6137); -- 6
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Olin Arak', 'Mon Calar', 8380); -- 7
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Bossk', 'Wobani', 1008); -- 8

INSERT INTO types (name, picture) VALUES ('Medical', 'hold.jpeg'); -- 1
INSERT INTO types (name, picture) VALUES ('Protocol', 'hold.jpeg'); -- 2
INSERT INTO types (name, picture) VALUES ('Battle', 'hold.jpeg'); -- 3
INSERT INTO types (name, picture) VALUES ('Astromech', 'hold.jpeg'); -- 4
INSERT INTO types (name, picture) VALUES ('Maintenance', 'hold.jpeg'); -- 5

INSERT INTO technicians (name, picture, type_id) VALUES ('Eslor Keggle', 'hold.jpeg', 1); -- 1
INSERT INTO technicians (name, picture, type_id) VALUES ('Grida Reeven','hold.jpeg', 2); -- 2
INSERT INTO technicians (name, picture, type_id) VALUES ('Noma Raki','hold.jpeg', 3); -- 3
INSERT INTO technicians (name, picture, type_id) VALUES ('Bo Sund','hold.jpeg', 4); -- 4
INSERT INTO technicians (name, picture, type_id) VALUES ('Jallo Aren','hold.jpeg', 5); -- 5

INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('C-4AS', 2, '1057-11-14', 'None', 1, 2);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('R5-D4', 4, '1050-06-05', 'None', 1, 4);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('BB-2', 4, '1045-12-16', 'None', 2, 4);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('Mr Bones', 3, '1048-02-17', 'None', 3, 3);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('2-1B', 1, '1055-07-30', 'None', 4, 1);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('AP-5', 2, '1053-03-28', 'None', 4, 2);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('GA-22', 5, '1042-05-21', 'None', 4, 5);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('DT-8G', 3, '1054-04-15', 'None', 5, 3);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('FX-6', 1, '1051-10-28', 'None', 6, 1);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('W-1LE', 2, '1056-01-15', 'None', 6, 2);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('AP-5', 4, '1049-03-06', 'None', 7, 4);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('T3-B4', 5, '1035-09-01', 'None', 8, 5);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('T3-M4', 5, '1046-09-01', 'None', 8, 5);
INSERT INTO droids (name, type_id, registration_date, repair_notes, owner_id, technician_id) VALUES ('T3-X4', 5, '1056-09-01', 'None', 8, 5);
