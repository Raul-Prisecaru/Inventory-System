DROP TABLE IF EXISTS LoginInformation;
DROP TABLE IF EXISTS Purchase;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS PurchaseHistory;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Drivers;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS OutgoingTransportationSchedules;
DROP TABLE IF EXISTS IncomingTransportationSchedules;
DROP TABLE IF EXISTS ExternalCompanies;
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS userConsent;

-- Drop Views
DROP VIEW IF EXISTS masked_login_information;
DROP VIEW IF EXISTS viewInventory;
DROP VIEW IF EXISTS masked_Customer;
DROP VIEW IF EXISTS viewCustomerProfile;
DROP VIEW IF EXISTS viewCustomerLogin;
DROP VIEW IF EXISTS viewPurchase;
DROP VIEW IF EXISTS viewDisplayIncomingSchedules;
DROP VIEW IF EXISTS viewDisplayOutgoingSchedules;


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
--     OrderID INTEGER REFERENCES Orders(OrderID)
);

CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderName TEXT,
    DeliveryDate DATE,
    CustomerID INTEGER,
	PurchaseID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (PurchaseID) REFERENCES Purchase(PurchaseID)
);

CREATE TABLE IF NOT EXISTS Inventory(
    InventoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    InventoryName TEXT,
    StockLevel INTEGER,
    InventoryPrice INTEGER,
    LocationBuilding TEXT,
    IncomingScheduleID INTEGER,
    FOREIGN KEY (IncomingScheduleID) REFERENCES IncomingTransportationSchedules(IncomingScheduleID)
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
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (PurchaseID) REFERENCES Purchase(PurchaseID)
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


-- Default LOGIN
INSERT INTO Customer(CustomerName, CustomerEmail, CustomerPhoneNumber, CustomerCreditCard) VALUES ('Administrator', 'Admin@stmarys.com', 123123, 1234123412341234);
INSERT INTO Customer(CustomerName, CustomerEmail, CustomerPhoneNumber, CustomerCreditCard) VALUES ('Jake', 'Staff@stmarys.com', 123123, 1234123412341234);
INSERT INTO Customer(CustomerName, CustomerEmail, CustomerPhoneNumber, CustomerCreditCard) VALUES ('Raul', 'Raul@Prisecaru.com', 123123, 1234123412341234);
INSERT INTO Customer(CustomerName, CustomerEmail, CustomerPhoneNumber, CustomerCreditCard) VALUES ('user4', 'user4', 423243234, 243342324342);

-- Testing Purposes
INSERT INTO Inventory (InventoryName, StockLevel, InventoryPrice) VALUES ('Empty Stock', 0, '10');
INSERT INTO Purchase (PurchaseName, PurchaseDeliveryDate, PurchaseStock, CustomerID) VALUES ('CustomerTest', 2024-20-1, 10, 3);
INSERT INTO Purchase (PurchaseName, PurchaseDeliveryDate, PurchaseStock, CustomerID) VALUES ('CustomerTest', 2024-20-1, 10, 4);

CREATE VIEW viewInventory AS
    SELECT InventoryID, InventoryName, StockLevel
    FROM Inventory;

CREATE VIEW viewDisplayIncomingSchedules AS
    SELECT IncomingTransportationSchedules.*, ExternalCompanies.*
    FROM IncomingTransportationSchedules
    INNER JOIN ExternalCompanies on ExternalCompanies.ExternalCompanyID = IncomingTransportationSchedules.ExternalCompanyID;

CREATE VIEW viewDisplayOutgoingSchedules AS
    SELECT OutgoingTransportationSchedules.*, C.CustomerName, C.CustomerAddress
    FROM OutgoingTransportationSchedules
    INNER JOIN Customer C on C.CustomerID = OutgoingTransportationSchedules.CustomerID;

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



