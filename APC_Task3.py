CREATE TABLE if not exists Student(
    ID int, 
    first name text,
    last name text,
    expected graduation year int,
    major text,
    email text
);

CREATE TABLE if not exists Instructor(
    ID int, 
    first name text,
    last name text,
    title text,
    year hired int,
    department text,
    email text
);

CREATE TABLE if not exists Admin(
    ID int, 
    first name text,
    last name text,
    title text,
    office text,
    email text
);

CREATE TABLE if not exists Course(
    CRN int, 
    Title text,
    department text,
    time text,
    days of the week text,
    semster text,
    year int,
    credit int
);
