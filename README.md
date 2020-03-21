# Competition Rules

## Overview

As you can see in the ``evaluation.py`` file, the competition is decided as follows:

1. Your algorithm will be given access to three quarters of all of the baseball games ever played to train itself. These games are chosen randomly.
2. After training, we loop through the remaining quarter of the games in chronological order. For each game, the algorithm is asked to predict the winner. After predicting each game, the algorithm is given the results of the game (winner, scoreline, player performances, etc).
3. The algorithm with higher overall accuracy wins! 

## Your Algorithm

Your algorithm should be a class which implements the following methods:

1. ``train``: Given a pandas dataframe of the training data, it will do most of the computation it needs to create predictions. It's fine if this takes a bit of time.

Specifically, the input to the ``train`` method will be the following: 
``train_data = pd.read_csv('data/processed/train.csv')``

2. ``predict``: Given identifying information of a small number of games (anywhere between 1 and 100) from the testing data, it predicts the outcomes of those games. This should be basically instant.

The format of the data inputed will be similar to the training data, but only a subset of the columns. In particular, it will be the following columns:

``[
	'yyyymmdd',
	'game_no',
	'weekday',
	'visiting_team',
	'visiting_team_league',
	'home_team',
	'home_team_league',
	'daytime',
	'park_id',
]
``
plus, in addition, all of the starting players for both teams and their defensive positions. As described below, these columns have the following names:
```
[
		'home_starting_player1_id',
		'home_starting_player1_name',
		'home_starting_player1_def_position',
]
```

Note that in the output, which should be a pandas series in the same order as the prediction input, a 0 means that the home team won, whereas a 1 means that the visiting team won.

3. ``update``: Given **the full set of outcomes** from a small number of games (anywhere between 1 and 100), it adds the additional data to the algorithm.  The input to the ``update`` function will be identical to the input to the ``train`` function, except it will be much a smaller amount of data.

# Data 

## Overview

There are two CSVs of 

## Data Use

The columns of the data are listed below. For context on what they mean, read the retrosheet-readme.txt file. 

id,column_name
0,yyyymmdd
1,game_no
2,weekday
3,visiting_team
4,visiting_team_league
5,visiting_team_game_no
6,home_team
7,home_team_league
8,home_team_game_no
9,visiting_team_score
10,home_team_score
11,game_length_in_outs
12,daytime
13,completion
14,forfeit
15,protest
16,park_id
17,attendance
18,game_length_in_minutes
19,visiting_score_line
20,home_score_line
21,visiting_at_bats
22,visiting_hits
23,visiting_doubles
24,visiting_triples
25,visiting_homeruns
26,visiting_RBI
27,visiting_sacrifice_hits
28,visiting_sacrifice_flies
29,visiting_hit_by_pitch
30,visiting_walks
31,visiting_intentional_walks
32,visiting_striekouts
33,visiting_stolen_bases
34,visiting_caught_stealining
35,visiting_grounded_into_double_plays
36,visiting_awarded_first
37,visiting_left_on_base
38,visiting_pitchers_used
39,visiting_individual_earned_runs
40,visiting_team_earned_runs
41,visiting_wild_pitches
42,visiting_balks
43,visiting_putouts
44,visiting_assists
45,visiting_errors
46,visiting_passed_balls
47,visiting_double_plays
48,visiting_triple_plays
49,home_at_bats
50,home_hits
51,home_doubles
52,home_triples
53,home_homeruns
54,home_RBI
55,home_sacrifice_hits
56,home_sacrifice_flies
57,home_hit_by_pitch
58,home_walks
59,home_intentional_walks
60,home_striekouts
61,home_stolen_bases
62,home_caught_stealining
63,home_grounded_into_double_plays
64,home_awarded_first
65,home_left_on_base
66,home_pitchers_used
67,home_individual_earned_runs
68,home_team_earned_runs
69,home_wild_pitches
70,home_balks
71,home_putouts
72,home_assists
73,home_errors
74,home_passed_balls
75,home_double_plays
76,home_triple_plays
77,home_plate_umpire_id
78,home_plate_umpire_name
79,1B_umpire_id
80,1B_umpire_name
81,2B_umpire_id
82,2B_umpire_name
83,3B_umpire_id
84,3B_umpire_name
85,LF_umpire_id
86,LF_umpire_name
87,RF_umpire_id
88,RF_umpire_name
89,visiting_manager_id
90,visiting_manager_name
91,home_manager_id
92,home_manager_name
93,winning_pitcher_id
94,winning_pitcher_name
95,losing_pitcher_id
96,losing_pitcher_name
97,saving_pitcher_id
98,saving_pitcher_name
99,game_winning_rbi_batter_id
100,game_winning_rbi_batter_name
101,visiting_starting_pitcher_id
102,visiting_starting_pitcher_name
103,home_starting_pitcher_id
104,home_starting_pitcher_name
105,visiting_starting_player1_id
106,visiting_starting_player1_name
107,visiting_starting_player1_def_position
108,visiting_starting_player2_id
109,visiting_starting_player2_name
110,visiting_starting_player2_def_position
111,visiting_starting_player3_id
112,visiting_starting_player3_name
113,visiting_starting_player3_def_position
114,visiting_starting_player4_id
115,visiting_starting_player4_name
116,visiting_starting_player4_def_position
117,visiting_starting_player5_id
118,visiting_starting_player5_name
119,visiting_starting_player5_def_position
120,visiting_starting_player6_id
121,visiting_starting_player6_name
122,visiting_starting_player6_def_position
123,visiting_starting_player7_id
124,visiting_starting_player7_name
125,visiting_starting_player7_def_position
126,visiting_starting_player8_id
127,visiting_starting_player8_name
128,visiting_starting_player8_def_position
129,visiting_starting_player9_id
130,visiting_starting_player9_name
131,visiting_starting_player9_def_position
132,home_starting_player1_id
133,home_starting_player1_name
134,home_starting_player1_def_position
135,home_starting_player2_id
136,home_starting_player2_name
137,home_starting_player2_def_position
138,home_starting_player3_id
139,home_starting_player3_name
140,home_starting_player3_def_position
141,home_starting_player4_id
142,home_starting_player4_name
143,home_starting_player4_def_position
144,home_starting_player5_id
145,home_starting_player5_name
146,home_starting_player5_def_position
147,home_starting_player6_id
148,home_starting_player6_name
149,home_starting_player6_def_position
150,home_starting_player7_id
151,home_starting_player7_name
152,home_starting_player7_def_position
153,home_starting_player8_id
154,home_starting_player8_name
155,home_starting_player8_def_position
156,home_starting_player9_id
157,home_starting_player9_name
158,home_starting_player9_def_position
159,additional_info
160,acquisition_information

## Sources

- https://www.retrosheet.org/gamelogs/index.html
- http://www.seanlahman.com/
