# AnimeAi Chatbot

# Overview
 -This project is an anime chatbot using NLTK (Natural Language Toolkit) for tokenization and Dialogflow from Google Cloud for natural language processing and understanding.

# Features
- Anime Recommendations: The chatbot can recommend a list of animes to watch using the command word "recommend"
- Tokenization: NLTK is used for tokenizing user input to process natural language queries.
- Dialogflow: Dialogflow provides natural language understanding and conversation management capabilities, with added coversational flavor to give it the personality of the creators
- Anime Art: Using the command word "art" or "ascii art" ect. the chat bot will follow up with a question asking you which anime you want to see art for, and if you respond with an anime in our database you will see the art.

# Prerequisites
- Before running the chatbot, make sure you have the following installed and set up:
- NLTK library (pip install nltk)
- Dialogflow account and API credentials

# Setup
- Clone this repository to your local machine.
- Install the required Python dependencies by running pip install -r requirements.txt.
- Set up your Dialogflow agent and obtain the necessary credentials (API key or service account key).
- Replace the placeholder API credentials in the code with your actual credentials.
- Run the chatbot script using python bot.py

# Usage
- Start the chatbot application.
- Enter your name.
- Talk with the chatbot by typing animes or converse with it.
- The chatbot will provide anime recommendations and respond to your queries based on the configured Dialogflow agent.
