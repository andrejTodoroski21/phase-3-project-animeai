import re
import os
import sys
import random
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from google.oauth2 import service_account
from google.cloud import dialogflow_v2beta1 as dialogflow
import uuid
from lib.models import Recommendations
from lib.models import Anime
from lib.models import Questions
from lib.models import Commands
from lib.models import About_keywords

class AnmieAI:
    
    asked_questions = []

    exit_commands = ('exit', 'quit', 'pause', 'goodbye', 'bye', 'see you later', 'see you', 'see ya later', 'see ya', 'later')


    random_quetions = (
        'Why are you here?',
        'What is your favorite anime?',
        'Do you like anime?',
        'Why do like anime?',
        'How many animes have you watched so far?'
    )

    descriptions = ('fantastic', 'great', 'fun', 'just wow')

    def __init__(self):
        self.keywords1 = ('animeai', 'yourself' ,'who', 'AnimeAI', 'AnimeAi')
        self.keywords2 = ('recommend', 'suggest', 'anime to watch', 'animes to watch')
        self.keywords3 = ('weather', 'weather')
        self.keywords4 = ('how are you', 'how is it going', 'what\'s up', 'su\'p')
        self.keywords5 = ('questions', 'random')
        self.keywords6 = ('ascii art', 'anime art', 'show me ascii art', 'art')

        

    def greet(self):
        print('''
        Here are some commands you can ask AnimeAi
        1. Ask for "art"
        2. Ask for recommondations ("recommend"/"suggest")
        3. Ask AnimeAi about itself ("who are you"/"yourself")
        4. Ask AnimeAi how it is doing ("how are you")
        5. Lastly you can chat with AnimeAi about anime if anime is in db
        ''')
        self.user_input = input('What is your name? \n')
        now_watching = input(
            f"Hey! {self.user_input}. I am AnimeAI. What anime are you watching? \n"
        )
        tokens = sent_tokenize(now_watching)
        tokens = [token.lower() for token in tokens]
        Anime.read_all()
        Anime.read_all_art()
        anime_art = { an:ar for (an,ar) in zip(Anime.all_animes, Anime.all_art)}
        if any(keyword in tokens for keyword in [anime.lower() for anime in Anime.all_animes]):
            print(f"{(now_watching)} is a {random.choice(self.descriptions)} anime to watch")
            for key, value in anime_art.items():
                if now_watching == key:
                    print(f"here is some are for {now_watching}: {value}")
            return self.chat()
        return self.chat()
    
        # else: 
        #     return self.chat()

    def exit(self, reply):
        Commands.read_all()
        if reply in Commands.all_commands:
            print ("Have a good day!")
            return True
        else:
            return self.match_reply(reply)

    def chat(self):
        while True:
            reply = input('You: ').lower()
            if self.exit(reply):
                return
            else:
                return self.match_reply(reply)

    

    def match_reply(self, reply):
        if reply in Commands.all_commands:
            return self.exit(reply)
        else:
            tokens = word_tokenize(reply)
            sentences = []
            sentences = sent_tokenize(reply)
            sentences = [ sentence.lower() for sentence in sentences]
            About_keywords.retreive_about_keywords()
            Recommendations.retreive_keywords()
            if any(keyword in tokens for keyword in About_keywords.all_about_keywords):
                return self.about()
            
            elif any(keyword in tokens for keyword in Recommendations.all_keywords):
                return self.recommend()
            
            elif any(keyword in sentences for keyword in self.keywords4):
                return self.how_is_AI()
            
            elif any(keyword in sentences for keyword in self.keywords6):
                return self.ascii_art(reply)
            
            else:
                # Load service account key
                # /home/jj/Development/code/phase-3/senstive-files/rich-world-329001-e02b32691e8a.json
                # ''/Users/andrejtodoroski/Development/code/phase-3/sensitive-files/rich-world-329001-e02b32691e8a.json
                credentials = service_account.Credentials.from_service_account_file('/Users/andrejtodoroski/Development/code/phase-3/sensitive-files/rich-world-329001-e02b32691e8a.json') 

                # Create a Dialogflow client
                client = dialogflow.SessionsClient(credentials=credentials)

                # Define project ID and session ID
                project_id = 'rich-world-329001'
                session_id = str(uuid.uuid4())

                # Create session path
                session_path = client.session_path(project_id, session_id)

                # User query
                query = reply

                # Define query input
                query_input = {
                    'text': { 
                        'text': query,
                        'language_code': 'en-US'
                    }
                }

                # Send query to Dialogflow
                response = client.detect_intent(
                    session=session_path,
                    query_input=query_input
                )

                # Extract response from Dialogflow
                response_text = response.query_result.fulfillment_text

                # Print response
                print('AnimeAi:', response_text)
                new_input = input('You: ')
                return self.match_reply(new_input)
   
        
    def about(self):
        About_keywords.retreive_recommondations()
        # print(About_keywords.all_responses)
        print(random.choice(About_keywords.all_responses))
        user_input = input('You: ')
        return self.match_reply(user_input)
        # this is a comment
    
    def recommend(self):
        Recommendations.retreive_recommondations()
        print(random.choice(Recommendations.all_recommendations))
        user_input = input('You: ')
        return self.match_reply(user_input)
    
    def about_anime(self):
        # responses = ('AnimeAI is an anime chatbot!', 'AnimeAI is a wonderfull chatbot to talk about anime.', 'AnimeAI is where you find cool animes to watch.')
        Anime.read_all()
        return random.choice(Anime.all_animes)
    
    def how_is_AI(self):
        responses = ('I\'m a bot, I don\'t have feelings, but I\'m hoping you\'re doing well.', 'I don\'t feel anything, I\'m just a bot!')
        print(random.choice(responses))
        user_input = input('You: ')
        return self.match_reply(user_input)

    def ascii_art(self, reply):
        user_input = input('Which anime art you want to see: ')
        Anime.read_all()
        Anime.read_all_art()
        anime_art = { an:ar for (an,ar) in zip(Anime.all_animes, Anime.all_art)}
        # print(anime_art)
        if reply in self.keywords6:
            for key, value in anime_art.items():
                if user_input == key:
                    print(f"here is some are for {user_input}: {value}")
                    return self.match_reply('exit art method')
                    break
        else:
            print(f'Sorry, we don\'t have {user_input} in our database!')
            return self.match_reply('exit art method')

