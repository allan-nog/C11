
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dataset = pd.read_csv('airtravel.csv', index_col='Date', parse_dates=True)

dataset['Passengers'].plot(figsize=(8, 6), title='Passageiros por mês')
plt.show()

decomposition = seasonal_decompose(dataset['Passengers'], model='multiplicative', period=12)

decomposition.plot()
plt.tight_layout()
plt.show()

dataset = pd.read_csv('co2_emissions.csv')

dataset['Year'] = pd.to_datetime(dataset['Year'], format='%Y')
dataset = dataset.set_index('Year')

dataset['CO2_Emissions'].plot(figsize=(8, 6), title='Emissões de CO2 por ano')
plt.show()

decomposition = seasonal_decompose(dataset['CO2_Emissions'], model='additive', period=8)

decomposition.plot()
plt.tight_layout()
plt.show()
