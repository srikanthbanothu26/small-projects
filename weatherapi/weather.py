import sqlite3
import datetime
import requests

city = "vijayawada" 
url = f"http://api.weatherapi.com/v1/current.json?key=f295a68795214493ab660007231812&q={city}&aqi=no"
api_key="f295a68795214493ab660007231812" 
conn =sqlite3.connect("weather.db")
cursor=conn.cursor()
cursor=conn.cursor()
response = requests.get(url)
data = response.json()
 

print(data)
print("-------data printed is over------")

cursor.execute("""CREATE TABLE if not exists  weather_data1 (
                                                                id INTEGER  PRIMARY KEY autoincrement,
                                                                city_name VARCHAR(255),
                                                                region   text ,
                                                                country  text,
                                                                lat float,
                                                                lon  float,
                                                                temp  float,
                                                                pressure float,
                                                                humidity INT,
                                                                last_updated  datetime,
                                                                code  int,
                                                                condition text,
                                                                date_time DATETIME )""")



region=data['location']['region']
country=data['location']['country']
lat=data['location']['lat']
lon=data['location']['lon']


temperature = data['current']['temp_c']
pressure = data['current']['pressure_in']
humidity = data['current']['humidity']
last_updated=data['current']['last_updated']

code=data['current']['condition']['code']
condition=data['current']['condition']['text']

now = datetime.datetime.now()
datetime1 = now.strftime("%Y-%m-%d %H:%M:%S")


sql =f"""INSERT INTO weather_data1(city_name,region,country,lat,lon, temp, pressure, humidity,last_updated,code,condition, date_time) 
                         VALUES ('{city}','{region}' ,'{country}','{lat}','{lon}' ,'{temperature}','{pressure}','{humidity}','{last_updated}' ,'{code}','{condition}','{datetime1}' )"""

cursor.execute(sql)
conn.commit()
print(cursor.rowcount, "record inserted.")

val=(city,region,country,lat,lon, temperature, pressure, humidity,last_updated,code,condition, datetime1)
print(val)

conn.commit()
conn.close()
