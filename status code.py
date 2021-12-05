import pandas as pd
import requests
df= pd.read_csv('D:\\New folder\\discover_not_index.csv')
for url in df['urls']:
   response= requests.get(url)
   status= response.status_code
   df['status']=status
   df.to_csv('status_codes.csv')
for url in df['urls']:
  response= requests.get(url)
  status= response.status_code
  df['status']=status
  if status == 403:
    print(url)