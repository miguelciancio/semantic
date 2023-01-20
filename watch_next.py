import spacy

def watch_next(description):    
    #  Most recent movied watched by the user.
    watched_movie = {
    'movie': 'Planet Hulk',
    'description': 'Planet Hulk - Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle\
and lunch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Saakar where he is sold into slavery and trained\
as a gladiator.'
}
    #  Iterate through all of descriptions in order to obtain the most similar
    #  movie based on the most recent watched movie by the user. Add the results
    #  in a list (similarities_list) in order to get the movie with the biggest number
    #  of similatiry.
    similarities_number_list = []
    token_ = nlp(watched_movie["description"])
    for token in description:
        token = nlp(token)
        similarities_number_list.append(token.similarity(token_))

    #  Get the index of the biggest similar number.
    index_next_movie = similarities_number_list.index(max(similarities_number_list))

    #  Iterate through watch_next_movie_list comparing 
    #  to the index of the biggest similar number and 
    #  print out on screen the reccomendation of the 
    #  next movie that the user should watch
    for index, next_movie in enumerate(watch_next_movie_list):
        if index == index_next_movie:
            return f"Next Movie You Should Watch: \n{next_movie['movie']} - {next_movie['description']}\
                    \nPercentage of match: {round(max(similarities_number_list), 4) * 100}%"



    



#  Initialize SpaCy with Advanced Language Model
nlp = spacy.load("en_core_web_md")


#  List variables that will receive data that
#  will be used later
watch_next_movie_list = []
movie_descriptions = []

#  Get all lines from the file movies.txt and
#  store them into a list of dictionaries with
#  each movie data.
with open("movies.txt", "r", encoding="utf-8") as rfile:
    for lines in map(str.strip, rfile):
        if not lines:
            continue
        movie, description = [
            line.strip() for line in lines.split(":")
        ]
        watch_next_movie_list.append(
            {
                "movie": movie,
                "description": description
            }
        )    

#  Get all descriptions from the list.
for data in watch_next_movie_list:
    movie_descriptions.append(data["description"])

#  Get the next option movie for the user watch based on
#  the last movie that he/she/it watched
user_next_movie = watch_next(movie_descriptions)
print(user_next_movie)