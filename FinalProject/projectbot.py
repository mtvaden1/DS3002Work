#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:23:13 2022

@author: teagannorrgard
"""

#%%
 
import os
import discord
from dotenv import load_dotenv
import requests
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

client = discord.Client()


## function for when user asks for temperature
def get_temp(city):
    try: 
        
        ## takes city and puts into url that grabs coordinates
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        
        ## uses coordinates to make new url that will get weather info
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        
        ## finding temperature in the json data
        tempK = int(weather_json_data['main']['temp'])
        
        ## temp was in Kelvin, this changes it to Fahrenheit
        tempF = str(round(((tempK - 273.15) * (9/5)) + 32, 2)) + " degrees Fahrenheit"
        return(tempF)
    except:
        ## if user has misspelled or entered an invalid city, this will give a new message from the bot instead of breaking
        return('Please make sure you enter your information and city in the correct format: information, city, state')
    
    
def get_wind(city):
    try: 
        
        ## takes city and puts into url that grabs coordinates
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        
        ## uses coordinates to make new url that will get weather info
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        
        ## finding wind speed in json data
        wind = "wind speed: " + str(weather_json_data['wind']['speed']) + " mph"
        return(wind)
    except:
        ## if user has misspelled or entered an invalid city, this will give a new message from the bot instead of breaking
        return('Please make sure you enter your information and city in the correct format: information, city, state')


def get_desc(city):
    try: 
        
        ## takes city and puts into url that grabs coordinates
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        
        ## uses coordinates to make new url that will get weather info
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        
        ## finding weather description in json data
        desc = weather_json_data['weather'][0]['description']
        return(desc)
    except:
        ## if user has misspelled or entered an invalid city, this will give a new message from the bot instead of breaking
        return('Please make sure you enter your information and city in the correct format: information, city, state')
    
    
def get_humidity(city):
    try: 
        
        ## takes city and puts into url that grabs coordinates
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        
        ## uses coordinates to make new url that will get weather info
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        
        ## finding humidity % in json data
        humidity = str(weather_json_data['main']['humidity']) + "%"
        return(humidity)
    except:
        ## if user has misspelled or entered an invalid city, this will give a new message from the bot instead of breaking
        return('Please make sure you enter your information and city in the correct format: information, city, state')
        
        
@client.event
async def on_ready():
    ## lets me know in terminal that the bot is running correctly
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    ## a hello message will be answered with what the bot does and how to phrase a query
    if message.content.startswith('hello'):
        await message.channel.send('Hello! I can find the weather of any U.S. city you would like. Please type what information you are looking for (temperature, wind, description, or humidity) and the city (city, state).')
        
    ## if a user wants temperature
    if message.content.startswith('temp'):
        
        ## takes the whole message after 'temperature, '
        citySpace = message.content.split("temperature, ",1)[1]
        
        ## splits city/state at comma
        cityComm = citySpace.split(",")
        
        ## replaces any spaces in city name with a '%20' which is how a valid url for the API is structured
        city = cityComm[0].replace(" ", "%20")
        
        ## replaces any spaces in state name with nothing, which is how a valid url for the API is structured
        state = cityComm[1].replace(" ", "")
        
        ## adding comma back in (needed for valid url)
        correct = city + "," + state
        
        ## calls temperature function for this city,state
        temp = get_temp(correct)
        
        ## bot answers with what the function returns
        await message.channel.send(temp)
        
    ## same way of getting correctly formatted city,state for API url  
    if message.content.startswith('desc'):
        citySpace = message.content.split("description, ",1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        desc = get_desc(correct)
        await message.channel.send(desc)
     
    ## same way of getting correctly formatted city,state for API url      
    if message.content.startswith('wind'):
        citySpace = message.content.split("wind, ",1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        wind = get_wind(correct)
        await message.channel.send(wind)
    
    ## same way of getting correctly formatted city,state for API url  
    if message.content.startswith('humid'):
        citySpace = message.content.split("humidity, ",1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        humid = get_humidity(correct)
        await message.channel.send(humid)
        
    ## if a user asks for help
    if message.content.startswith('help'):
        ## bot responds with what it can do, and how to correctly format a query
        await message.channel.send('Please enter what information you would like about a U.S. city (information, city, state)')
    
client.run(TOKEN)





