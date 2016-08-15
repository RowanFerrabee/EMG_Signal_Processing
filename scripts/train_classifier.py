from sys import argv

def main(args):
	

if __name__ == '__main__':
	if (len(argv) < 2):
		print "Usage: pass in EMG data files you wish to train the classifier with. For file format, see README.txt"
	else:
		main(argv[1:])
