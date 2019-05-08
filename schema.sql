DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude        TEXT NOT NULL,
    longitude       TEXT NOT NULL,
    velocidade      TEXT NOT NULL,
    satelites       TEXT NOT NULL,
    data_hora       DATETIME NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);