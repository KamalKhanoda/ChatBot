# ChatBot

A simple Python-based personal assistant chatbot that can:

- Greet users and introduce itself
- Tell the current date
- Open popular websites (YouTube, Google, Facebook, Instagram)
- Play the first YouTube video for a given search term
- Open installed applications on your computer
- Search Google for any other queries

## Requirements

- Python 3.x
- [pytube](https://pytube.io/en/latest/) (`pip install pytube`)

## Usage

1. Clone or download this repository.
2. Install the required dependencies:
    ```sh
    pip install pytube
    ```
3. Run the chatbot:
    ```sh
    python chatbot.py
    ```

4. Interact with the chatbot using the terminal. Example commands:
    - `hello`
    - `what is your name`
    - `date`
    - `open youtube`
    - `play python tutorial`
    - `open notepad`
    - Any other query will be searched on Google.

5. To exit, type `bye`, `exit`, or `quit`.

## Features

- **Greeting:** Responds to greetings and introduces itself.
- **Date:** Tells today's date.
- **Open Websites:** Opens YouTube, Google, Facebook, or Instagram in your browser.
- **Play YouTube Videos:** Searches and plays the first YouTube video for your query.
- **Open Applications:** Attempts to open installed applications (Windows only).
- **Fallback Search:** Any other input is searched on Google.

## Notes

- The application uses the default web browser for opening links.
- Application opening (`os.system("start ...")`) works on Windows.
- Make sure you have an active internet connection for web features.
