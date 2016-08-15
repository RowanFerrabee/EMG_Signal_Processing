# Does simple preprocessing of data such as bandpass filtering, normalization, and segmenting data sets into more useful arrangements
import csv
from file_reading import get_label
from sys import argv
from os import path

# Takes a generator of labelled of emg samples and splits it by label. Setting the percent_kept set the percent of samples from each label that the program will keep.
# In cases where percept_kept is set, the program will take from the middle section of the data set to get the portion of the data with the most constant signal.
# data_iterator should be an array or generator, each iterand is an array where all but the last value are emg readings, and the last value is a label
def split_data_by_label(data_iterator, percent_kept=100.0):
	if isinstance(percent_kept, int):
		percent_kept = float(percent_kept)
	elif not(isinstance(percent_kept, float)):
		print "Error: percent_kept variable must be of type float or int"
		return []

	num_data_sets = 0
	data_sets = []
	current_label = -1
	for sample in data_iterator:
		if (get_label(sample) != current_label):
			data_sets.append([sample])
			num_data_sets += 1
			current_label = get_label(sample)
		else:
			data_sets[num_data_sets-1].append(sample)

	if (percent_kept < 100.0 and percent_kept > 0.0):
		for idx, data_set in enumerate(data_sets):
			edge_trim = int((50.0-percent_kept/2)*len(data_set)/100.0)	# Amount to trim off of each end of the data set
			data_sets[idx] = data_set[edge_trim:len(data_set)-edge_trim]

	return data_sets

# Edits data parameter (a list) such that the frequency of its contents are restricted between low_freq and high_freq (given time_interval is the interval of time between elements in the list)
def bandpass_filter(data, time_interval, low_freq, high_freq):
	
	return False
	# No return, edit data object

# Normalizes the data across all samples and all input elements
def normalize_data(data_set):
	#Determine largest magnitude
	largest_magnitude = -1
	for sample in data_set:
		for value in sample[:len(sample)-1]:
			abs_value = abs(value)
			if abs_value > largest_magnitude:
				largest_magnitude = abs_value

	#Scale data, such that largest value is now 1 (or -1)
	for sample_idx, sample in enumerate(data_set):
		for value_idx, value in enumerate(sample[:len(sample)-1]):
			data_set[sample_idx][value_idx] = value / largest_magnitude

	# No return, edited data object

def main(args):
	filename = args[0]
	filepath = path.join("../data/",filename)
	if not(path.isfile(filepath)):
		print "Error:", filename, "not found in data/ directory"
		return

	with open(filepath, "r") as f:
		reader = csv.reader(f)
		data_sets = split_data_by_label(reader, 1.0)
		print "final lens:"
		for data_set in data_sets:
			print len(data_set)


if __name__ == '__main__':
	if (len(argv) < 2):
		print "Usage: pass in name of EMG data file you wish to preprocess. For file format, see README.txt"
	else:
		main(argv[1:])