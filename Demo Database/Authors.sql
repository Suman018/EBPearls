
CREATE TABLE Authors (
    AuthorID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50),
    BirthDate DATE,
    Nationality VARCHAR(50)
);

INSERT INTO Authors (FirstName, LastName, BirthDate, Nationality)
VALUES
    ('John', 'Doe', '1980-05-15', 'American'),
    ('Jane', 'Smith', '1975-12-22', 'British'),
    ('Michael', 'Johnson', '1990-08-03', 'Canadian');
