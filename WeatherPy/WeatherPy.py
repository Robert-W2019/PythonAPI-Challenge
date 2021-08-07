#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


get_ipython().system('pip install citipy')


# In[2]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress



# Import API key
from api_keys import weather_api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[20]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[22]:


# URL for Weather Map API call

url = f"http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID={weather_api_key}"

#list of city data
city_data= []

#print to logger
print("Beginning Data Retrieval")
print("-"*15)

#create counters
record_count = 1
set_count = 1
import time
#loop through all the cities in our list
for index, city in enumerate(cities):
    #Group cities in sets of 50 for loggin purpose
    if (index % 50 == 0 and index >= 50):
        set_count += 1
        record_count = 0
    #endpoint url with each city
    city_url = url + "&q=" + city
    
    #log the url record and set number
    print (f'Processing Record {record_count} of Set {set_count} | {city}')
    time.sleep(3)
    record_count += 1
    
    #API requests for each of the cities
    try:
        #parse JSON and retrieve data
        city_weather = requests.get(city_url).json()
        
        #extract out max temp humidity and cloudiness
        city_lat = city_weather['coord']['lat']
        city_lng = city_weather['coord']['lon']
        city_max_temp = city_weather['main']['temp_max']
        city_humidity = city_weather['main']['humidity']
        city_clouds = city_weather['clouds']['all']
        city_wind = city_weather['wind']['speed']
        city_country = city_weather['sys']['country']
        city_date = city_weather['dt']
        
        #append the city info into city data list
        city_data.append({
            "City":city,
            "Lat":city_lat,
            "Lng":city_lng,
            "Max Temp":city_max_temp,
            "Humidity":city_humidity,
            "Cloudiness": city_clouds,
            "Wind Speed":city_wind,
            "Country": city_country,
            "Date":city_date   
        })
    
    except:
        print("City not found. Skipping ....")
        pass
    
#loading complete
print("--------------------")
print("Data Retrieval Complete")
print("--------------------")
        




# In[ ]:





# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[23]:


#convert array of JSON into pandas
city_data_df = pd.DataFrame(city_data)

#Extract relevant fields from the data frame
lats = city_data_df['Lat']
max_temps = city_data_df['Max Temp']
humidity = city_data_df['Humidity']
cloudiness = city_data_df['Cloudiness']
wind_speed = city_data_df['Wind Speed']


#Export the city data into a .csv.
city_data_df.to_csv(output_data_file, index_label='City_ID')


city_data_df.count()


# In[ ]:





# In[24]:


#Display the city Data Frame
city_data_df.head()


# In[ ]:





# ## Inspect the data and remove the cities where the humidity > 100%.
# ----
# Skip this step if there are no cities that have humidity > 100%. 

# In[ ]:





# In[27]:


#  Get the indices of cities that have humidity over 100%.
city_data_humidity_df = city_data_df.loc[(city_data_df['Humidity'] > 100)]
city_data_humidity_df.head()


# In[ ]:


#No humidity >100%


# In[ ]:


# Make a new DataFrame equal to the city data to drop all humidity outliers by index.
# Passing "inplace=False" will make a copy of the city_data DataFrame, which we call "clean_city_data".


# In[ ]:





# ## Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# ## Latitude vs. Temperature Plot

# In[29]:


# Build scatter plot for latitude vs. temperature
plt.scatter(lats,
           max_temps,
           edgecolor='black', linewidth=1, marker ='o',
           alpha=0.8, label='Cities')

#Incorporate the other graph properties
plt.title(f'City Latitude vs. Max Temperature (%s)' % time.strftime('%x'))
plt.ylabel('Max Temperature (F)')
plt.xlabel('Latitude')
plt.grid(True)

#Save the figure
plt.savefig('output_data/Fig1.png')

#Show plot
plt.show()



# In[ ]:





# ## Latitude vs. Humidity Plot

# In[35]:


# Build scatter plot for latitude vs. humidity
plt.scatter(lats,
           humidity,
           edgecolor='black', linewidth=1, marker ='o',
           alpha=0.8, label='Cities')

#Incorporate the other graph properties
plt.title(f'City Latitude vs. Humidity (%s)' % time.strftime('%x'))
plt.ylabel('Humidity (%)')
plt.xlabel('Latitude')
plt.grid(True)

#Save the figure
plt.savefig('output_data/Fig2.png')

#Show plot
plt.show()


# In[ ]:





# ## Latitude vs. Cloudiness Plot

# In[36]:


# Build scatter plot for latitude vs. cloudiness
plt.scatter(lats,
           cloudiness,
           edgecolor='black', linewidth=1, marker ='o',
           alpha=0.8, label='Cities')

#Incorporate the other graph properties
plt.title(f'City Latitude vs. Cloudiness (%s)' % time.strftime('%x'))
plt.ylabel('Cloudiness (%)')
plt.xlabel('Latitude')
plt.grid(True)

#Save the figure
plt.savefig('output_data/Fig3.png')

#Show plot
plt.show()


# In[ ]:





# ## Latitude vs. Wind Speed Plot

# In[37]:


# Build scatter plot for latitude vs. wind speed
plt.scatter(lats,
           wind_speed,
           edgecolor='black', linewidth=1, marker ='o',
           alpha=0.8, label='Cities')

#Incorporate the other graph properties
plt.title(f'City Latitude vs. Wind Speed (%s)' % time.strftime('%x'))
plt.ylabel('Wind Speed mph')
plt.xlabel('Latitude')
plt.grid(True)

#Save the figure
plt.savefig('output_data/Fig4.png')

#Show plot
plt.show()


# In[ ]:





# ## Linear Regression

# In[48]:


#OPTIONAL: Create a function to create Linear Regression plots
def plot_linear_regression(x_values, y_values, title, text_coordinates):
    
    #run regressions on southern hemisphere
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
    regress_values = x_values * slope + intercept
    line_eq = 'y = ' + str(round(slope,2)) + ' x + ' + str(round(intercept,2))
    
    #plot
    plt.scatter(x_values,y_values)
    plt.plot(x_values,regress_values, 'r-')
    plt.annotate(line_eq, text_coordinates, fontsize=15, color='red')
    plt.xlabel('Latitude')
    plt.ylabel(title)
    print(f'The r-squared is: {rvalue}')
    plt.show()



# In[49]:


#Northern and southern hemisphere DataFrames
northern_hemi_df = city_data_df.loc[(city_data_df['Lat'] >= 0)]
southern_hemi_df = city_data_df.loc[(city_data_df['Lat'] < 0)]


# ####  Northern Hemisphere - Max Temp vs. Latitude Linear Regression

# In[50]:


x_values = northern_hemi_df['Lat']
y_values = northern_hemi_df['Max Temp']
plot_linear_regression(x_values, y_values, 'Max Temp', (6,30))


# In[ ]:





# ####  Southern Hemisphere - Max Temp vs. Latitude Linear Regression

# In[52]:


x_values = southern_hemi_df['Lat']
y_values = southern_hemi_df['Max Temp']
plot_linear_regression(x_values, y_values, 'Max Temp', (-30,40))


# In[ ]:





# ####  Northern Hemisphere - Humidity (%) vs. Latitude Linear Regression

# In[53]:


x_values = northern_hemi_df['Lat']
y_values = northern_hemi_df['Humidity']
plot_linear_regression(x_values, y_values, 'Humidity', (40,10))


# In[ ]:





# ####  Southern Hemisphere - Humidity (%) vs. Latitude Linear Regression

# In[54]:


x_values = southern_hemi_df['Lat']
y_values = southern_hemi_df['Humidity']
plot_linear_regression(x_values, y_values, 'Humidity', (-30,150))


# In[ ]:





# ####  Northern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

# In[55]:


x_values = northern_hemi_df['Lat']
y_values = northern_hemi_df['Cloudiness']
plot_linear_regression(x_values, y_values, 'Cloudiness', (40,30))


# In[ ]:





# ####  Southern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

# In[56]:


x_values = southern_hemi_df['Lat']
y_values = southern_hemi_df['Cloudiness']
plot_linear_regression(x_values, y_values, 'Cloudiness', (-30,30))


# In[ ]:





# ####  Northern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

# In[57]:


x_values = northern_hemi_df['Lat']
y_values = northern_hemi_df['Wind Speed']
plot_linear_regression(x_values, y_values, 'Wind Speed', (40,25))


# In[ ]:





# ####  Southern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

# In[58]:


x_values = southern_hemi_df['Lat']
y_values = southern_hemi_df['Wind Speed']
plot_linear_regression(x_values, y_values, 'Wind Speed', (-30,30))


# In[ ]:





# In[ ]:




