# Code to download data freely available on https://data.humdata.org/dataset/
# name of dataset comes from  https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases


from hdx.hdx_configuration import Configuration 
from hdx.data.dataset import Dataset
import pandas as pd
Configuration.create(hdx_site='prod', user_agent='A_Quick_Example', hdx_read_only=True)
dataset = Dataset.read_from_hdx('novel-coronavirus-2019-ncov-cases')  # name of the dataset, see above
resources = dataset.get_resources()
#print(resources)

# resource id (e.g., resource[id]) comes from the number of the dataset you see on the dataset page
# e.g., on this page id=0 is time_series_covid19_confirmed_global.csv
url, path = resources[0].download()
#print(url, ' ::  ',path)
#print('Resource URL %s downloaded to %s' % (url, path))

dfIn=pd.read_csv(path)
print(dfIn)




