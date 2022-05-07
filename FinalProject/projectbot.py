#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:23:13 2022

@author: teagannorrgard
"""

# %%

import os
import discord
from dotenv import load_dotenv
import requests
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

client = discord.Client()


def get_temp(city):
    try:
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(
            city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        tempK = int(weather_json_data['main']['temp'])
        tempF = str(round(((tempK - 273.15) * (9 / 5)) + 32, 2)) + " degrees Fahrenheit"
        return (tempF)
    except:
        return ('Please make sure you enter your information and city in the correct format: information, city, state')


def get_wind(city):
    try:
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(
            city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        wind = "wind speed: " + str(weather_json_data['wind']['speed']) + " mph"
        return (wind)
    except:
        return ('Please make sure you enter your information and city in the correct format: information, city, state')


def get_desc(city):
    try:
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(
            city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        desc = weather_json_data['weather'][0]['description']
        return (desc)
    except:
        return ('Please make sure you enter your information and city in the correct format: information, city, state')


def get_humidity(city):
    try:
        coord_url = 'https://api.openweathermap.org/geo/1.0/direct?q=' + str(
            city) + '&limit=1&appid=021e72b2b00f0125fe9357f7e5c6094f'
        coord_response = requests.get(str(coord_url))
        coord_json_data = json.loads(coord_response.text)
        lat = str(coord_json_data[0]["lat"])
        lon = str(coord_json_data[0]["lon"])
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=021e72b2b00f0125fe9357f7e5c6094f'
        weather_response = requests.get(str(weather_url))
        weather_json_data = json.loads(weather_response.text)
        humidity = str(weather_json_data['main']['humidity']) + "%"
        return (humidity)
    except:
        return ('Please make sure you enter your information and city in the correct format: information, city, state')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(
            'Hello! I can find the weather of any U.S. city you would like. Please type what information you are looking for (temperature, wind, description, or humidity) and the city (city, state).')

    if message.content.startswith('temp'):
        citySpace = message.content.split("temperature, ", 1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        temp = get_temp(correct)
        await message.channel.send(temp)

    if message.content.startswith('desc'):
        citySpace = message.content.split("description, ", 1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        desc = get_desc(correct)
        await message.channel.send(desc)

    if message.content.startswith('wind'):
        citySpace = message.content.split("wind, ", 1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        wind = get_wind(correct)
        await message.channel.send(wind)

    if message.content.startswith('humid'):
        citySpace = message.content.split("humidity, ", 1)[1]
        cityComm = citySpace.split(",")
        city = cityComm[0].replace(" ", "%20")
        state = cityComm[1].replace(" ", "")
        correct = city + "," + state
        humid = get_humidity(correct)
        await message.channel.send(humid)

    if message.content.startswith('help'):
        await message.channel.send(
            'Please enter what information you would like about a U.S. city (information, city, state)')


client.run('TOKEN')

