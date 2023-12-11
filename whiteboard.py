# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship

def solution(games): # Take in a list of games ['x:y', 'x:y', etc]
    season_total = 0 # Set the season total to 0
    for game in games: # Loop through each game in the season
        points = game.split(':') # Get the points for each team
        x_score = int(points[0]) # Team X is everything before the colon (converted to integer)
        y_score = int(points[1]) # Team Y is everything after the colon (converted to integer)
        if x_score > y_score: # If x score is greater than y_score
            season_total += 3 # Add 3 points to the season total
        elif x_score == y_score: # If x ties y (aka same amount of goals)
            season_total += 1 # Add 1 point to the season total
    return season_total # Once we have looped through every game, return the season_total


my_cart = {
    'Banana': {
        'price': .55,
        'quantity': 6
    }
}

