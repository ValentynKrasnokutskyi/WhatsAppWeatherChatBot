# WhatsApp Weather Bot

This project is a Python script that sends daily weather updates via WhatsApp messages. The script uses the OpenWeatherMap API to fetch weather data and the `pywhatkit` library to send messages through WhatsApp. Contacts for sending messages are read from a file, and the bot can send messages to both individual contacts and groups.

## Features

- Fetches daily weather updates for a specified city.
- Sends weather updates to individual WhatsApp contacts.
- Sends weather updates to WhatsApp groups.
- Uses environment variables to store sensitive information.

## Requirements

- Python 3.7+
- An OpenWeatherMap API key
- WhatsApp Web logged in on your default browser

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ValentynKrasnokutskyi/WhatsAppWeatherChatBot.git
    cd WhatsAppWeatherChatBot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your OpenWeatherMap API key:
    ```env
    OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
    ```

5. Create a `contacts.txt` file and add the phone numbers of the contacts you want to send messages to:
    ```
    +1234567890
    +0987654321
    ```

## Usage

1. Run the script:
    ```sh
    python weather_bot_v1.py
    ```

2. The bot will read the contacts from `contacts.txt` and send the weather update at the scheduled time.

## Configuration

- **CITY**: Change the city for which you want to get the weather update in the `weather_bot_v1.py` file.
- **TIME_TO_SEND**: Set the time at which the bot should send the weather update in the `weather_bot_v1.py` file.

## Notes

- Make sure WhatsApp Web is open and you are logged in to send messages.
- The script uses the `pywhatkit.sendwhatmsg_instantly` function to send messages immediately. Adjust the sleep time if you experience any issues with message delivery.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
