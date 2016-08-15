# Parses csv data files and returns appropriate data structures (i.e. lists)
import csv
from os import path

# Returns emg_data object from csv
def emg_data_set_from_csv(filename):
	return False
	# return emg_data_set

def get_label(data_sample):
	num_inputs = 8
	return data_sample[num_inputs]