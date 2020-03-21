import os
import glob
import numpy as np
import pandas as pd

def main():

	# Read columns in
	columns = pd.read_csv('data/raw/retrosheet-columns.txt')
	columns = columns['column_name'].tolist()

	# Training data
	all_data = []

	# Loop through all the files...
	files = glob.glob('data/raw/gl1871_2019/*')
	for counter, file in enumerate(files):

		if counter % 10 == 0:
			print(f"Processing {counter}th file")

		# Read data
		data = pd.read_csv(file, header=None)
		data.columns = columns
	
		# Append
		all_data.append(data)

	# Combine training and test data
	all_data = pd.concat(all_data, axis=0)
	num_games = all_data.shape[0]
	new_index = np.arange(0, num_games, 1)
	all_data.index = new_index

	# Select random subset for training
	np.random.seed(110)
	train_inds = []
	test_inds = []

	# Speedy way to create test/train split
	np.random.shuffle(new_index)
	for i, j in enumerate(new_index):
		if i % 4 == 0:
			test_inds.append(j)
		else:
			train_inds.append(j)
	train_data = all_data.loc[train_inds]
	test_data = all_data.loc[test_inds]

	# Make directory
	if not os.path.exists('data/processed/'):
		os.makedirs('data/processed/')

	train_data.to_csv('data/processed/train.csv', index=False)
	test_data.to_csv('data/processed/test.csv', index=False)


if __name__ == '__main__':
	main()