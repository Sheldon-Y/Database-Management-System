import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="Sheldon", 
            user="postgres", 
            password="123", 
            host="localhost"
        )
        print("Connection to PostgreSQL DB successful")
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None

connection = create_connection()

def exit_application():
    if connection:
        connection.close()
    print("Exiting the application...")
    exit(0)

def query_menu():
    print("Please select an option:")
    print("QA: Query all currently active campaigns")
    print("QB: Query volunteers who have participated more than 3 times")
    print("QC: Query donors who have donated more than 1000")
    print("QD: Query the number of volunteers participating in each campaign")
    print("QE: Query the total donation amount for each campaign")
    print("QF: Query all volunteers who have participated in at least one campaign")
    print("QG: Query the list of employees participating in a specific campaign")
    print("QH: Query employees who have not participated in any campaigns")
    print("QI: Query the number of campaigns each organisation is responsible for")
    print("QJ: Query all campaigns with a cost above the average cost")
    print("QK: Query campaign events")
    print("QL: Query financial summary")
    print("QM: Query detailed financial report")

def query_choice(choice):
    if choice == "QA":
        query = """
        SELECT * FROM Campaign WHERE Status = 'Active';
        """
        query_execute(connection, query)
    elif choice == "QB":
        query = """
        SELECT Name, ContactInfo FROM Volunteer WHERE ParticipationCount > 3;
        """
        query_execute(connection, query)
    elif choice == "QC":
        query = """
        SELECT Name, ContactInfo FROM Donor
        WHERE DonateAmount > 1000;
        """
        query_execute(connection, query)
    elif choice == "QD":
        query = """
        SELECT c.Name, COUNT(vp.VolunteerID) AS VolunteerCount
        FROM Campaign c
        JOIN VolunteerParticipates vp ON c.CampaignID = vp.CampaignID
        GROUP BY c.Name;
        """
        query_execute(connection, query)
    elif choice == "QE":
        query = """
        SELECT c.Name, SUM(d.DonateAmount) AS TotalDonations
        FROM Campaign c
        JOIN Donor d ON c.CampaignID = d.DonorID
        GROUP BY c.Name;
        """
        query_execute(connection, query)
    elif choice == "QF":
        query = """
        SELECT DISTINCT v.Name, v.ContactInfo
        FROM Volunteer v
        JOIN VolunteerParticipates vp ON v.VolunteerID = vp.VolunteerID;
        """
        query_execute(connection, query)
    elif choice == "QG":
        query = """
        SELECT e.Name, e.Role
        FROM Employees e
        JOIN EmployeeParticipates ep ON e.EmployeeID = ep.EmployeeID
        WHERE ep.CampaignID = 1;
        
        """
        query_execute(connection, query)
    elif choice == "QH":
        query = """
        SELECT e.Name, e.Role
        FROM Employees e
        WHERE NOT EXISTS (
        SELECT 1 FROM EmployeeParticipates ep WHERE ep.EmployeeID = e.EmployeeID
        );
        """
        query_execute(connection, query)
    elif choice == "QI":
        query = """
        SELECT o.Location, COUNT(c.CampaignID) AS CampaignCount
        FROM Organisation o
        JOIN Campaign c ON o.OrganisationID = c.CampaignID
        GROUP BY o.Location;
        """
        query_execute(connection, query)
    elif choice == "QJ":
        query = """
        SELECT Name, Cost
        FROM Campaign
        WHERE Cost > (SELECT AVG(Cost) FROM Campaign);
        """
        query_execute(connection, query)
    elif choice == "QK":
        campaign_id = input("Enter campaign ID (leave blank for all events): ")
        campaign_id = int(campaign_id) if campaign_id.strip().isdigit() else None
        query_campaign_events(connection, campaign_id)
    return

def query_execute(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"An error '{e}' occurred")

def query_campaign_events(connection, campaign_id=None):
    cursor = connection.cursor()
    if campaign_id:
        query = "SELECT * FROM CampaignEvent WHERE CampaignID = %s;"
        print(f"Querying events for campaign ID {campaign_id}:")
        cursor.execute(query, (campaign_id,))
    else:
        query = "SELECT * FROM CampaignEvent;"
        print("Querying all events:")
        cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

def exit_application():
    print("Exiting the application...")

def sql_menu():
    print("Please select an operation to perform:")
    print("AA: Add a new campaign")
    print("AB: Add a new volunteer")
    print("AC: Add a new donor")
    print("AD: Add a new organisation")
    print("AE: Add a new employee")
    print("AF: Add a new website update")
    print("AG: Add a new event to a campaign")
    print("AH: Add a volunteer participation in a campaign")
    print("AI: Add an employee participation in a campaign")
    print("AJ: Add a relationship between an organisation and a website update")
    print("AK: Add a plan for a campaign and an organisation")

def sql_choice(choice):
    if choice == "AA":
        sql_add_campaign(connection)
    elif choice == "AB":
        sql_add_volunteer(connection)
    elif choice == "AC":
        sql_add_donor(connection)
    elif choice == "AD":
        sql_add_organisation(connection)
    elif choice == "AE":
        sql_add_employee(connection)
    elif choice == "AF":
        sql_add_website_update(connection)
    elif choice == "AG":
        sql_add_campaign_event(connection)
    elif choice == "AH":
        sql_add_volunteer_participation(connection)
    elif choice == "AI":
        sql_add_employee_participation(connection)
    elif choice == "AJ":
        sql_add_organisation_web_relation(connection)
    elif choice == "AK":
        sql_add_campaign_organisation_plan(connection)

def sql_add_campaign(connection):
    print("Adding a new campaign...")
    name = input("Enter campaign name: ")
    description = input("Enter campaign description: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    region = input("Enter region: ")
    status = input("Enter status (Planning/Active/Completed): ")
    cost = input("Enter cost: ")
    campaign_type = input("Enter campaign type: ")
    query = """
    INSERT INTO Campaign (Name, Description, StartDate, EndDate, Region, Status, Cost, Type)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (name, description, start_date, end_date, region, status, cost, campaign_type))
        connection.commit()
        print("Campaign added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_volunteer(connection):
    print("Adding a new volunteer...")
    name = input("Enter volunteer name: ")
    contact_info = input("Enter contact info: ")
    participation_count = input("Enter participation count: ")
    level = input("Enter level (New/Intermediate/Expert): ")
    join_date = input("Enter join date (YYYY-MM-DD): ")
    query = """
    INSERT INTO Volunteer (Name, ContactInfo, ParticipationCount, Level, JoinDate)
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (name, contact_info, participation_count, level, join_date))
        connection.commit()
        print("Volunteer added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_donor(connection):
    print("Adding a new donor...")
    name = input("Enter donor name: ")
    contact_info = input("Enter contact info: ")
    donate_amount = input("Enter donate amount: ")
    query = """
    INSERT INTO Donor (Name, ContactInfo, DonateAmount)
    VALUES (%s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (name, contact_info, donate_amount))
        connection.commit()
        print("Donor added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_organisation(connection):
    print("Adding a new organisation...")
    location = input("Enter location: ")
    goal = input("Enter goal: ")
    number_of_people = input("Enter number of people: ")
    query = """
    INSERT INTO Organisation (Location, Goal, NumberOfPeople)
    VALUES (%s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (location, goal, number_of_people))
        connection.commit()
        print("New organisation added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_employee(connection):
    print("Adding a new employee...")
    name = input("Enter employee name: ")
    role = input("Enter role: ")
    salary = input("Enter salary: ")
    contact_info = input("Enter contact info: ")
    organisation_id = input("Enter organisation ID: ")
    query = """
    INSERT INTO Employees (Name, Role, Salary, ContactInfo, OrganisationID)
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (name, role, salary, contact_info, organisation_id))
        connection.commit()
        print("Employee added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_website_update(connection):
    print("Adding a new website update...")
    campaign_id = input("Enter campaign ID: ")
    publish_date = input("Enter publish date (YYYY-MM-DD): ")
    content = input("Enter content: ")
    organisation_id = input("Enter organisation ID: ")
    query = """
    INSERT INTO Website (CampaignID, PublishDate, Content, OrganisationID)
    VALUES (%s, %s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (campaign_id, publish_date, content, organisation_id))
        connection.commit()
        print("Website update added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_campaign_event(connection):
    print("Adding a new event to a campaign...")
    campaign_id = input("Enter campaign ID: ")
    event_name = input("Enter event name: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    event_time = input("Enter event time (HH:MM): ")
    location = input("Enter location: ")
    description = input("Enter description: ")
    query = """
    INSERT INTO CampaignEvent (CampaignID, EventName, EventDate, EventTime, Location, Description)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (campaign_id, event_name, event_date, event_time, location, description))
        connection.commit()
        print("Event added to campaign successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_volunteer_participation(connection):
    print("Adding a volunteer participation in a campaign...")
    volunteer_id = input("Enter volunteer ID: ")
    campaign_id = input("Enter campaign ID: ")
    query = """
    INSERT INTO VolunteerParticipates (VolunteerID, CampaignID)
    VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (volunteer_id, campaign_id))
        connection.commit()
        print("Volunteer participation added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_employee_participation(connection):
    print("Adding an employee participation in a campaign...")
    employee_id = input("Enter employee ID: ")
    campaign_id = input("Enter campaign ID: ")
    query = """
    INSERT INTO EmployeeParticipates (EmployeeID, CampaignID)
    VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (employee_id, campaign_id))
        connection.commit()
        print("Employee participation added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_organisation_web_relation(connection):
    print("Adding a relationship between an organisation and a website update...")
    organisation_id = input("Enter organisation ID: ")
    web_id = input("Enter web ID: ")
    query = """
    INSERT INTO Transacts (OrganisationID, WebID)
    VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (organisation_id, web_id))
        connection.commit()
        print("Organisation and website relation added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def sql_add_campaign_organisation_plan(connection):
    print("Adding a plan for a campaign and an organisation...")
    campaign_id = input("Enter campaign ID: ")
    organisation_id = input("Enter organisation ID: ")
    query = """
    INSERT INTO Plan (CampaignID, OrganisationID)
    VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (campaign_id, organisation_id))
        connection.commit()
        print("Campaign and organisation plan added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def query_financial_summary(connection):
    print("Financial Summary:")
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(DonateAmount) FROM Donor;")
    total_donations = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(Cost) FROM Campaign;")
    total_costs = cursor.fetchone()[0] or 0
    print(f"Total Donations: {total_donations}")
    print(f"Total Costs: {total_costs}")
    print_financial_bar_chart(total_donations, total_costs)

def print_financial_bar_chart(total_donations, total_costs, detailed_report=None):
    if detailed_report:
        print("Detailed Financial Bar Chart:")
        max_donation = max(row[2] for row in detailed_report)
        max_cost = max(row[1] for row in detailed_report)
        max_value = max(max_donation, max_cost, 1)
        bar_length = 40
        for campaign, cost, donations in detailed_report:
            donation_bar = '#' * int((donations / max_value) * bar_length)
            cost_bar = '#' * int((cost / max_value) * bar_length)
            print(f"{campaign[:20]:20} | Donations: [{donation_bar.ljust(bar_length)}] {donations}")
            print(f"{' ':20} | Costs:     [{cost_bar.ljust(bar_length)}] {cost}")
    else:
        print("Financial Summary Bar Chart:")
        max_value = max(total_donations, total_costs, 1)
        bar_length = 40
        donation_bar = '#' * int((total_donations / max_value) * bar_length)
        cost_bar = '#' * int((total_costs / max_value) * bar_length)
        print(f"Donations: [{donation_bar.ljust(bar_length)}] {total_donations}")
        print(f"Costs:     [{cost_bar.ljust(bar_length)}] {total_costs}")

def query_detailed_financial_report(connection):
    print("Detailed Financial Report:")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.Name, c.Cost, COALESCE(SUM(d.DonateAmount), 0) AS Donations
        FROM Campaign c
        LEFT JOIN Donor d ON c.CampaignID = d.DonorID
        GROUP BY c.Name, c.Cost
    """)
    detailed_report = cursor.fetchall()
    for row in detailed_report:
        print(f"Campaign: {row[0]}, Cost: {row[1]}, Donations: {row[2]}")

def generate_dynamic_report(connection):
    print("Generate Custom Report")
    start_date = input("Enter start date (YYYY-MM-DD) or leave blank: ")
    end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ")
    region = input("Enter region or leave blank: ")
    campaign_type = input("Enter campaign type or leave blank: ")
    where_clauses = []
    params = []
    if start_date:
        where_clauses.append("c.StartDate >= %s")
        params.append(start_date)
    if end_date:
        where_clauses.append("c.EndDate <= %s")
        params.append(end_date)
    if region:
        where_clauses.append("c.Region = %s")
        params.append(region)
    if campaign_type:
        where_clauses.append("c.Type = %s")
        params.append(campaign_type)
    base_query = """
    SELECT c.Name, c.StartDate, c.EndDate, c.Region, c.Type, COUNT(vp.VolunteerID) AS VolunteerCount
    FROM Campaign c
    LEFT JOIN VolunteerParticipates vp ON c.CampaignID = vp.CampaignID
    """
    if where_clauses:
        base_query += " WHERE " + " AND ".join(where_clauses)
    base_query += " GROUP BY c.Name, c.StartDate, c.EndDate, c.Region, c.Type"
    cursor = connection.cursor()
    try:
        cursor.execute(base_query, tuple(params))
        reports = cursor.fetchall()
        print("Custom Report:")
        for report in reports:
            print(f"Campaign: {report[0]}, Date: {report[1]} to {report[2]}, Region: {report[3]}, Type: {report[4]}, Volunteer Count: {report[5]}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

def main():
    connection = create_connection()
    if connection is None:
        return
    options = {
        'Exit': ("Exit the application", exit_application),
        'QA': ("Query all currently active campaigns", lambda: query_choice('QA')),
        'QB': ("Query volunteers who have participated more than 3 times", lambda: query_choice('QB')),
        'QC': ("Query donors who have donated more than 1000", lambda: query_choice('QC')),
        'QD': ("Query the number of volunteers participating in each campaign", lambda: query_choice('QD')),
        'QE': ("Query the total donation amount for each campaign", lambda: query_choice('QE')),
        'QF': ("Query all volunteers who have participated in at least one campaign", lambda: query_choice('QF')),
        'QG': ("Query the list of employees participating in a specific campaign", lambda: query_choice('QG')),
        'QH': ("Query employees who have not participated in any campaigns", lambda: query_choice('QH')),
        'QI': ("Query the number of campaigns each organisation is responsible for", lambda: query_choice('QI')),
        'QJ': ("Query all campaigns with a cost above the average cost", lambda: query_choice('QJ')),
        'QK': ("Query campaign events", lambda: query_choice('QK')),
        'QL': ("Query financial summary", lambda: query_financial_summary(connection)),
        'QM': ("Query detailed financial report", lambda: query_detailed_financial_report(connection)),
        'AA': ("Add a new campaign", lambda: sql_choice('AA')),
        'AB': ("Add a new volunteer", lambda: sql_choice('AB')),
        'AC': ("Add a new donor", lambda: sql_choice('AC')),
        'AD': ("Add a new organisation", lambda: sql_choice('AD')),
        'AE': ("Add a new employee", lambda: sql_choice('AE')),
        'AF': ("Add a new website update", lambda: sql_choice('AF')),
        'AG': ("Add a new event to a campaign", lambda: sql_choice('AG')),
        'AH': ("Add a volunteer participation in a campaign", lambda: sql_choice('AH')),
        'AI': ("Add an employee participation in a campaign", lambda: sql_choice('AI')),
        'AJ': ("Add a relationship between an organisation and a website update", lambda: sql_choice('AJ')),
        'AK': ("Add a plan for a campaign and an organisation", lambda: sql_choice('AK')),
        'GR': ("Generate custom report", lambda: generate_dynamic_report(connection))
    }
    print("Please select an option:")
    for key, (description, _) in options.items():
        print(f"{key}: {description}")
    while True:
        choice = input("Enter your choice: ")
        if choice in options:
            action = options[choice][1] 
            action()
            if choice == 'Exit':
                break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
