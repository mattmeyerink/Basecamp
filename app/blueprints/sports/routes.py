"""Routes for sports scores blueprint."""
import flask
from datetime import date
import requests
from . import sports_bp
from config import Config
from pprint import pprint


@sports_bp.route("/")
def show_sportsfeed():
    """Routing for page to display all of the scores."""
    # Determine the current date
    today = date.today()

    # Make API call for todays games from ESPN API
    response = requests.get(f"https://site.api.espn.com/apis/site/v2" +
                            f"/sports/basketball/mens-college-basketball/" +
                            f"scoreboard")
    game_data = response.json()["events"]

    # Process sportradar data
    games = []
    for game in game_data:
        current_game = {}
        
        game_data = game["competitions"]
        home_team = game_data[0]["competitors"][0]
        away_team = game_data[0]["competitors"][1]

        # Check if the game contains a team that is currently ranked in top 25
        if not (home_team["curatedRank"]["current"] <= 25 or 
                away_team["curatedRank"]["current"] <= 25):
            continue

        # Gather the time
        time = game["status"]["type"]["shortDetail"]
        if "-" in time:
            i = time.index("-") + 1
            time = time[i:-4]

        current_game["time"] = time

        # Gather the home team data
        home_team_data = {}
        home_team_data["rank"] = home_team["curatedRank"]["current"]
        home_team_data["record"] = home_team["records"][0]["summary"]
        home_team_data["score"] = home_team["score"]
        home_team_data["logo"] = home_team["team"]["logo"]
        home_team_data["short_name"] = home_team["team"]["shortDisplayName"]
        home_team_data["long_name"] = home_team["team"]["displayName"]

        # Add home team data to current_game
        current_game["home_team"] = home_team_data

        # Gather the away team data
        away_team_data = {}
        away_team_data["rank"] = away_team["curatedRank"]["current"]
        away_team_data["record"] = away_team["records"][0]["summary"]
        away_team_data["score"] = away_team["score"]
        away_team_data["logo"] = away_team["team"]["logo"]
        away_team_data["short_name"] = away_team["team"]["shortDisplayName"]
        away_team_data["long_name"] = away_team["team"]["displayName"]

        # Add the away team data to current_game
        current_game["away_team"] = away_team_data

        # Append current_game to games
        games.append(current_game)
        
    scores = None
    context = {
        "games": games
    }
    return flask.render_template("sports.html", **context)