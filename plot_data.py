from dbhelper import DBHelper
import matplotlib.dates
import matplotlib.pyplot as plt

def plot_marketcap(id):
    db = DBHelper()

    db.setup()

    data = db.get_eco_stats(id)

    x = []
    y = []

    for i in data:
        x.append(i[2])
        y.append(i[4])

    dates = x
    mc = y

    plt.plot(mc,dates)
    plt.ylabel("Market Cap")
    plt.xlabel("Dates")
    plt.title(data[0][1] + " Market Capitalization Over Time")
    plt.show()

def plot_volume(id):
    db = DBHelper()

    db.setup()

    data = db.get_eco_stats(id)

    x = []
    y = []

    for i in data:
        x.append(i[3])
        y.append(i[4])

    dates = x
    volume = y

    plt.plot(volume,dates)
    plt.ylabel("Volume")
    plt.xlabel("Dates")
    plt.title(data[0][1] + " Volume Over Time")
    plt.show()

# plot_marketcap('smart-contract-platform')
plot_volume('smart-contract-platform')