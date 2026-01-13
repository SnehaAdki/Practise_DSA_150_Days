import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/SAI15/Downloads/Practise_DSA_150_Days-main/Pandas/data.csv')

df.plot()

plt.show()

df.plot(kind='scatter',x='Duration',y='Calories')

plt.show()

df['Calories'].plot(kind='hist')
plt.show()

df['Duration'].plot(kind='hist')
plt.show()

df['Pulse'].plot(kind='hist')
plt.show()