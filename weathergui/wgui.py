import requests
from tkinter import *
import datetime

window=Tk()
window.geometry("300x300")
window.configure(background = "gray")
window.title("Weather App")

city_text= StringVar()

def get_weather():
    api_key = "f295a68795214493ab660007231812" 
    city_name=city_text.get()
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    response = requests.get(weather_url)
    weather_info = response.json()
    weather_data.delete("1.0", "end")
    if response.status_code==200:
        region=weather_info['location']['region']
        country=weather_info['location']['country']
        lat=weather_info['location']['lat']
        lon=weather_info['location']['lon']

        temperature = weather_info['current']['temp_c']
        pressure = weather_info['current']['pressure_in']
        humidity = weather_info['current']['humidity']
        last_updated=weather_info['current']['last_updated']
        condition=weather_info['current']['condition']['text']
            
        now = datetime.datetime.now()
        datetime1 = now.strftime("%Y-%m-%d %H:%M:%S")
       
        weather = f"\nWeather of: {city_name},\nregion: {region},\ncountry={country},\nlat={lat},\nlon={lon},\nTemperature (Celsius): {temperature},\nPressure: {pressure},\nHumidity: {humidity},\nCloud: {condition},\nlast_updated: {last_updated},\ndate-time={datetime1}"
    else:
        weather = f"\n\tWeather for '{city_name}'\nnot found!,\n\tKindly Enter a valid\nCity Name !!"
        
    weather_data.insert(INSERT, weather)
    
frame1 = Frame(window, background="white", borderwidth=2)
frame1.pack()

    
city_head= Label(frame1, text = 'Weather report', font = ('Consolas',25)).pack(padx=40,pady=10)
 
city= Label(window, text = 'Enter City Name', font = 'consolas').pack(pady=10)
 
city_entry = Entry(window, textvariable = city_text,  width = 24, font='Consolas',borderwidth=5).pack()
  
Button(window, command = get_weather, text = "Check Weather", font="Consolas", bg='lightblue', fg='black',borderwidth=4, activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
  
current_weather = Label(window, text = "current Weather is:", font = 'Consolas').pack(padx=15,pady=10)
 
weather_data= Text(window, width=30, height=13)
weather_data.pack()
 
mainloop()





