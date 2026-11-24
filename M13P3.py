from pathlib import Path

# function section

def display_players(player_averages):
    print(f"{'Last Name':<16}{'Batting Average':>16}")

    for last_name, batting_average in player_averages.items():
        print(f"{last_name:<16}{batting_average:>16.3f}")


# input section

player_file = Path(__file__).with_name("players.txt")
player_averages = {}

# processing section

with open(player_file, "r", encoding="utf-8") as data_file:
    for player_line in data_file:
        last_name, average_text = player_line.strip().split(",")
        player_averages[last_name] = float(average_text)

# output section

display_players(player_averages)
