from dbhelper import DBHelper
import matplotlib.dates
import matplotlib.pyplot as plt

def plot_marketcap(id):
    db = DBHelper()

    db.setup()

    data = db.get_eco_stats(id)

    dates = []
    mc = []

    for i in data:
        mc.append(i[2])
        dates.append(i[4])

    plt.plot(mc,dates)
    plt.ylabel("Market Cap")
    plt.xlabel("Dates")
    plt.title(data[0][1] + " Market Capitalization Over Time")
    plt.show()

def plot_volume(id):
    db = DBHelper()

    db.setup()

    data = db.get_eco_stats(id)

    dates = []
    volume = []

    for i in data:
        volume.append(i[3])
        dates.append(i[4])

    plt.plot(dates,volume)
    plt.ylabel("Volume")
    plt.xlabel("Dates")
    plt.title(data[0][1] + " Volume Over Time")
    plt.show()

#plot_marketcap('smart-contract-platform')
plot_volume('smart-contract-platform')