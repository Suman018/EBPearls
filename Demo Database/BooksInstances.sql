CREATE TABLE BookInstances (
    InstanceID SERIAL PRIMARY KEY,
    BookID INT REFERENCES Books(BookID),
    Status VARCHAR(20) NOT NULL,
    Condition VARCHAR(50),
    AcquiredDate DATE
);

INSERT INTO BookInstances (BookID, Status, Condition, AcquiredDate)
VALUES
    (1, 'Available', 'Good', '2022-01-10'),
    (2, 'Checked Out', 'Excellent', '2021-06-01'),
    (3, 'Available', 'Fair', '2023-03-15');

