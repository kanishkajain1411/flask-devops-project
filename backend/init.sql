CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users(name,email)
VALUES
('Kanishka','kanishka@gmail.com'),
('Rahul','rahul@gmail.com'),
('Ankit','ankit@gmail.com');