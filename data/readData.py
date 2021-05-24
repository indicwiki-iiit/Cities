import pickle
import pandas as pd
def main():
	citiesFile = './cities2.csv'
	citiesDF = pd.read_csv(citiesFile)
	pickle.dump(citiesDF, open('./citiesDF.pkl', 'wb'))


if __name__ == '__main__':
	main()