# PythonAPI-Challenge

## WeatherPy

# Generate Cities List

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Max Temp</th>
      <th>Humidity</th>
      <th>Cloudiness</th>
      <th>Wind Speed</th>
      <th>Country</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>upernavik</td>
      <td>72.7868</td>
      <td>-56.1549</td>
      <td>43.03</td>
      <td>83</td>
      <td>71</td>
      <td>14.54</td>
      <td>GL</td>
      <td>1628243435</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chokurdakh</td>
      <td>70.6333</td>
      <td>147.9167</td>
      <td>43.97</td>
      <td>76</td>
      <td>100</td>
      <td>9.26</td>
      <td>RU</td>
      <td>1628243438</td>
    </tr>
    <tr>
      <th>2</th>
      <td>nome</td>
      <td>64.5011</td>
      <td>-165.4064</td>
      <td>51.87</td>
      <td>87</td>
      <td>90</td>
      <td>10.36</td>
      <td>US</td>
      <td>1628243441</td>
    </tr>
    <tr>
      <th>3</th>
      <td>atuona</td>
      <td>-9.8000</td>
      <td>-139.0333</td>
      <td>77.29</td>
      <td>79</td>
      <td>19</td>
      <td>13.98</td>
      <td>PF</td>
      <td>1628243445</td>
    </tr>
    <tr>
      <th>4</th>
      <td>padang</td>
      <td>-0.9492</td>
      <td>100.3543</td>
      <td>87.85</td>
      <td>69</td>
      <td>60</td>
      <td>3.60</td>
      <td>ID</td>
      <td>1628243449</td>
    </tr>
  </tbody>
</table>
</div>

# Inspect the data and remove the cities where the humidity > 100%.
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Max Temp</th>
      <th>Humidity</th>
      <th>Cloudiness</th>
      <th>Wind Speed</th>
      <th>Country</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>

No humidity >100%

# Latitude vs. Temperature Plot

![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_21_0.png?raw=true)

# Latitude vs. Humidity Plot

![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_24_0.png?raw=true)

# Latitude vs. Cloudiness Plot

![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_27_0.png?raw=true)

# Latitude vs. Wind Speed Plot

![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_30_0.png?raw=true)



# Linear Regression
#  Northern Hemisphere - Max Temp vs. Latitude Linear Regression

The r-squared is: -0.626692359392303
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_36_1.png?raw=true)


#  Southern Hemisphere - Max Temp vs. Latitude Linear Regression

The r-squared is: 0.7839579389903588
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_39_1.png?raw=true)


#  Northern Hemisphere - Humidity (%) vs. Latitude Linear Regression

The r-squared is: 0.010344523856748057
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_42_1.png?raw=true)


#  Southern Hemisphere - Humidity (%) vs. Latitude Linear Regression

The r-squared is: -0.01119630670214178
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_45_1.png?raw=true)



#  Northern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

The r-squared is: -0.011519813975742468 
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_48_1.png?raw=true)



#  Southern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

The r-squared is: -0.05766033609555552 
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_51_1.png?raw=true)



#  Northern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

The r-squared is: -0.06462790577943926 
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_54_1.png?raw=true)
    


#  Southern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

The r-squared is: 0.050889201747779444
![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/WeatherPy/output_data/output_57_1.png?raw=true)


## VacationPy

# Store Part I results into DataFrame

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City_ID</th>
      <th>City</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Max Temp</th>
      <th>Humidity</th>
      <th>Cloudiness</th>
      <th>Wind Speed</th>
      <th>Country</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>upernavik</td>
      <td>72.7868</td>
      <td>-56.1549</td>
      <td>43.03</td>
      <td>83</td>
      <td>71</td>
      <td>14.54</td>
      <td>GL</td>
      <td>1628243435</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>chokurdakh</td>
      <td>70.6333</td>
      <td>147.9167</td>
      <td>43.97</td>
      <td>76</td>
      <td>100</td>
      <td>9.26</td>
      <td>RU</td>
      <td>1628243438</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>nome</td>
      <td>64.5011</td>
      <td>-165.4064</td>
      <td>51.87</td>
      <td>87</td>
      <td>90</td>
      <td>10.36</td>
      <td>US</td>
      <td>1628243441</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>atuona</td>
      <td>-9.8000</td>
      <td>-139.0333</td>
      <td>77.29</td>
      <td>79</td>
      <td>19</td>
      <td>13.98</td>
      <td>PF</td>
      <td>1628243445</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>padang</td>
      <td>-0.9492</td>
      <td>100.3543</td>
      <td>87.85</td>
      <td>69</td>
      <td>60</td>
      <td>3.60</td>
      <td>ID</td>
      <td>1628243449</td>
    </tr>
  </tbody>
</table>
</div>


# Create new DataFrame fitting weather criteria


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City_ID</th>
      <th>City</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Max Temp</th>
      <th>Humidity</th>
      <th>Cloudiness</th>
      <th>Wind Speed</th>
      <th>Country</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>cayenne</td>
      <td>4.9333</td>
      <td>-52.3333</td>
      <td>73.44</td>
      <td>91</td>
      <td>0</td>
      <td>1.99</td>
      <td>GF</td>
      <td>1628243525</td>
    </tr>
    <tr>
      <th>240</th>
      <td>240</td>
      <td>namibe</td>
      <td>-15.1961</td>
      <td>12.1522</td>
      <td>76.15</td>
      <td>56</td>
      <td>0</td>
      <td>6.73</td>
      <td>AO</td>
      <td>1628244351</td>
    </tr>
    <tr>
      <th>274</th>
      <td>274</td>
      <td>marondera</td>
      <td>-18.1853</td>
      <td>31.5519</td>
      <td>75.06</td>
      <td>18</td>
      <td>0</td>
      <td>0.56</td>
      <td>ZW</td>
      <td>1628244466</td>
    </tr>
    <tr>
      <th>340</th>
      <td>340</td>
      <td>kasungu</td>
      <td>-13.0333</td>
      <td>33.4833</td>
      <td>79.70</td>
      <td>30</td>
      <td>0</td>
      <td>6.91</td>
      <td>MW</td>
      <td>1628244720</td>
    </tr>
    <tr>
      <th>349</th>
      <td>349</td>
      <td>guerrero negro</td>
      <td>27.9769</td>
      <td>-114.0611</td>
      <td>72.00</td>
      <td>79</td>
      <td>0</td>
      <td>4.97</td>
      <td>MX</td>
      <td>1628244754</td>
    </tr>
    <tr>
      <th>379</th>
      <td>379</td>
      <td>grootfontein</td>
      <td>-19.5667</td>
      <td>18.1167</td>
      <td>75.15</td>
      <td>18</td>
      <td>0</td>
      <td>9.75</td>
      <td>NaN</td>
      <td>1628244855</td>
    </tr>
    <tr>
      <th>417</th>
      <td>417</td>
      <td>mabopane</td>
      <td>-25.4977</td>
      <td>28.1007</td>
      <td>76.21</td>
      <td>21</td>
      <td>0</td>
      <td>5.03</td>
      <td>ZA</td>
      <td>1628245007</td>
    </tr>
    <tr>
      <th>504</th>
      <td>504</td>
      <td>omaruru</td>
      <td>-21.4333</td>
      <td>15.9333</td>
      <td>77.14</td>
      <td>15</td>
      <td>0</td>
      <td>0.78</td>
      <td>NaN</td>
      <td>1628245329</td>
    </tr>
    <tr>
      <th>512</th>
      <td>512</td>
      <td>opuwo</td>
      <td>-18.0607</td>
      <td>13.8400</td>
      <td>79.99</td>
      <td>15</td>
      <td>0</td>
      <td>8.55</td>
      <td>NaN</td>
      <td>1628245356</td>
    </tr>
  </tbody>
</table>
</div>

#Hotel DataFrame

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Country</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Hotel Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>cayenne</td>
      <td>GF</td>
      <td>4.9333</td>
      <td>-52.3333</td>
      <td>Hôtel Le Dronmi</td>
    </tr>
    <tr>
      <th>240</th>
      <td>namibe</td>
      <td>AO</td>
      <td>-15.1961</td>
      <td>12.1522</td>
      <td>Hotel Chik Chik Namibe</td>
    </tr>
    <tr>
      <th>274</th>
      <td>marondera</td>
      <td>ZW</td>
      <td>-18.1853</td>
      <td>31.5519</td>
      <td>HopeFay Conference Centre</td>
    </tr>
    <tr>
      <th>340</th>
      <td>kasungu</td>
      <td>MW</td>
      <td>-13.0333</td>
      <td>33.4833</td>
      <td>Mame Motel</td>
    </tr>
    <tr>
      <th>349</th>
      <td>guerrero negro</td>
      <td>MX</td>
      <td>27.9769</td>
      <td>-114.0611</td>
      <td>Casa Laguna, Bed &amp; Breakfast</td>
    </tr>
    <tr>
      <th>379</th>
      <td>grootfontein</td>
      <td>NaN</td>
      <td>-19.5667</td>
      <td>18.1167</td>
      <td>Meteor Travel Inn</td>
    </tr>
    <tr>
      <th>417</th>
      <td>mabopane</td>
      <td>ZA</td>
      <td>-25.4977</td>
      <td>28.1007</td>
      <td>Wolf Residence</td>
    </tr>
    <tr>
      <th>504</th>
      <td>omaruru</td>
      <td>NaN</td>
      <td>-21.4333</td>
      <td>15.9333</td>
      <td>Kashana, Omaruru, Namibia</td>
    </tr>
    <tr>
      <th>512</th>
      <td>opuwo</td>
      <td>NaN</td>
      <td>-18.0607</td>
      <td>13.8400</td>
      <td>ABBA Guesthouse</td>
    </tr>
  </tbody>
</table>
</div>



# Humidity & Hotel Heatmap

![png](https://github.com/Robert-W2019/PythonAPI-Challenge/blob/main/VacationPy/output_data/Final%20Map%20with%20Humidity%20Heatmap%20and%20%20Hotels.png?raw=true)