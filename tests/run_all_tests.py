#Tests
from os import path
import sys 

dir_path = path.dirname(path.realpath(__file__))
sys.path.append(path.join(dir_path,'../scripts'))

import preprocessing

def split_data_by_label_test_reduces_properly():
	numLabels = 10
	labelSetSize = 10

	#create fake data
	data_iterator = []
	for i in range(numLabels * 10):
		data_frame = []
		for j in range(8):
			data_frame.append(j)

		data_frame.append(i / 10 + 1)
		data_iterator.append(data_frame)

	split_sets = preprocessing.split_data_by_label(data_iterator, 80.0)
	labelOutputSize = int(labelSetSize * 0.8);	

	for i in range(len(split_sets)):
		label_set = split_sets[i]

		#check size of each set, which should be trimmed according to second param
		if len(label_set) != labelOutputSize:
			print("Expected different output size")
			return False

		for j in range(labelOutputSize):
			data_frame = label_set[j]

			#check the length of a data frame
			if len(data_frame) != 9:
				print("Expected different frame size")
				return False

			#check that values haven't been changed
			for k in range(8):
				if data_frame[k] != k:
					print("Expected different values")
					return False

			#check that label matches
			if data_frame[8] != (i + 1):
				print("Expected different label. Expected: " + str(i+1) + ", Got: " + str(data_frame[8]))
				return False

	return True

def split_data_by_label_test_splits_properly():
	numLabels = 10
	labelSetSize = 10

	#create fake data
	data_iterator = []
	for i in range(numLabels * 10):
		data_frame = []
		for j in range(8):
			data_frame.append(j)

		data_frame.append(str(i / 10 + 1))
		data_iterator.append(data_frame)

	split_sets = preprocessing.split_data_by_label(data_iterator, 80.0)

	#check the number of sets with same label
	if len(split_sets) != numLabels:
		return False

	return True

def bandpass_filter_data_filters_properly():
	# create sin fnction consisting of 10, 30, & 50 Hz freq
	# filter it with our filter
	# fft it
	# check that primary frequency is 30Hz

def main(argv):
	print("Running Tests");
	testResults = []
	testTitles = []

	result = split_data_by_label_test_splits_properly()
	testResults.append(result)
	testTitles.append("split_data_by_label:: splits properly")

	result = split_data_by_label_test_reduces_properly()
	testResults.append(result)
	testTitles.append("split_data_by_label:: reduces properly")

	for i in range(len(testResults)):
		s = "Test -- " + testTitles[i] + ": "
		if testResults[i]:
			s = s + "PASSED"
		else:
			s = s + "FAILED"

		print(s)


if __name__ == '__main__':
	main(sys.argv[1:])