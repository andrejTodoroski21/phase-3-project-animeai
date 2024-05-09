import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from google.oauth2 import service_account
from google.cloud import dialogflow_v2beta1 as dialogflow
import uuid
from lib.models import Recommendations
from lib.models import Anime
from lib.models import Commands
from lib.models import About_keywords

class AnmieAI():
    
    exit_commands = ('exit', 'quit', 'pause', 'goodbye', 'bye', 'see you later', 'see you', 'see ya later', 'see ya', 'later')

    descriptions = ('fantastic', 'great', 'fun', 'just wow')

    def __init__(self):
        self.keywords1 = ('how are you', 'how is it going', 'what\'s up', 'su\'p')
        self.keywords2 = ('ascii art', 'anime art', 'show me ascii art', 'art')

    def greet(self):
        #This method gets trigered when we run the bot, it displays a list of what the bot can do
        print('''
        Here are some commands you can ask AnimeAi
        1. Ask for "art"
        2. Ask for recommondations ("recommend"/"suggest")
        3. Ask AnimeAi about itself ("who are you"/"yourself")
        4. Ask AnimeAi how it is doing ("how are you")
        5. Lastly you can chat with AnimeAi about anime if anime is in db
        ''')
        # Get the user's name
        self.user_input = input('AnimeAi: What is your name? \n')
        # Get what anime the user is watching now
        now_watching = input(
            f"AnimeAi: Hey! {self.user_input}. I am AnimeAI. What anime are you watching? \n"
        )
        # Here we used nltk to tokenize the user_input
        tokens = sent_tokenize(now_watching)
        # Convert the tokens into lower case
        tokens = [token.lower() for token in tokens]
        # Get all the animes from our database and store them in a list
        Anime.read_all()
        # Get all the ascii art for each anime from the database and store them in a list.
        Anime.read_all_art()
        # Make a dictionary out of the above two lists where keys are the first list elements and values are the second list elements.
        anime_art = { an:ar for (an,ar) in zip(Anime.all_animes, Anime.all_art)}
        # if the anime the user is watching now in our database do the following else return self.chat()
        if any(keyword in tokens for keyword in [anime for anime in Anime.all_animes]):
            print(f"{(now_watching).upper()} is a {random.choice(self.descriptions)} anime to watch")
            for key, value in anime_art.items():
                if now_watching.lower() == key:
                    print(f"AnimeAi: here is some art for {now_watching}: {value}")
            return self.chat()
        return self.chat()
    
    # If the user types "exit" or any other exit command from the exit_commands list, it wishes the user a good day and exits, else it handles user_input using self.match_reply method
    def exit(self, reply):
        Commands.read_all()
        if reply in Commands.all_commands:
            print ("AnimeAi: Have a good day!")
            return True
        else:
            return self.match_reply(reply)

    # This method takes user input and checks first if it's an exit command, else it handles the input using self.match_reply method
    def chat(self):
        while True:
            reply = input('You: ').lower()
            if self.exit(reply):
                return
            else:
                return self.match_reply(reply)

    
    def match_reply(self, reply):
        # If reply matches one of our predefined exit commands exit the app,
        if reply in Commands.all_commands:
            return self.exit(reply)
        # else handle the input using the following conditions
        else:
            # Use nltk to tokenize the input into words
            tokens = word_tokenize(reply)
            # Tokenize the input into sentences, and then lowercase the sentences
            sentences = []
            sentences = sent_tokenize(reply)
            sentences = [ sentence.lower() for sentence in sentences]
            # Get all the about keywords from database and store then in a list
            About_keywords.retreive_about_keywords()
            # Get all the recommen keywords from database and store them in a list
            Recommendations.retreive_keywords()
            # If the user input matches one of the about keywords,return self.about method
            if any(keyword in sentences for keyword in About_keywords.all_about_keywords):
                return self.about()
            # If the user input matches one of the recommend keywords,return self.recommend method
            elif any(keyword in tokens for keyword in Recommendations.all_keywords):
                return self.recommend()
            # If the user input matches one of the keywords in self.keywords1,return self.how_is_AI method
            elif any(keyword in sentences for keyword in self.keywords1):
                return self.how_is_AI()
             # If the user input matches one of the keywords in self.keywords2,return self.ascii_art method
            elif any(keyword in sentences for keyword in self.keywords2):
                return self.ascii_art(reply)
            # else send the user input to our dialogflow project for further processing
            else:
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
        # Get all the responses for about animeai from database and print a random response. then take a new input and return self.match_reply method with the new input
        About_keywords.retreive_recommondations()
        print(random.choice(About_keywords.all_responses))
        user_input = input('You: ')
        return self.match_reply(user_input)
    
    def recommend(self):
         # Get all the responses for anime recommendations from database and print a random response. then take a new input and return self.match_reply method with the new input
        Recommendations.retreive_recommondations()
        print(random.choice(Recommendations.all_recommendations))
        user_input = input('You: ')
        return self.match_reply(user_input)
    
    def how_is_AI(self):
         # Print a random response from the tuple below. then take a new input and return self.match_reply method with the new input
        responses = ('AnimeAi: I\'m a bot, I don\'t have feelings, but I\'m hoping you\'re doing well.', 'AnimeAi: I don\'t feel anything, I\'m just a bot!')
        print(random.choice(responses))
        user_input = input('You: ')
        return self.match_reply(user_input)

    def ascii_art(self, reply):
        # Ask the user which anime they would like to see ascii art for
        user_input = input('AnimeAi: Which anime art you want to see: ')
        # Get all the animes from our database and store them in a list
        Anime.read_all()
        # Get all the ascii art for each anime from the database and store them in a list.
        Anime.read_all_art()
        # Make a dictionary out of the above two lists where keys are the first list elements and values are the second list elements.
        anime_art = { an:ar for (an,ar) in zip(Anime.all_animes, Anime.all_art)}
        # if the anime the user typed is in the database display art fot it and return self.match_reply to keep the conversaton going,
        if reply in self.keywords6:
            for key, value in anime_art.items():
                if user_input.lower() == key.lower():
                    print(f"AnimeAi: here is some art for {user_input}: {value}")
                    return self.match_reply('exit art method')
                    break
            # esle if the anime is not in the database, tell the user we don't have that anime and return self.match_reply to keep the conversaton going
            print(f'AnimeAi: Sorry, we don\'t have {user_input} in our database!')
            return self.match_reply('exit art method')

