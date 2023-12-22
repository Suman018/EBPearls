SELECT
    Books.Title,
    Authors.FirstName,
    Authors.LastName
FROM
    Books
RIGHT JOIN Authors ON Books.AuthorID = Authors.AuthorID;

SELECT
    authors.FirstName,
    authors.LastName,
    books.Title
FROM
    authors
LEFT JOIN books ON authors.AuthorID = books.AuthorID;

SELECT
    Books.Title,
    Authors.FirstName,
    Authors.LastName
FROM
    Books
RIGHT JOIN Authors ON Books.AuthorID = Authors.AuthorID;