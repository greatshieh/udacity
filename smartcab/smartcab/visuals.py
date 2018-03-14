import numpy as np
import pandas as pd
import os
import ast


def calculate_safety(data):
	""" Calculates the safety rating of the smartcab during testing. """

	good_ratio = data['good_actions'].sum() * 1.0 / \
	(data['initial_deadline'] - data['final_deadline']).sum()

	if good_ratio == 1: # Perfect driving
		return "A+"
	else: # Imperfect driving
		if data['actions'].apply(lambda x: ast.literal_eval(x)[4]).sum() > 0: # Major accident
			return "F"
		elif data['actions'].apply(lambda x: ast.literal_eval(x)[3]).sum() > 0: # Minor accident
			return "D"
		elif data['actions'].apply(lambda x: ast.literal_eval(x)[2]).sum() > 0: # Major violation
			return "C"
		else: # Minor violation
			minor = data['actions'].apply(lambda x: ast.literal_eval(x)[1]).sum()
			if minor >= len(data)/2: # Minor violation in at least half of the trials
				return "B"
			else:
				return "A"


def calculate_reliability(data):
	""" Calculates the reliability rating of the smartcab during testing. """

	success_ratio = data['success'].sum() * 1.0 / len(data)

	if success_ratio == 1: # Always meets deadline
		return "A+"
	else:
		if success_ratio >= 0.90:
			return "A"
		elif success_ratio >= 0.80:
			return "B"
		elif success_ratio >= 0.70:
			return "C"
		elif success_ratio >= 0.60:
			return "D"
		else:
			return "F"


def plot_trials(csv):
	""" Plots the data from logged metrics during a simulation."""

	data = pd.read_csv(os.path.join("logs", csv))
	
	# Create additional features
	data['average_reward'] = (data['net_reward'] / (data['initial_deadline'] - data['final_deadline'])).rolling(window=10, center=False).mean()
	data['reliability_rate'] = (data['success']*100).rolling(window=10, center=False).mean()  # compute avg. net reward with window=10
	data['good_actions'] = data['actions'].apply(lambda x: ast.literal_eval(x)[0])
	data['good'] = (data['good_actions'] * 1.0 / \
		(data['initial_deadline'] - data['final_deadline'])).rolling(window=10, center=False).mean()
	data['minor'] = (data['actions'].apply(lambda x: ast.literal_eval(x)[1]) * 1.0 / \
		(data['initial_deadline'] - data['final_deadline'])).rolling(window=10, center=False).mean()
	data['major'] = (data['actions'].apply(lambda x: ast.literal_eval(x)[2]) * 1.0 / \
		(data['initial_deadline'] - data['final_deadline'])).rolling(window=10, center=False).mean()
	data['minor_acc'] = (data['actions'].apply(lambda x: ast.literal_eval(x)[3]) * 1.0 / \
		(data['initial_deadline'] - data['final_deadline'])).rolling(window=10, center=False).mean()
	data['major_acc'] = (data['actions'].apply(lambda x: ast.literal_eval(x)[4]) * 1.0 / \
		(data['initial_deadline'] - data['final_deadline'])).rolling(window=10, center=False).mean()
	data['epsilon'] = data['parameters'].apply(lambda x: ast.literal_eval(x)['e']) 
	data['alpha'] = data['parameters'].apply(lambda x: ast.literal_eval(x)['a']) 


	# Create training and testing subsets
	testing_data = data[data['testing'] == True]


	safety_rating = calculate_safety(testing_data)
	reliability_rating = calculate_reliability(testing_data)
	
	return safety_rating, reliability_rating
