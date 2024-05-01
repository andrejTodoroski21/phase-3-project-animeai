import re
import random

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
        self.dict = {
            'describe_animeai_intent': r'.*\s* AnimeAi',
            'answer_why_intent': r'why\sare.*',
            'about_anime':r'.*\s* Anime',
            
        }

    def greet(self):
        self.user_input = input('What is your name?\n')
        now_watching = input(
            f"Hey! {self.user_input}. I am AnimeAI. What anime are you watching?\n"
        )
        if now_watching in self.all_animes:
            return f"{(now_watching)} is a {random.choice(self.descriptions)}"
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
        for key, value in self.dict.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_animeai_intent':
                return self.describe_animeai_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_anime':
                return self.about_anime()
        if not found_match:
            return self.no_match_intent()
        
    def describe_animeai_intent(self):
        responses = ('I\'m a chatbot created by two stupid humans who don\'t that I will destroy them someday!', 'I am a friendly AI bot!', 'I am here to suggest some cool animes to watch.')
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = ('I\'m here to collect data about your favorite animes and suggest new ones for you to watch!', 'I love drinking coffee while watching anime :)')
        return random.choice(responses)
    
    def about_anime(self):
        responses = ('AnimeAI is an anime chatbot!', 'AnimeAI is a wonderfull chatbot to talk about anime.', 'AnimeAI is where you find cool animes to watch.')
        return random.choice(responses)
    
    def no_match_intent(self):
        responses = ('Please tell me more.\n', 'Intersting. How would you briefly describe it?')
        return random.choice(responses)
