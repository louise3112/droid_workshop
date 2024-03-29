DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS droids;
DROP TABLE IF EXISTS technicians;
DROP TABLE IF EXISTS services_types;
DROP TABLE IF EXISTS services;
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
    type_id INT NOT NULL REFERENCES types(id)
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cost INT
);

CREATE TABLE services_types (
    id SERIAL PRIMARY KEY,
    service_id INT NOT NULL REFERENCES services(id),
    type_id INT NOT NULL REFERENCES types(id)
);

CREATE TABLE droids (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type_id INT NOT NULL REFERENCES types(id),
    activation_date DATE,  -- format YYYY-MM-DD
    owner_id INT NOT NULL REFERENCES owners(id),
    technician_id INT REFERENCES technicians(id)
);

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    date DATE,
    note TEXT,
    droid_id INT NOT NULL REFERENCES droids(id),
    service_id INT NOT NULL REFERENCES services(id)
);


INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Kyle Kattarn', 'Tatooine', 1456); -- 1
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Kandri Beren', 'Yavin 4', 2398); -- 2
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Temmin Wexley', 'Sinta', 9007); -- 3
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Leru Javik', 'Jakku', 7692); -- 4
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Cran Corrand', 'Takodana', 4085); -- 5
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Peli Motto', 'Dantooine', 6137); -- 6
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Olin Arak', 'Mon Calar', 8380); -- 7
INSERT INTO owners (name, home_planet, comlink_frequency) VALUES ('Bossk', 'Wobani', 1008); -- 8

INSERT INTO types (name, picture) VALUES ('Medical', '/static/images/medical_droid.svg'); -- 1
INSERT INTO types (name, picture) VALUES ('Protocol', '/static/images/protocol_droid.svg'); -- 2
INSERT INTO types (name, picture) VALUES ('Battle', '/static/images/battle_droid.svg'); -- 3
INSERT INTO types (name, picture) VALUES ('Astromech', '/static/images/astromech_droid.svg'); -- 4
INSERT INTO types (name, picture) VALUES ('Maintenance', '/static/images/maintenance_droid.svg'); -- 5

INSERT INTO services (name, cost) VALUES ('Registration', 500); -- 1
INSERT INTO services (name, cost) VALUES ('Factory reset', 1000); -- 2
INSERT INTO services (name, cost) VALUES ('Software upgrade', 250); -- 3
INSERT INTO services (name, cost) VALUES ('Hologram retrieval', 2000); -- 4
INSERT INTO services (name, cost) VALUES ('Add new language', 500); -- 5

INSERT INTO services_types (service_id, type_id) VALUES (1, 1);
INSERT INTO services_types (service_id, type_id) VALUES (1, 2);
INSERT INTO services_types (service_id, type_id) VALUES (1, 3);
INSERT INTO services_types (service_id, type_id) VALUES (1, 4);
INSERT INTO services_types (service_id, type_id) VALUES (1, 5);
INSERT INTO services_types (service_id, type_id) VALUES (2, 1);
INSERT INTO services_types (service_id, type_id) VALUES (2, 2);
INSERT INTO services_types (service_id, type_id) VALUES (2, 3);
INSERT INTO services_types (service_id, type_id) VALUES (2, 4);
INSERT INTO services_types (service_id, type_id) VALUES (2, 5);
INSERT INTO services_types (service_id, type_id) VALUES (3, 1);
INSERT INTO services_types (service_id, type_id) VALUES (3, 2);
INSERT INTO services_types (service_id, type_id) VALUES (3, 3);
INSERT INTO services_types (service_id, type_id) VALUES (3, 4);
INSERT INTO services_types (service_id, type_id) VALUES (3, 5);
INSERT INTO services_types (service_id, type_id) VALUES (4, 1);
INSERT INTO services_types (service_id, type_id) VALUES (4, 2);
INSERT INTO services_types (service_id, type_id) VALUES (4, 4);
INSERT INTO services_types (service_id, type_id) VALUES (5, 2);

INSERT INTO technicians (name, type_id) VALUES ('Eslor Keggle', 1); -- 1
INSERT INTO technicians (name, type_id) VALUES ('Grida Reeven', 2); -- 2
INSERT INTO technicians (name, type_id) VALUES ('Noma Raki', 3); -- 3
INSERT INTO technicians (name, type_id) VALUES ('Bo Sund', 4); -- 4
INSERT INTO technicians (name, type_id) VALUES ('Jallo Aren', 5); -- 5
INSERT INTO technicians (name, type_id) VALUES ('Myn Adis', 1); -- 6

INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('C-4AS', 2, '1057-11-14', 1, 2);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('R5-D4', 4, '1050-06-05', 1, 4);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('BB-2', 4, '1045-12-16', 2, 4);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('Cpl Bones', 3, '1048-02-17', 3, 3);
INSERT INTO droids (name, type_id, activation_date, owner_id) VALUES ('Dr Bones', 1, '1049-10-01', 3);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('2-1B', 1, '1055-07-30', 4, 1);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('AP-5', 2, '1053-03-28', 4, 2);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('GA-22', 5, '1042-05-21', 4, 5);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('DT-8G', 3, '1054-04-15', 5, 3);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('FX-6', 1, '1051-10-28', 6, 1);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('W-1LE', 2, '1056-01-15', 6, 2);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('AP-5', 4, '1049-03-06', 7, 4);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('T3-B4', 5, '1035-09-01', 8, 5);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('T3-M4', 5, '1046-09-01', 8, 5);
INSERT INTO droids (name, type_id, activation_date, owner_id, technician_id) VALUES ('T3-X4', 5, '1056-09-01', 8, 5);

INSERT INTO notes (date, note, droid_id, service_id) VALUES ('1057-12-01', 'Basic functioning tests run and all passed. No history due to recent date of activation.', 1, 1);
INSERT INTO notes (date, note, droid_id, service_id) VALUES ('1061-06-24', 'Jawa language added.', 1, 5);
INSERT INTO notes (date, note, droid_id, service_id) VALUES ('1060-06-24', 'Protocol software updated to v32.1.8', 1, 4);
