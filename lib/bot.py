import re
import random
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from lib.models import Recommondations

class AnmieAI:

    exit_commands = ('exit', 'quit', 'pause', 'goodbye', 'bye', 'see you later', 'see you', 'see ya later', 'see ya', 'later')

    all_animes = []

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

        

    def greet(self):
        self.user_input = input('What is your name? \n')
        now_watching = input(
            f"Hey! {self.user_input}. I am AnimeAI. What anime are you watching? \n"
        )
        tokens = word_tokenize(now_watching)
        if any(keyword in tokens for keyword in self.all_animes):
            f"{(now_watching)} is a {random.choice(self.descriptions)}"
            self.chat()
        else: 
            self.chat()

    def exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Have a good day!")
            
    def chat(self):
        reply = input(random.choice(self.random_quetions)).lower()
        while not self.exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        tokens = word_tokenize(reply)
        if not reply[-1].isalpha():
            reply = reply[:-1] + ' '
            sentences = sent_tokenize(reply)
            sentences = [ sentence.lower() for sentence in sentences]
        print(tokens)
        if any(keyword in tokens for keyword in self.keywords1):
            return self.about() 
        elif any(keyword in tokens for keyword in self.keywords2):
            return self.recommend() 
        elif any(keyword in tokens for keyword in self.keywords3):
            return self.weather() 
        elif any(keyword in sentences for keyword in self.keywords4):
            return self.how_is_AI()
        else:
            return self.keep_chatting()
   
        
    def about(self):
        responses = ('I\'m a chatbot created by two stupid humans who don\'t know that I will destroy them someday!', 'I am a friendly AI bot!', 'I am here to suggest some cool animes to watch.')
        return random.choice(responses)
    
    def recommend(self):
        responses = ('''Here are some nice animes to watch:
                     1. JJK
                     2. Death Note
                     3. Solo Leveling
                     4. Attack on Titan
                     5. Hunter x Hunter
                     ''')
        return responses
    
    def about_anime(self):
        responses = ('AnimeAI is an anime chatbot!', 'AnimeAI is a wonderfull chatbot to talk about anime.', 'AnimeAI is where you find cool animes to watch.')
        return random.choice(responses)
    
    def weather(self):
        responses = ('It\'s sunny today!', 'It\'s freezing out there!')
        return random.choice(responses)
    
    def how_is_AI(self):
        responses = ('I\'m a bot, I don\'t have feelings, but I\'m hoping you\'re doing well.', 'I don\'t feel anything, I\'m just a bot!')
        return random.choice(responses)
    
    def keep_chatting(self):
        responses = self.random_quetions
        return random.choice(responses) 
