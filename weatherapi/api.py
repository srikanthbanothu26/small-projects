"""Weather Data Logger
Description: Build an application that collects weather data from a weather API, stores it in a MySQL database, and provides historical weather data analysis.

Key Components of the project are:

1. Use the Requests module to retrieve weather data from a weather API like OpenWeatherMap.
2. Regularly update the MySQL database with the latest weather data.
3. Create features for users to view historical weather patterns or statistics"""

import pymysql
import datetime
import requests

city = "hyderabad" 
url = f"http://api.weatherapi.com/v1/current.json?key=f295a68795214493ab660007231812&q={city}&aqi=no"

api_key="f295a68795214493ab660007231812"

response = requests.get(url)
data = response.json()
conn =pymysql.connect(db="defaultdb",
                     host="mysql-323302ad-banothusrikanth267-d588.a.aivencloud.com",
                     user="avnadmin",
                     password="AVNS_mEQfCEIkupo_GdLjlhc",
                     port=26621)
cursor=conn.cursor()
cursor.execute("""CREATE TABLE if not exists  weather_data2 (
                                                                id INT  PRIMARY KEY auto_increment,
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
                                                                cnd text,
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


sql =f"""INSERT INTO weather_data2(city_name,region,country,lat,lon, temp, pressure, humidity,last_updated,code,cnd, date_time) 
                         VALUES ('{city}','{region}' ,'{country}','{lat}','{lon}' ,'{temperature}','{pressure}','{humidity}','{last_updated}' ,'{code}','{condition}','{datetime1}' )"""
                         
cursor.execute(sql)
conn.commit()
print(cursor.rowcount, "record inserted.")

val=(city,region,country,lat,lon, temperature, pressure, humidity,last_updated,code,condition, datetime1)
print(val)

conn.commit()
conn.close()
