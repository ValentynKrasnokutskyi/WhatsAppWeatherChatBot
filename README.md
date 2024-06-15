# WhatsApp Weather Bot

This is a Python script that sends daily weather updates to a list of WhatsApp contacts using the `pywhatkit` library and the OpenWeatherMap API. The bot is designed to run on a schedule, sending weather information for a specified city every day at a designated time.

## Features

- Fetches current weather data for a specified city.
- Sends WhatsApp messages to multiple contacts.
- Uses environment variables to manage sensitive information.
- Schedule messages to be sent daily at a specified time.

## Requirements

- Python 3.6+
- An OpenWeatherMap API key
- `pywhatkit` library
- `requests` library
- `schedule` library
- `python-dotenv` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/whatsapp-weather-bot.git
   cd whatsapp-weather-bot
   
2. Install the required packages:

    ```sh
    pip install -r requirements.txt
   
3. Create a '.env' file in the root directory and add your OpenWeatherMap API key:
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key

   
4. Create a 'contacts.txt' file in the root directory and add the phone numbers of your contacts (one per line) in the format:

   Exemple:  
   
            +1234567890  
            +0987654321

5. Update the 'CITY', 'CONTACTS_FILE', 'TIME_TO_SEND', and other configurations in weather_bot_v1.py as needed.


6. Run the script:
    
    ```sh
    python weather_bot_v1.py
