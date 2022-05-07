# Michael Vaden, Emily Pham, Teagan Norrgard

import sqlite3
import matplotlib.pyplot as plt
import schedule
import pandas as pd
import urllib.request


minutes = 0
data = []


def job():
    my_request = urllib.request.urlopen("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
    my_HTML = my_request.read().decode("utf8")
    spl = my_HTML.split(",")
    global data
    data.append(spl)
    global minutes
    minutes += 1
    # print(minutes)


schedule.every().minute.at(":15").do(job)


while minutes < 60:
    schedule.run_pending()

factor_list = []
pi_list = []
time_list = []

for i in data:
    factor_temp = i[0].split(":")
    factor_list.append(int(factor_temp[1]))
    pi_temp = i[1].split(":")
    pi_list.append(float(pi_temp[1]))
    time_temp = i[2].split(":")
    time_list.append(time_temp[1] + ":" + time_temp[2] + ":" + time_temp[3])

# print(factor_list)
# print(pi_list)
# print(time_list)

try:
    # Create connection to SQLite database
    con = sqlite3.connect('Final_DB')

    df = pd.DataFrame(list(zip(factor_list, pi_list, time_list)), columns= ['Factors', 'Pi', 'Time'])

    # push the data frame to the database
    df.to_sql('final_data', con, if_exists='replace', index=False)

    cur = con.cursor()

    # Fetch and display number of rows and columns from SQLite database
    cur.execute('SELECT * FROM final_data')
    numRows = len(cur.fetchall())
    cur.execute('PRAGMA table_info(final_data)')
    numCols = len(cur.fetchall())
    print("Number of Rows: ", numRows, "\nNumber of Columns: ", numCols)

    cur.execute('SELECT * FROM final_data')
    rows = cur.fetchall()

    # showing the relationship between factor and time (minute)
    for row in rows:
        print("factor: ", row[0], " minute (^3): ", int(row[2].split(":")[1])**3, " pi difference: ", abs(row[1] - 3.1415926535897932))
    # We can see that minute cubed is equal to factor for all minutes,
    # as well as that pi approaches the real value of pi (3.14159265...)

    # Show Factor vs Pi trend graph
    cur.execute('SELECT Factors, Pi, Time FROM final_data')
    graph_data = cur.fetchall()

    factors = []
    pi = []
    time = []

    for row in graph_data:
        factors.append(row[0])
        pi.append(row[1])
        time.append(row[2].split(":")[1])

    # Graph Factors vs Pi
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.xlim(1, 4000)
    plt.ylim(3.10, 3.20)
    ax1.set_title("Factors vs Pi")

    ax1.plot(factors, pi, '-', label="Pi", color='r')
    plt.show()
    # As we can see, as factor increases each minute,
    # the values of pi are upper and lower bounded approaching the real value of pi

    # Graph Pi over time
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    plt.xlim(0, 60)
    plt.ylim(3.00, 3.30)
    ax2.set_title("Pi over time")

    ax2.plot(time, pi, '-', label="Pi", color='r')
    plt.show()
    # Pi gets closer to the real value of Pi over time (3.14159265)

    # Graph Factors over time
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    plt.xlim(0, 60)
    plt.ylim(0, 250000)
    ax3.set_title("Factors over time")

    ax3.plot(time, factors, '-', label="Factors", color='r')
    plt.show()
    # Factors grows at an exponential (cubic) rate over time

    # Close connection
    con.close()
except ConnectionError:
    print("Connection Error Occurred")
