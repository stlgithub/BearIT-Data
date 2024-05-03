CREATE DATABASE popup_myynti;
USE popup_myynti;

    CREATE TABLE IF NOT EXISTS tuotteet
    (
    kategoria_id SMALLINT NOT NULL,
    kategoria_nimi VARCHAR(100) NOT NULL,
    tuote_id SMALLINT NOT NULL,
    tuote_nimi VARCHAR(100),
    ostohinta DECIMAL(6,2),
    myyntihinta DECIMAL(6,2),
    alv DECIMAL(5,2),
    PRIMARY KEY (tuote_id),
    UNIQUE KEY (tuote_nimi)
    );
    