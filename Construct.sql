-- Create the Campaign table to store campaign details
CREATE TABLE Campaign (
    CampaignID SERIAL PRIMARY KEY, -- Primary key for Campaign table
    Name VARCHAR(255),
    Description TEXT,
    StartDate DATE,
    EndDate DATE,
    Region VARCHAR(255),
    Status VARCHAR(50),
    Cost NUMERIC,
    Type VARCHAR(100)
);

-- Create the Volunteer table to store volunteer details
CREATE TABLE Volunteer (
    VolunteerID SERIAL PRIMARY KEY, -- Primary key for Volunteer table
    Name VARCHAR(255),
    ContactInfo TEXT,
    ParticipationCount INTEGER,
    Level VARCHAR(50),
    JoinDate DATE
);

-- Create the Donor table to store donor details
CREATE TABLE Donor (
    DonorID SERIAL PRIMARY KEY, -- Primary key for Donor table
    Name VARCHAR(255),
    ContactInfo TEXT,
    DonateAmount NUMERIC
);

-- Create the Organisation table to store organisation details
CREATE TABLE Organisation (
    OrganisationID SERIAL PRIMARY KEY, -- Primary key for Organisation table
    Location TEXT,
    Goal TEXT,
    NumberOfPeople INTEGER
);

-- Create the Employees table to store employee details and link them to an Organisation
CREATE TABLE Employees (
    EmployeeID SERIAL PRIMARY KEY, -- Primary key for Employees table
    Name VARCHAR(255),
    Role VARCHAR(100),
    Salary NUMERIC,
    ContactInfo TEXT,
    OrganisationID INTEGER REFERENCES Organisation(OrganisationID) -- Foreign key to Organisation table
);

-- Create the Website table to store website details and associate them with Campaigns and Organisations
CREATE TABLE Website (
    WebID SERIAL PRIMARY KEY, -- Primary key for Website table
    CampaignID INTEGER REFERENCES Campaign(CampaignID), -- Foreign key to Campaign table
    PublishDate DATE,
    Content TEXT,
    OrganisationID INTEGER REFERENCES Organisation(OrganisationID) -- Foreign key to Organisation table
);

-- Create the CampaignEvent table
CREATE TABLE CampaignEvent (
    EventID SERIAL PRIMARY KEY,
    CampaignID INTEGER REFERENCES Campaign(CampaignID),
    EventName VARCHAR(255),
    EventDate DATE,
    EventTime TIME,
    Location TEXT,
    Description TEXT
);

-- Create a junction table for many-to-many relationship between Campaigns and Donors
CREATE TABLE Transacts (
    OrganisationID INTEGER REFERENCES Organisation(OrganisationID),
    WebID INTEGER REFERENCES Website(WebID),
    PRIMARY KEY (OrganisationID, WebID)
);

-- Create a junction table for many-to-many relationship between Volunteers and Campaigns
CREATE TABLE VolunteerParticipates (
    CampaignID INTEGER REFERENCES Campaign(CampaignID), -- Foreign key to Campaign table
    VolunteerID INTEGER REFERENCES Volunteer(VolunteerID), -- Foreign key to Volunteer table
    PRIMARY KEY (CampaignID, VolunteerID) -- Composite primary key
);

-- Create a junction table for many-to-many relationship between Employees and Campaigns
CREATE TABLE EmployeeParticipates (
    CampaignID INTEGER REFERENCES Campaign(CampaignID), -- Foreign key to Campaign table
    EmployeeID INTEGER REFERENCES Employees(EmployeeID), -- Foreign key to Employees table
    PRIMARY KEY (CampaignID, EmployeeID) -- Composite primary key
);

-- Create a junction table for many-to-many relationship between Campaigns and Organisations
CREATE TABLE Plan (
    CampaignID INTEGER REFERENCES Campaign(CampaignID), -- Foreign key to Campaign table
    OrganisationID INTEGER REFERENCES Organisation(OrganisationID), -- Foreign key to Organisation table
    PRIMARY KEY (CampaignID, OrganisationID) -- Composite primary key
);

-- Insert organisation data into Organisation table
INSERT INTO Organisation (Location, Goal, NumberOfPeople)
VALUES
('Downtown', 'To make the city greener and cleaner.', 10),
('Suburbs', 'To engage the community in environmental activities.', 20),
('City Center', 'To promote cultural events and activities.', 15),
('Industrial Area', 'To advocate for eco-friendly practices in industries.', 8);

-- Insert campaign data into Campaign table
INSERT INTO Campaign (Name, Description, StartDate, EndDate, Region, Status, Cost, Type)
VALUES
('Clean the City', 'A campaign to clean up the city streets.', '2023-07-01', '2023-07-14', 'Urban', 'Active', 1500, 'Cleanup'),
('Plant a Tree', 'A campaign to plant trees in the city park.', '2023-08-01', '2023-08-30', 'Urban', 'Active', 1200, 'Environment'),
('Save Water', 'Raise awareness about water conservation methods.', '2023-09-01', '2023-09-15', 'Rural', 'Planning', 1000, 'Awareness'),
('Recycling Awareness', 'Educate people about the benefits of recycling.', '2023-10-01', '2023-10-31', 'Urban', 'Planning', 800, 'Awareness'),
('Green Energy Expo', 'Showcase renewable energy solutions.', '2023-11-01', '2023-11-15', 'Urban', 'Planning', 2000, 'Exhibition'),
('Community Garden', 'Create a communal garden for local residents.', '2023-12-01', '2023-12-31', 'Suburban', 'Active', 1200, 'Community');

-- Insert volunteer data into Volunteer table
INSERT INTO Volunteer (Name, ContactInfo, ParticipationCount, Level, JoinDate)
VALUES
('Alice Smith', 'alice.smith@example.com', 4, 'Expert', '2022-06-01'),
('Bob Jones', 'bob.jones@example.com', 2, 'Intermediate', '2022-07-01'),
('Carol White', 'carol.white@example.com', 5, 'Expert', '2022-05-15'),
('Eva Green', 'eva.green@example.com', 3, 'Intermediate', '2022-08-01'),
('Harry Blue', 'harry.blue@example.com', 1, 'Beginner', '2022-09-01'),
('Ivy Yellow', 'ivy.yellow@example.com', 6, 'Expert', '2022-07-15');

-- Insert donor data into Donor table
INSERT INTO Donor (Name, ContactInfo, DonateAmount)
VALUES
('David Grey', 'david.grey@example.com', 5000),
('Emma Brown', 'emma.brown@example.com', 2500),
('Fred Orange', 'fred.orange@example.com', 3000),
('Grace Purple', 'grace.purple@example.com', 1500),
('Henry Black', 'henry.black@example.com', 2000);

-- Insert employee data into Employees table
INSERT INTO Employees (Name, Role, Salary, ContactInfo, OrganisationID)
VALUES
('Frank Black', 'Project Manager', 75000, 'frank.black@example.com', 1),
('Gina Red', 'Volunteer Coordinator', 65000, 'gina.red@example.com', 1),
('Helen Nonparticipant', 'Marketing', 60000, 'helen.nonparticipant@example.com', 2),
('Jack White', 'Financial Analyst', 70000, 'jack.white@example.com', 2),
('Kate Brown', 'Community Outreach Coordinator', 65000, 'kate.brown@example.com', 2),
('Linda Green', 'Event Planner', 60000, 'linda.green@example.com', 3);

-- Insert website update data into Website table
INSERT INTO Website (CampaignID, PublishDate, Content, OrganisationID)
VALUES
(1, '2023-07-02', 'Join us this weekend to make our city clean!', 1),
(2, '2023-08-02', 'Help us increase the green space in our park.', 1),
(3, '2023-12-05', 'Join us in creating a beautiful garden for everyone!', 2),
(1, '2023-10-02', 'Learn how recycling can benefit our environment.', 3),
(2, '2023-11-02', 'Explore the future of green energy at our expo.', 4);

-- Insert CampaignEvent data into CampaignEvent table
INSERT INTO CampaignEvent (CampaignID, EventName, EventDate, EventTime, Location, Description)
VALUES
(1, 'City Clean-Up Kickoff', '2023-07-01', '09:00', 'City Center', 'Kickoff event for city clean-up campaign.'),
(1, 'City Clean-Up Final Day', '2023-07-14', '17:00', 'City Park', 'Final day event for city clean-up, summarizing the work done.'),
(2, 'Tree Planting Day 1', '2023-08-01', '10:00', 'Northern Park', 'First day of tree planting in the northern park.'),
(2, 'Tree Planting Day 2', '2023-08-15', '10:00', 'Eastern Park', 'Continuing our effort to green the city, focusing on the eastern park.'),
(3, 'Garden Planning Meeting', '2023-12-01', '14:00', 'Community Center', 'Meeting to discuss plans for the community garden.'),
(3, 'Garden Planting Day', '2023-12-15', '09:00', 'Suburban Park', 'Join us to plant the first seeds in the community garden.'),
(4, 'Recycling Workshop', '2023-10-10', '15:00', 'City Hall', 'Workshop to educate people about recycling practices.');


-- Insert data into VolunteerParticipates table to represent the many-to-many relationship between Volunteers and Campaigns
INSERT INTO VolunteerParticipates (CampaignID, VolunteerID)
VALUES
(1, 1),
(2, 1),
(1, 3),
(3, 2),
(2, 3),
(4, 1);

-- Insert data into EmployeeParticipates table to represent the many-to-many relationship between Employees and Campaigns
INSERT INTO EmployeeParticipates (CampaignID, EmployeeID)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 2),
(5, 1);

-- Insert data into Plan table to represent the many-to-many relationship between Campaigns and Organisations
INSERT INTO Plan (CampaignID, OrganisationID)
VALUES
(1, 1),
(2, 2),
(3, 1),
(4, 3),
(5, 4),
(6, 3);
