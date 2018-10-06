#import
import os
import matplotlib.pyplot as plt
import pandas as pd
#load data
def load_data(data_path = "data"):
    csv_path = os.path.join(data_path,"kaggle_income.csv")
    return pd.read_csv(csv_path, encoding = "ISO-8859-1")
#Check data
income = load_data()
income.head()

income.info()

income.describe()

income["County"].value_counts()

#%matplotlib inline
income.hist(bins=50,figsize=(20,15))
plt.show()

income.plot(kind = "scatter", x = "Lon", y = "Lat", alpha = 0.2)

income.plot(kind = "scatter", x = "Lon", y = "Lat", alpha = 0.8, figsize=(40,30), 
           s = income["sum_w"]/100,label = "Weight",
           c = "Mean", cmap = plt.get_cmap("jet"), colorbar = True,)
plt.legend()

income.plot(kind = "scatter", x = "Lon", y = "Lat", alpha = 0.8, figsize=(40,30), 
           s = income["sum_w"]/100,label = "Weight",
           c = "Median", cmap = plt.get_cmap("jet"), colorbar = True,)
plt.legend()