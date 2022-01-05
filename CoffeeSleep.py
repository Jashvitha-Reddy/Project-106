import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffee_in_ml=[]
    sleep_in_hours=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee"]))
            sleep_in_hours.append(float(row["Sleep"]))
    
    return{"x":coffee_in_ml,"y":sleep_in_hours}

def findCorrelation(data_source):
    correlaton=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Coffee and Sleep is :\n",correlaton[0,1])

def plotFigure(data_path):
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x='Coffee',y='Sleep')
    fig.show()

def setup():
    data_path="IceCreamTempdata.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()




