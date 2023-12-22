CREATE TABLE Publishers (
    PublisherID SERIAL PRIMARY KEY,
    PublisherName VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Website VARCHAR(100)
);

INSERT INTO Publishers (PublisherName, Address, Website)
VALUES
    ('ABC Publishing', '123 Main St, Cityville', 'www.abcpublishing.com'),
    ('XYZ Books', '456 Oak St, Townsville', 'www.xyzbooks.net'),
    ('123 Press', '789 Pine St, Villagetown', 'www.123press.org');