
## Campaign

| CampaignID (PK) | Name            | Description                                 | StartDate  | EndDate    | Region | Status   | Cost | Type        |
|-----------------|-----------------|---------------------------------------------|------------|------------|--------|----------|------|-------------|
| 1               | Clean the City  | A campaign to clean up the city streets.    | 2023-07-01 | 2023-07-14 | Urban  | Active   | 1500 | Cleanup     |
| 2               | Plant a Tree    | A campaign to plant trees in the city park. | 2023-08-01 | 2023-08-30 | Urban  | Active   | 1200 | Environment |
| 3               | Save Water      | Raise awareness about water conservation.   | 2023-09-01 | 2023-09-15 | Rural  | Planning | 1000 | Awareness   |

## Volunteer

| VolunteerID (PK) | Name        | ContactInfo             | ParticipationCount | Level        | JoinDate   |
|------------------|-------------|-------------------------|--------------------|--------------|------------|
| 1                | Alice Smith | alice.smith@example.com | 4                  | Expert       | 2022-06-01 |
| 2                | Bob Jones   | bob.jones@example.com   | 2                  | Intermediate | 2022-07-01 |
| 3                | Carol White | carol.white@example.com | 5                  | Expert       | 2022-05-15 |

## Donor

| DonorID (PK) | Name       | ContactInfo            | DonateAmount |
|--------------|------------|------------------------|--------------|
| 1            | David Grey | david.grey@example.com | 5000         |
| 2            | Emma Brown | emma.brown@example.com | 2500         |

## Employees

| EmployeeID (PK) | Name                 | Role                  | Salary | ContactInfo             | OrganisationID (FK) |
|-----------------|----------------------|-----------------------|--------|-------------------------|---------------------|
| 1               | Frank Black          | Project Manager       | 75000  | frank.black@example.com | 1                   |
| 2               | Gina Red             | Volunteer Coordinator | 65000  | gina.red@example.com    | 1                   |
| 3               | Helen Nonparticipant | Marketing             | 60000  | helen.nonparticipant@example.com | 2        |

## Website

| WebID (PK) | CampaignID (FK) | PublishDate | Content                                       | OrganisationID (FK) |
|------------|-----------------|-------------|-----------------------------------------------|---------------------|
| 1          | 1               | 2023-07-02  | Join us this weekend to make our city clean! | 1                   |
| 2          | 2               | 2023-08-02  | Help us increase the green space in our park.| 1                   |

## Organisation

| OrganisationID (PK) | Location | Goal                                                 | NumberOfPeople |
|---------------------|----------|------------------------------------------------------|----------------|
| 1                   | Downtown | To make the city greener and cleaner.                | 10             |
| 2                   | Suburbs  | To engage the community in environmental activities. | 20             |

## Transacts

| OrganisationID (FK) | WebID (FK) |
|---------------------|------------|
| 1                   | 1          |
| 2                   | 2          |

## VolunteerParticipates

| CampaignID (FK) | VolunteerID (FK) |
|-----------------|------------------|
| 1               | 1                |
| 2               | 1                |
| 1               | 3                |

## EmployeeParticipates

| CampaignID (FK) | EmployeeID (FK) |
|-----------------|-----------------|
| 1               | 1               |
| 2               | 2               |

## Plan

| CampaignID (FK) | OrganisationID (FK) |
|-----------------|---------------------|
| 1               | 1                    |
| 2               | 2                    |
| 3               | 1                    |

