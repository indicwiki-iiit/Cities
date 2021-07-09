import pickle
import pandas as pd
def main():
	# Change the data set file here for different versions of project
	citiesFile = './29k_full.xlsx'
	citiesDF = pd.read_excel(citiesFile,dtype = "unicode")
	pickle.dump(citiesDF, open('./citiesDF.pkl', 'wb'))


if __name__ == '__main__':
	main()