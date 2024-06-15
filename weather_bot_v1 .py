import os
import pywhatkit as kit
import requests
import schedule
import time

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
CITY = 'Boston'
CONTACTS_FILE = 'contacts.txt'
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
TIME_TO_SEND = "13:00"


def get_weather(api_key, city):
    # Get weather data from OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return "Failed to get weather data."


def send_whatsapp_message(phone_number, message):
    try:
        # Send a WhatsApp message instantly
        kit.sendwhatmsg_instantly(phone_number, message)
        time.sleep(10)  # Delay to ensure the message is sent
        print(f"Message sent to {phone_number} successfully")
    except Exception as e:
        print(f"An error occurred when sending to {phone_number}: {e}")


def send_messages_to_contacts():
    # Read contacts from the file
    with open(CONTACTS_FILE, 'r') as file:
        contacts = file.readlines()

    # Get the weather message
    weather_message = get_weather(API_KEY, CITY)
    for contact in contacts:
        contact = contact.strip()
        if contact:  # Check if the line is not empty
            send_whatsapp_message(contact, weather_message)


def job():
    # Job to send messages to all contacts
    send_messages_to_contacts()


# Schedule the job to run every day at the specified time
schedule.every().day.at(TIME_TO_SEND).do(job)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)
