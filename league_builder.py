import csv


def open_file(filename):
    '''
    Opens and reads csv using csv.DictReader() builtin
    :param filename: relative path of filename
    :return: List of Dicts
    '''
    with open(filename, encoding='utf8') as fin:
        data = [row for row in csv.DictReader(fin)]
        return data


def split_players(players):
    '''
    Iterates over list of players and splitting them by experienced or not
    :param players: List of players
    :return: list of new_players and list of experienced_players
    '''
    new_players = [row for row in players if row['Soccer Experience'] == 'NO']
    experienced_players = [row for row in players if row['Soccer Experience'] == 'YES']
    return new_players, experienced_players


def assemble_teams(new_players, experienced_players):
    """
    Create equally manned teams
    :param new_players: list of new players
    :param experienced_players: list of experienced players
    :return: teams: Dict()
    """
    teams = {
        'Sharks': [],
        'Dragons': [],
        'Raptors': []
    }
    # add new players to teams
    teams['Sharks'].extend(new_players[:3])
    teams['Dragons'].extend(new_players[3:6])
    teams['Raptors'].extend(new_players[6:])

    # add experienced players to teams
    teams['Sharks'].extend(experienced_players[:3])
    teams['Dragons'].extend(experienced_players[3:6])
    teams['Raptors'].extend(experienced_players[6:])
    return teams


def create_file(teams):
    '''
    Create output file (teams.txt) in the following format:
        Team Name
        player name, experience, Gyardian Name(s)
    :param teams: Dictionary containing Soccer Teams
    :return: None
    '''
    with open('teams.txt', 'w', encoding='utf8') as outfile:
        for team in teams:
            outfile.write(f"{team} \n")
            for player in teams[team]:
                outfile.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
    return None


if __name__ == '__main__':
    # read in the players from supplied file
    players = open_file('soccer_players.csv')
    # split the players up by experience
    new_players, experienced_players = split_players(players)
    # assemble equal teams
    teams = assemble_teams(new_players, experienced_players)
    # create the output file
    create_file(teams)
