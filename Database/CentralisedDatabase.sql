PRAGMA cache_size = 5000;

DROP TABLE IF EXISTS LoginInformation;
DROP TABLE IF EXISTS Purchase;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS PurchaseHistory;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Drivers;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS OutgoingTransportationSchedules;
DROP TABLE IF EXISTS IncomingTransportationSchedules;
DROP TABLE IF EXISTS ExternalCompanies;
DROP TABLE IF EXISTS logs;


-- Drop Views
DROP VIEW IF EXISTS masked_login_information;
DROP VIEW IF EXISTS viewInventory;
DROP VIEW IF EXISTS masked_Customer;
DROP VIEW IF EXISTS viewCustomerProfile;
DROP VIEW IF EXISTS viewCustomerLogin;
DROP VIEW IF EXISTS viewPurchase;
DROP VIEW IF EXISTS viewDisplayIncomingSchedules;
DROP VIEW IF EXISTS viewDisplayOutgoingSchedules;
DROP VIEW IF EXISTS viewDrivers;

-- Drop Indexes if not created
DROP INDEX IF EXISTS idxLoginInformation;
DROP INDEX IF EXISTS idxCustomer;
DROP INDEX IF EXISTS idxPurchase;
DROP INDEX IF EXISTS idxInventory;
DROP INDEX IF EXISTS idxDrivers;
DROP INDEX IF EXISTS idxVehicle;
DROP INDEX IF EXISTS idxOutgoingTransportationSchedules;
DROP INDEX IF EXISTS idxIncomingTransportationSchedules;
DROP INDEX IF EXISTS idxExternalCompanies;
DROP INDEX IF EXISTS idxLogs;

CREATE TABLE IF NOT EXISTS LoginInformation(
    LoginID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE,
    Password TEXT,
    Permission TEXT DEFAULT 'Customer', -- Can Be Changed By Admin
    AccountStatus TEXT DEFAULT 'Unlocked',
    CustomerID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE IF NOT EXISTS Customer(
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT,
    CustomerEmail TEXT,
    CustomerAddress TEXT,
    CustomerPhoneNumber INTEGER,
    CustomerCreditCard INTEGER,
    CreationDate DATE DEFAULT (date('now'))
);

CREATE TABLE IF NOT EXISTS Purchase(
    PurchaseID INTEGER PRIMARY KEY AUTOINCREMENT,
    PurchaseName TEXT,
    PurchaseDeliveryDate DATE DEFAULT (date('now', '+1 day')),
    PurchaseStock TEXT,
    CustomerID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);


CREATE TABLE IF NOT EXISTS Inventory(
    InventoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    InventoryName TEXT,
    StockLevel INTEGER,
    InventoryPrice INTEGER,
    LocationBuilding TEXT
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
    DriverID INTEGER,
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);


CREATE TABLE IF NOT EXISTS OutgoingTransportationSchedules(
    OutgoingScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExpectedArrivalDate DATE DEFAULT (date('now', '+1 day')),
--     ExpectedArrivalTime INTEGER,
    IsItOnTheWay INTEGER,
--     InventoryID INTEGER REFERENCES Inventory(InventoryID),
--     DriverID INTEGER REFERENCES Drivers(DriverID),
    CustomerID INTEGER,
	PurchaseID INTEGER,
	DriverID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (PurchaseID) REFERENCES Purchase(PurchaseID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);


CREATE TABLE IF NOT EXISTS IncomingTransportationSchedules(
    IncomingScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExpectedArrivalDate DATE DEFAULT (date('now', '+1 day')),
    IncomingStock INTEGER,
    IsItOnTheWay INTEGER,
    InventoryID INTEGER REFERENCES Inventory(InventoryID),
    ExternalCompanyID INTEGER,
    FOREIGN KEY (ExternalCompanyID) REFERENCES ExternalCompanies(ExternalCompanyID)
);


CREATE TABLE IF NOT EXISTS ExternalCompanies(
    ExternalCompanyID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExternalCompanyName TEXT,
    ExternalCompanyRelationship DATE
);

CREATE TABLE IF NOT EXISTS logs(
    LogID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    Description TEXT,
    Type TEXT,
    LogCreated DATE DEFAULT (date('now')),
    LoginID INTEGER,
    FOREIGN KEY (LoginID) REFERENCES LoginInformation(LoginID)
);

CREATE VIEW viewInventory AS
    SELECT InventoryID, InventoryName, StockLevel
    FROM Inventory;

CREATE VIEW viewDisplayIncomingSchedules AS
    SELECT IncomingTransportationSchedules.*, ExternalCompanies.*
    FROM IncomingTransportationSchedules
    INNER JOIN ExternalCompanies on ExternalCompanies.ExternalCompanyID = IncomingTransportationSchedules.ExternalCompanyID;

CREATE VIEW viewDisplayOutgoingSchedules AS
    SELECT OutgoingTransportationSchedules.*, D.DriverID, D.DriverName,C.CustomerName, C.CustomerAddress, C.CustomerPhoneNumber
    FROM OutgoingTransportationSchedules
    INNER JOIN Customer C on C.CustomerID = OutgoingTransportationSchedules.CustomerID
    INNER JOIN Drivers D on D.DriverID = OutgoingTransportationSchedules.DriverID;

CREATE VIEW viewCustomerLogin AS
    SELECT Customer.CustomerID, LoginInformation.LoginID, LoginInformation.Username
    FROM Customer
    INNER JOIN LoginInformation on Customer.CustomerID = LoginInformation.CustomerID;

CREATE VIEW viewPurchase AS
    SELECT Customer.CustomerID, Purchase.PurchaseID, Purchase.PurchaseName, Purchase.PurchaseDeliveryDate, Purchase.PurchaseStock
    FROM Customer
    INNER JOIN Purchase ON Customer.CustomerID = Purchase.CustomerID;

-- Masking Sensitive Views

CREATE VIEW masked_login_information AS
SELECT
    LoginID,
    Username,
    '********' AS MaskedPassword,
    Permission,
    AccountStatus
FROM LoginInformation;

CREATE VIEW masked_Customer AS
    SELECT
        CustomerID,
        CustomerName ,
        CustomerEmail ,
        CustomerPhoneNumber ,
        'XXXX-XXXX-XXXX-' || substr(CustomerCreditCard,-4) AS MaskedCustomerCreditCard,
        CreationDate
    FROM Customer;


-- -- Creating Views for Role: Customer

CREATE VIEW viewCustomerProfile AS
    SELECT masked_login_information.* ,masked_Customer.*, Purchase.*
    FROM masked_login_information
    INNER JOIN masked_Customer ON masked_Customer.CustomerID = masked_login_information.CustomerID
    INNER JOIN Purchase ON Purchase.CustomerID = masked_Customer.CustomerID;

CREATE VIEW viewDrivers AS
    SELECT Drivers.*, Vehicles.VehicleType, Vehicles.VehicleBrand, Vehicles.VehicleLicensePlate
    FROM Drivers
    INNER JOIN Vehicles on Drivers.DriverID = Vehicles.DriverID;

CREATE INDEX IF NOT EXISTS idxLoginInformation
ON LoginInformation (LoginID, Username, CustomerID);

CREATE INDEX IF NOT EXISTS idxCustomer
ON Customer (CustomerID);

CREATE INDEX IF NOT EXISTS idxPurchase
ON Purchase (PurchaseID, CustomerID);

CREATE INDEX IF NOT EXISTS idxInventory
ON Inventory (InventoryID, InventoryName, StockLevel);

CREATE INDEX IF NOT EXISTS idxDrivers
ON Drivers (DriverID);

CREATE INDEX IF NOT EXISTS idxVehicle
ON Vehicles (VehicleID, DriverID);

CREATE INDEX IF NOT EXISTS idxOutgoingTransportationSchedules
ON OutgoingTransportationSchedules (OutgoingScheduleID, CustomerID, PurchaseID, DriverID);

CREATE INDEX IF NOT EXISTS idxIncomingTransportationSchedules
ON IncomingTransportationSchedules (IncomingScheduleID, ExternalCompanyID);

CREATE INDEX IF NOT EXISTS idxExternalCompanies
ON ExternalCompanies (ExternalCompanyID);

CREATE INDEX IF NOT EXISTS idxLogs
ON logs (LogID, LoginID);





