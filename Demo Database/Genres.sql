CREATE TABLE Genres (
    GenreID SERIAL PRIMARY KEY,
    GenreName VARCHAR(50) NOT NULL,
    Description TEXT
);

INSERT INTO Genres (GenreName, Description)
VALUES
    ('Fiction', 'Books created from the author''s imagination'),
    ('Non-Fiction', 'Based on real events, facts, and real people'),
    ('Mystery', 'Involves solving a crime or uncovering secrets');