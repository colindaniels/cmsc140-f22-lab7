import pandas

filename = 'city_temperature.csv'

data = pandas.read_csv(filename, low_memory=False)

idx = data.loc[data.groupby(["Region"])["AvgTemperature"].idxmax()]


print(idx)

idx.to_csv('city_maxtemp.csv')
