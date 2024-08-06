# Prompt the user for movie preferences
action = input("Do you like action movies? (yes/no): ").lower() == "yes"
comedy = input("Do you like comedy movies? (yes/no): ").lower() == "yes"
drama = input("Do you like drama movies? (yes/no): ").lower() == "yes"

# Combine booleans using logical operators
if action and comedy and not drama:
    genre = "Action-Comedy"
elif action and drama and not comedy:
    genre = "Action-Drama"
elif comedy and drama and not action:
    genre = "Comedy-Drama"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif drama:
    genre = "Drama"
else:
    genre = "Unknown"

# Recommend movies based on the genre using conditional statements
if genre == "Action-Comedy":
    print("Recommended movies: 'The Gentlemen', 'Deadpool', 'Beverly Hills Cop'")
elif genre == "Action-Drama":
    print("Recommended movies: 'Gen V', 'Kingdom of the Planet of the Apes', 'House of the Dragon'")
elif genre == "Comedy-Drama":
    print("Recommended movies: 'IF', 'Hit Man', 'Juno'")
elif genre == "Action":
    print("Recommended movies: 'Die Hard', 'The Matrix', 'Mission: Impossible'")
elif genre == "Comedy":
    print("Recommended movies: 'The Hangover', 'Superbad', 'Bridesmaids'")
elif genre == "Drama":
    print("Recommended movies: 'The Shawshank Redemption', 'Forrest Gump', 'The Green Mile'")
else:
    print("Sorry, we couldn't determine your movie preferences.")