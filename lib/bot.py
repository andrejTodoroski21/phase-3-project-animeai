import re
import random
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

class AnmieAI:

    negative_responses = ('no', 'nope', 'nah', 'sorry')

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
        # self.dict = {
        #     'describe_animeai_intent': r'.*\s* AnimeAi',
        #     'answer_why_intent': r'why\sare.*',
        #     'about_anime':r'.*\s* Anime',
            
        # }
        self.keywords1 = ('animeai', 'yourself' ,'who', 'AnimeAI', 'AnimeAi')
        self.keywords2 = ('recommend', 'suggest', 'anime to watch', 'animes to watch')

        

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
                return "Have a good day!"
            
    def chat(self):
        reply = input(random.choice(self.random_quetions)).lower()
        while not self.exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        tokens = word_tokenize(reply)
        print(tokens)
        if any(keyword in tokens for keyword in self.keywords1):
            return self.about() 
        elif any(keyword in tokens for keyword in self.keywords2):
            return self.recommend() 
        else:
            return self.no_match_intent()
    #     for key, value in self.dict.items():
    #         intent = key
    #         regex_pattern = value
    #         found_match = re.match(regex_pattern, reply)
    #         if found_match and intent == 'describe_animeai_intent':
    #             return self.describe_animeai_intent()
    #         elif found_match and intent == 'answer_why_intent':
    #             return self.answer_why_intent()
    #         elif found_match and intent == 'about_anime':
    #             return self.about_anime()
    #     if not found_match:
    #         return self.no_match_intent()
    # def match_reply(self, reply:str):
    #     for key, value in self.dict.items():
    #         intent = key
    #         regex_pattern = value
    #         found_match = re.match(regex_pattern, str(reply))
    #         if found_match:
    #             if intent == 'describe_animeai_intent':
    #                 return self.describe_animeai_intent()
    #             elif intent == 'answer_why_intent':
    #                 return self.answer_why_intent()
    #             elif intent == 'about_anime':
    #                 return self.about_anime()
    #     if not found_match:
    #         return self.no_match_intent()
        
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
    
    def no_match_intent(self):
        responses = self.random_quetions
        return random.choice(responses)
