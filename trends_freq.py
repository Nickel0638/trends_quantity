import pandas as pd
from pytrends.request import TrendReq

# process connection
pytrends = TrendReq(hl='en-US', tz=360)

# keywords list
kw_list = ['Python','PhP','Java', 'javascript']

# build request
pytrends.build_payload(kw_list, timeframe='today 12-m', geo='US')

# reciev data from Google trends
interest_over_time_df = pytrends.interest_over_time()

# check data
if not interest_over_time_df.empty:
    print(interest_over_time_df.head())  # Виведення перших кількох рядків, якщо дані існують
else:
    print('No data was returned')
