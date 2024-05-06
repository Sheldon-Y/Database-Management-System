-- Query 1: Find all currently active campaigns
SELECT * FROM Campaign
WHERE Status = 'Active';

-- Query 2: Find volunteers who have participated more than 3 times
SELECT Name, ContactInfo FROM Volunteer
WHERE ParticipationCount > 3;

-- Query 3: Find donors who have donated more than 1000
SELECT Name, ContactInfo FROM Donor
WHERE DonateAmount > 1000;

-- Query 4: Calculate the number of volunteers participating in each campaign
SELECT c.Name, COUNT(vp.VolunteerID) AS VolunteerCount
FROM Campaign c
JOIN VolunteerParticipates vp ON c.CampaignID = vp.CampaignID
GROUP BY c.Name;

-- Query 5: Find the total donation amount for each campaign
SELECT c.Name, SUM(d.DonateAmount) AS TotalDonations
FROM Campaign c
JOIN Donor d ON c.CampaignID = d.DonorID
GROUP BY c.Name;

-- Query 6: Find all volunteers who have participated in at least one campaign
SELECT DISTINCT v.Name, v.ContactInfo
FROM Volunteer v
JOIN VolunteerParticipates vp ON v.VolunteerID = vp.VolunteerID;

-- Query 7: Find the list of employees participating in a specific campaign (e.g., CampaignID = 1)
SELECT e.Name, e.Role
FROM Employees e
JOIN EmployeeParticipates ep ON e.EmployeeID = ep.EmployeeID
WHERE ep.CampaignID = 1;

-- Query 8: Find employees who have not participated in any campaigns
SELECT e.Name, e.Role
FROM Employees e
WHERE NOT EXISTS (
  SELECT 1 FROM EmployeeParticipates ep WHERE ep.EmployeeID = e.EmployeeID
);

-- Query 9: Find the number of campaigns each organisation is responsible for
SELECT o.Location, COUNT(c.CampaignID) AS CampaignCount
FROM Organisation o
JOIN Campaign c ON o.OrganisationID = c.CampaignID
GROUP BY o.Location;

-- Query 10: Find all campaigns with a cost above the average cost
SELECT Name, Cost
FROM Campaign
WHERE Cost > (SELECT AVG(Cost) FROM Campaign);
