#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
        games = f.read().splitlines()

game_sheet = {
        "a": "",
        "b": "",
        "a_score": 0,
        "b_score": 0,
        "a_result": "",
        "b_result": "",
        }

a_moves = { "A": "Rock", "B": "Paper", "C": "Scissors" }
b_moves = { "X": "Rock", "Y": "Paper", "Z": "Scissors" }
move_scores = { "Rock": 1, "Paper": 2, "Scissors": 3 }
result_scores = {"Loss": 0, "Draw": 3, "Win": 6}
results = {
        "RockRock": "Draw Draw",
        "RockPaper": "Loss Win",
        "RockScissors": "Win Loss",
        "PaperRock": "Win Loss",
        "PaperPaper": "Draw Draw",
        "PaperScissors": "Loss Win",
        "ScissorsScissors": "Draw Draw",
        "ScissorsRock": "Loss Win",
        "ScissorsPaper": "Win Loss",
        }



tournament = []
for game in games:
    moves = game.split(' ')
    game_sheet["a"] = a_moves.get(moves[0])
    game_sheet["b"] = b_moves.get(moves[1])
    result = results.get(game_sheet['a']+game_sheet['b']).split(' ');
    game_sheet['a_result'] = result[0]
    game_sheet['b_result'] = result[1]
    game_sheet['a_score'] = move_scores.get(game_sheet['a'])+result_scores.get(game_sheet['a_result'])
    game_sheet['b_score'] = move_scores.get(game_sheet['b'])+result_scores.get(game_sheet['b_result'])

    print(game_sheet)
    tournament.append(game_sheet.copy())

my_score = 0
for game in tournament:
    my_score += game['b_score']


print(f"My Score: {my_score} {len(tournament)}")

b_intent = { "X": "Loss", "Y": "Draw", "Z": "Win" }
b_strat = {
        "RockLoss": "Scissors",
        "RockWin": "Paper",
        "RockDraw": "Rock",
        "PaperLoss": "Rock",
        "PaperWin": "Scissors",
        "PaperDraw": "Paper",
        "ScissorsLoss": "Paper",
        "ScissorsWin": "Rock",
        "ScissorsDraw": "Scissors",
        }

tournament = []
for game in games:
    moves = game.split(' ')
    game_sheet["a"] = a_moves.get(moves[0])
    game_sheet["b"] = b_strat.get(game_sheet["a"]+b_intent.get(moves[1]))
    result = results.get(game_sheet['a']+game_sheet['b']).split(' ');
    game_sheet['a_result'] = result[0]
    game_sheet['b_result'] = result[1]
    game_sheet['a_score'] = move_scores.get(game_sheet['a'])+result_scores.get(game_sheet['a_result'])
    game_sheet['b_score'] = move_scores.get(game_sheet['b'])+result_scores.get(game_sheet['b_result'])

    print(game_sheet)
    tournament.append(game_sheet.copy())

my_score = 0
for game in tournament:
    my_score += game['b_score']


print(f"My Score: {my_score} {len(tournament)}")

