# Michael Vaden, mtv2eva
import pandas as pd
import sqlite3

# Given data is a data frame of every NFL head coaching season and relevant statistics, found on Kaggle
# Read in data as CSV from local computer file path
data = pd.read_csv('/Users/michaelvaden/Downloads/nfl_head_coach_performance.csv')
# Examine the first 5 rows of the data
print(data.head())

# Remove a column from the data
data.pop("Result")

# View columns again to see that the Result column has been removed
print(data.columns)

# Take input to convert to JSON or SQL, check for valid input
valid = False
option = 0

while not valid:
    option = int(input("Enter 1 to convert to JSON, Enter 2 to convert to SQL: "))
    if option == 1 or option == 2:
        valid = True
    else:
        print("You must enter 1 or 2: ")

if option == 1:
    # Convert data to JSON
    data.to_json('/Users/michaelvaden/Downloads/nfl_head_coach_performance.json')
    # Create Pandas Data Frame from JSON File
    df = pd.read_json('/Users/michaelvaden/Downloads/nfl_head_coach_performance.json')

    # Display number of rows and columns from Data Frame
    numRows = len(df.axes[0])
    numCols = len(df.axes[1])
    print("Number of Rows: ", numRows, "\nNumber of Columns: ", numCols)

else:
    # Convert data to SQL
    # Try statement to account for potential errors
    try:
        # Create connection to SQLite database
        con = sqlite3.connect('Coaches.db')

        data.to_sql('coaching_seasons', con, if_exists='replace', index=False)

        cur = con.cursor()
        # Fetch and display number of rows and columns from SQLite database
        cur.execute('SELECT * FROM coaching_seasons')
        numRows = len(cur.fetchall())
        cur.execute('PRAGMA table_info(coaching_seasons)')
        numCols = len(cur.fetchall())

        print("Number of Rows: ", numRows, "\nNumber of Columns: ", numCols)
        # Close connection
        con.close()
    except ConnectionError:
        print("Connection Error Occurred")
