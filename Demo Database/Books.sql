CREATE TABLE Books (
    BookID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    AuthorID INT REFERENCES Authors(AuthorID),
    PublisherID INT REFERENCES Publishers(PublisherID),
    GenreID INT REFERENCES Genres(GenreID),
    ReleaseDate DATE,
    ISBN VARCHAR(13),
    Pages INT
);

INSERT INTO Books (Title, AuthorID, PublisherID, GenreID, ReleaseDate, ISBN, Pages)
VALUES
    ('The Great Novel', 1, 1, 1, '2022-01-10', '978-1234567890', 300),
    ('Historical Perspectives', 2, 2, 2, '2021-05-20', '978-9876543210', 250),
    ('Mystery at Midnight', 3, 3, 3, '2023-03-15', '978-1111222233', 200);