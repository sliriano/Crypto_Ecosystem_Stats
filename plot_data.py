from dbhelper import DBHelper
import matplotlib.dates
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go

def plot_marketcap(id):
    db = DBHelper()

    db.setup()

    data = db.get_eco_stats(id)

    dates = []
    mc = []

    for i in data:
        mc.append(i[2])
        dates.append(i[4])

    fig = go.Figure(go.Scatter(
        x = dates,
        y = mc
    ))

    fig.update_layout(
        xaxis_title = "Dates (UTC)\n(Month/Day/Hour)",
        yaxis_title = "Market Cap (Billions USD)",
        title = data[0][1] + " Market Capitalization Over Time", title_x=0.5)

    fig.update_xaxes(tickangle=45,
                    tickmode = 'array',
                    tickvals = dates[0::5])

    py.plot(fig)



    plt.plot(dates,mc)
    plt.ylabel("Market Cap (Hundreds of Billions)")
    plt.xlabel("Dates (UTC)\n(Month/Day/Hour)")
    plt.title(data[0][1] + " Market Capitalization Over Time")
    #plt.show()



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
    plt.xlabel("Dates (UTC)\n(Month/Day/Hour)")
    plt.title(data[0][1] + " Volume Over Time")
    plt.show()

plot_marketcap('smart-contract-platform')
#plot_volume('smart-contract-platform')
