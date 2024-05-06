# Database-Management-System

Developed a comprehensive database management system using Python and PostgreSQL to manage and automate tasks related to campaigns, volunteers, donors, and organizational events.

1. **Database Connection Establishment**:
   - **Functionality**: Creates and manages connections to a PostgreSQL database.
   - **Implementation Method**: Utilizes the `psycopg2` library to connect to the database, handling potential errors and ensuring successful database interactions.
2. **Data Querying and Management**:
   - **Functionality**: Supports a variety of queries to retrieve and manipulate data related to campaigns, donors, volunteers, and employees.
   - **Implementation Method**: Provides a menu-driven interface to execute predefined SQL queries, dynamically executing SQL statements based on user inputs and displaying results.
3. **Data Insertion and Update**:
   - **Functionality**: Allows users to add new data entries for campaigns, volunteers, donors, and other entities.
   - **Implementation Method**: Implements form-based input collection in the console, executing insert SQL commands and handling transactions with commit and rollback functionalities.
4. **Report Generation**:
   - **Functionality**: Generates financial summaries and detailed reports, along with custom dynamic reports based on user-defined filters.
   - **Implementation Method**: Executes complex SQL queries to aggregate and analyze financial data, outputting results and visualizing data through text-based bar charts.
5. **Interactive User Interface**:
   - **Functionality**: Provides a user-friendly, interactive command-line interface for database management.
   - **Implementation Method**: Utilizes a loop-based approach to handle user inputs and execute corresponding functions, enhancing user engagement and operational efficiency.
