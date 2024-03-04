from tkinter import *
import requests
from datetime import datetime
root =Tk()
root.geometry("400x400") 
root.title("Weather App ")
 
city_value = StringVar()
 
 
def time_format_for_location(x):
    local_time = datetime.utcfromtimestamp(x)
    return local_time.time()
 
def showWeather():
    api_key = "55960a113677437f7ef474e801212793"  
    city_name=city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()

    weather_data.delete("1.0", "end")   #to clear the text field for every new output
 
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched

    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
#-----------Storing the fetched values of weather of a city
#converting default kelvin value to Celcius
 
        temp = int(weather_info['main']['temp'] - kelvin)                                     
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
#assigning Values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
        
 #to insert or send value in our Text Field to display output
    weather_data.insert(INSERT, weather)  
 
  
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
 
city_entry = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
  
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
weather_data = Text(root, width=46, height=10)
weather_data.pack()
 
root.mainloop()