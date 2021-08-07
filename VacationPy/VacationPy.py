#!/usr/bin/env python
# coding: utf-8

# # VacationPy
# ----
# 
# #### Note
# * Keep an eye on your API usage. Use https://developers.google.com/maps/reporting/gmp-reporting as reference for how to monitor your usage and billing.
# 
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


get_ipython().system(' pip3 install gmaps')


# In[19]:


get_ipython().system(' jupyter nbextension enable --py gmaps')


# In[20]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import gmaps
import os

# Import API key
from api_keys import g_key


# In[ ]:





# ### Store Part I results into DataFrame
# * Load the csv exported in Part I to a DataFrame

# In[24]:


city_data_df = pd.read_csv('output_data/cities.csv')
city_data_df.head()


# ### Humidity Heatmap
# * Configure gmaps.
# * Use the Lat and Lng as locations and Humidity as the weight.
# * Add Heatmap layer to map.

# In[25]:


#config gmaps
gmaps.configure(api_key=g_key)


# In[26]:


#heatmap of humidity
locations = city_data_df[['Lat', 'Lng']]
humidity = city_data_df['Humidity']
fig = gmaps.figure()
heat_layer = gmaps.heatmap_layer(locations, weights=humidity, dissipating=False, max_intensity=300, point_radius=5)

fig.add_layer(heat_layer)
fig


# ### Create new DataFrame fitting weather criteria
# * Narrow down the cities to fit weather conditions.
# * Drop any rows will null values.

# In[32]:


#Narrow down the cities to fit weather conditions and Drop any rows will null values
narrowed_city_df = city_data_df.loc[(city_data_df['Max Temp'] < 80) & (city_data_df['Max Temp'] > 70)                                     & (city_data_df['Wind Speed'] < 10)                                     & (city_data_df['Cloudiness'] == 0)]
narrowed_city_df.dropna()

narrowed_city_df


# ### Hotel Map
# * Store into variable named `hotel_df`.
# * Add a "Hotel Name" column to the DataFrame.
# * Set parameters to search for hotels with 5000 meters.
# * Hit the Google Places API for each city's coordinates.
# * Store the first Hotel result into the DataFrame.
# * Plot markers on top of the heatmap.

# In[33]:


# Create DataFrame named hotel_df and Add a "Hotel Name" column to the DataFrame
hotel_df = narrowed_city_df[['City', 'Country', 'Lat', 'Lng']].copy()
hotel_df['Hotel Name'] = ""
hotel_df


# In[38]:


params = {
    'radius': 5000,
    'types': 'lodging',
    'key': g_key
    
}

for index, row in hotel_df.iterrows():
    #get latitude and longitude
    lat = row['Lat']
    lng = row['Lng']
    
    params['location'] = f"{lat},{lng}"
    
    #use the search term 'hotel' and produce the lat/lng 
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    
    name_address = requests.get(base_url, params=params).json()
    
    try:
        hotel_df.loc[index, 'Hotel Name'] = name_address['results'][0]['name']
    except(KeyError, IndexError):
        print('Missing field/result... skipping...')
        
hotel_df


# In[39]:


# NOTE: Do not change any of the code in this cell

# Using the template add the hotel marks to the heatmap
info_box_template = """
<dl>
<dt>Name</dt><dd>{Hotel Name}</dd>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
</dl>
"""
# Store the DataFrame Row
# NOTE: be sure to update with your DataFrame name
hotel_info = [info_box_template.format(**row) for index, row in hotel_df.iterrows()]
locations = hotel_df[["Lat", "Lng"]]


# In[40]:


# Add marker layer ontop of heat map
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)

fig.add_layer(marker_layer)

# Display figure
fig


# In[ ]:




