name = input("Hi! Nice to meet you, what's your name?: ")

def main():
    # give the user a message about the purpose of our program
    print()
    print(f"Alright {name}, follow the instructions below.")
    print("🎬 Welcome to the Cine Suggestion!")
    print("I'll ask you a few questions to recommend something you'll love. 🍿")

main()

# create our movie database using dictionaries and lists
movies = [
    {
        "title": "Inception",
        "genre": "Science fiction",
        "actor": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "mood": "Mind-blowing"
    },
    {
        "title": "Interstellar",
        "genre": "Science fiction",
        "actor": ["Matthew McConaughey", "Anne Hathaway", "Matt Damon"],
        "mood": "Emotional",
    },
    {
        "title": "La La Land",
        "genre": ["Romantic", "Drama"],
        "actor": ["Emma Stone", "Ryan Gosling"],
        "mood": "Musical",
    },
    {
        "title": "Eternal Sunshine",
        "genre": ["Drama", "Romantic"],
        "actor": ["Jim Carrey", "Mark Ruffalo", "Kate Winslet"],
        "mood": "Memories",
    },
    {
        "title": "Super Cool",
        "genre": "Comedy",
        "actor": ["Bradley Cooper", "Zach Galifianakis", "Ed Helms", "Ken Jeong"],
        "mood": "",
    },
    {
        "title": "The Hangover",
        "genre": "Comedy",
        "actor": ["Bradley Cooper", "Zach Galifianakis", "Ed Helms", "Ken Jeong"],
        "mood": "Dysfunctional Friendship",
    },
    {
        "title": "Black Swan",
        "genre": "Psychological Thriller",
        "actor": ["Natalie Portman", "Mila Kunis"],
        "mood": "Obsession"
    },
    {
        "title": "Shutter Island",
        "genre": "Psychological Thriller",
        "actor": ["Leonardo DiCaprio", "Mark Ruffalo"],
        "mood": "Twisted Reality"
    },
    {
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "actor": ["Tom Hardy", "Charlize Theron"],
        "mood": "High-Octane"
    },
    {
        "title": "John Wick",
        "genre": "Action",
        "actor": ["Keanu Reeves"],
        "mood": "Revenge"
    },
    {
        "title": "Coco",
        "genre": "Animation",
        "actor": ["Anthony Gonzalez", "Gael García Bernal"],
        "mood": "Heartwarming"
    },
    {
        "title": "Spider-Man: Into the Spider-Verse",
        "genre": "Animation",
        "actor": ["Shameik Moore", "Jake Johnson"],
        "mood": "Energetic"
    },
    {
        "title": "The Godfather",
        "genre": "Crime",
        "actor": ["Marlon Brando", "Al Pacino"],
        "mood": "Power and Loyalty"
    },
    {
        "title": "Goodfellas",
        "genre": "Crime",
        "actor": ["Robert De Niro", "Ray Liotta"],
        "mood": "Gritty Realism"
    },
    {
        "title": "Gone Girl",
        "genre": "Thriller",
        "actor": ["Ben Affleck", "Rosamund Pike"],
        "mood": "Dark Secrets"
    },
    {
        "title": "Prisoners",
        "genre": "Thriller",
        "actor": ["Hugh Jackman", "Jake Gyllenhaal"],
        "mood": "Tense and Mysterious"
    },
    {
        "title": "Creed",
        "genre": "Sports Drama",
        "actor": ["Michael B. Jordan", "Sylvester Stallone"],
        "mood": "Motivational"
    },
    {
        "title": "The Blind Side",
        "genre": "Sports/Drama",
        "actor": ["Sandra Bullock", "Quinton Aaron"],
        "mood": "Inspiring"
    },
    {
        "title": "Bohemian Rhapsody",
        "genre": "Biography/Music",
        "actor": ["Rami Malek"],
        "mood": "Musical Journey"
    },
    {
        "title": "Elvis",
        "genre": "Biography/Music",
        "actor": ["Austin Butler", "Tom Hanks"],
        "mood": "Legendary Rise"
    },
]

genre_input = input("What genre would you like to watch? (e.g., Action, Animation, Thriller, etc.): ").lower()
mood_input = input("What mood are you in? (e.g., Revenge, Heartwarming, Obsession, etc.): ").lower()
actor_input = input("Is there any actor or actress you'd like to see? (Just type one or leave blank): ").lower()

recommendations = []

for movie in movies:
    # genre can be a list or a string, convert to string to search
    genre_str = movie["genre"]
    if isinstance(genre_str, list):
        genre_str = " ".join(genre_str).lower()
    else:
        genre_str = genre_str.lower()

    # join actors for searching in string
    actors_str = " ".join(movie["actor"]).lower()

    if (
        (genre_input and genre_input in genre_str) or
        (mood_input and mood_input in movie["mood"].lower()) or
        (actor_input and actor_input in actors_str)
    ):
        if movie not in recommendations:  # avoid duplicates
            recommendations.append(movie)

if recommendations:
    print("\n🎥 Wow, you're a movie expert! Here are some recommendations:\n")
    for r in recommendations:
        print("- " + r["title"])
else:
    print("\n😕 Sorry, we couldn't find any matches for your preferences.")
