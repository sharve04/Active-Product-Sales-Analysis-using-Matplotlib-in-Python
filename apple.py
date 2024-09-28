import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Order_details = pd.read_csv('Order_details(masked).csv')

# here we have taken Transaction
# date column
Order_details['Time'] = pd.to_datetime(Order_details['Transaction Date'])

# After that we extracted hour 
# from Transaction date column
Order_details['Hour'] = (Order_details['Time']).dt.hour

# n =24 in this case, can be modified
# as per need to see top 'n' busiest hours
timemost1 = Order_details['Hour'].value_counts().index.tolist()[:24]

timemost2 = Order_details['Hour'].value_counts().index.tolist()[:24]

tmost = np.column_stack((timemost1,timemost2))

print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))

timemost = Order_details['Hour'].value_counts()
timemost1 = []

for i in range(0,23):
    timemost1.append(i)

timemost2 = timemost.sort_index()
timemost2.to_list()
timemost2 = pd.DataFrame(timemost2)

plt.figure(figsize = (20,10))
plt.title("Sales per Hour)",fontdict = {'fontname':'monospace', 'fontsize':30},y = 1.05)
plt.ylabel("Number of Purchases", fontsize = 18, labelpad = 20)
plt.xlabel("Hour", fontsize = 18, labelpad = 20)
plt.plot(timemost1, timemost2, color = 'm')
plt.grid()
plt.show()
