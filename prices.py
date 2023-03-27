import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

house_price_data = pd.read_csv("./prices.csv")

# house_price_data["bedrooms"].value_counts().plot(kind="bar")

# plt.title('number of Bedroom')
# plt.xlabel('Bedrooms')
# plt.ylabel('Count')
# sns.despine
# plt.show()

# plt.figure(figsize=(10,10))
# sns.jointplot(x=house_price_data.lat.values, y=house_price_data.long.values, size=10)
# plt.ylabel('Longitude', fontsize=12)
# plt.xlabel('Latitude', fontsize=12)
# plt.show()
# plt1 = plt()
# sns.despine

plt.scatter(house_price_data.price, house_price_data.sqft_living)
plt.title("Price vs Square Feet")
plt.show()