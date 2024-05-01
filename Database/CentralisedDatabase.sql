DROP TABLE IF EXISTS LoginInformation;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Drivers;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS OutgoingTransportationSchedules;
DROP TABLE IF EXISTS IncomingTransportationSchedules;
DROP TABLE IF EXISTS ExternalCompanies;
DROP TABLE IF EXISTS logs;

CREATE TABLE IF NOT EXISTS LoginInformation(
    Username TEXT UNIQUE,
    Password TEXT
);

CREATE TABLE IF NOT EXISTS Inventory(
    InventoryID INTEGER PRIMARY KEY,
    InventoryName TEXT,
    StockLevel INTEGER,
    LocationBuilding TEXT,
    IncomingScheduleID INTEGER /* Foreign Key */
);


CREATE TABLE IF NOT EXISTS Drivers(
    DriverID INTEGER PRIMARY KEY AUTOINCREMENT,
    DriverName TEXT,
    DriverPhoneNumber INTEGER,
    DriverLicenseRegistrationID TEXT
);


CREATE TABLE IF NOT EXISTS Vehicles(
    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
    VehicleType TEXT,
    VehicleBrand TEXT,
    VehicleLicensePlate TEXT,
    DriverID INTEGER /* Foreign Key */
);


CREATE TABLE IF NOT EXISTS OutgoingTransportationSchedules(
    OutgoingScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExpectedArrivalDate DATE,
    ExpectedArrivalTime INTEGER,
    IsItOnTheWay INTEGER,
    InventoryID INTEGER, /* Foreign Key */
    DriverID INTEGER /* Foreign Key */
);


CREATE TABLE IF NOT EXISTS IncomingTransportationSchedules(
    IncomingScheduleID INTEGER PRIMARY KEY,
    ExpectedArrivalDate DATE,
    ExpectedArrivalTime INTEGER,
    IsItOnTheWay INTEGER,
    InventoryID INTEGER, /* Foreign Key */
    ExternalCompanyID INTEGER /* Foreign Key */
);


CREATE TABLE IF NOT EXISTS ExternalCompanies(
    ExternalCompanyID INTEGER PRIMARY KEY,
    ExternalCompanyName TEXT,
    ExternalCompanyRelationship DATE
);

CREATE TABLE IF NOT EXISTS logs(
--     LogID INTEGER PRIMARY KEY,
    Username TEXT, -- foreign Key to Login
    Description TEXT
);

INSERT INTO LoginInformation (Username, Password) VALUES ('Admin', 'Password')