from jinja2 import Environment, FileSystemLoader
import pickle
from genXML import tewiki, writePage

# transliterate libraries
from deeptranslit import DeepTranslit
transliterator = DeepTranslit('telugu').transliterate

# translation libraries
# from google_trans_new import google_translator  
# translator = google_translator()

# function defination for translating the words from english to telugu
def translation(name):
	trans_name = translator.translate(name,lang_tgt="te")
	return trans_name

def transliteration(name): 
	trans_text = transliterator(name)[0]    
	# if trans_text["prob"] < 0.45:
	# 	return translation(name)
	return trans_text['pred']

def getData(row):

	data = {
			"city_name" : transliteration(row.city_name.values[0]), 
			"country_name" : transliteration(row.country_name.values[0]),
			"state_name" : transliteration(row.state_name.values[0]),
			"continent_name" : transliteration(row.continent_name.values[0]),
			"area" : str(row.area.values[0]),
			"population" : str(row.population.values[0]),
			"population_acc_to_year" : str(row.population_acc_to_year.values[0]),
			"is_state_capital" : row.is_state_capital.values[0],
			"is_country_capital" : row.is_country_capital.values[0],
			"other_names" : transliteration(row.other_names.values[0]),
			"GWCR_ranking" : transliteration(row.GWCR_ranking.values[0]),
			# "is_largest_country" :row.is_largest.values[0],
			# "city_type" : row.city_type.values[0],
			# "most_populous" : row.is_populous.values[0]
		}
	return data

def main():
	# Load Jinga template 
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader)
	template = env.get_template('City_Intro_Template2.j2')


	citiesDF =pickle.load(open('./data/citiesDF.pkl', 'rb'))

	ids = citiesDF.city_id.tolist()
	# ids =ids[:100] #remove this to generate articles for all movies

	# File object creation
	# sample text file to review the output.
	fobj1 = open("output.txt" , "w" , encoding= "utf-8")

	#file object for writing xml file (use this after reviewing the articles) 
	# fobj = open('cities.xml', 'w' , encoding="utf-8")
	# fobj.write(tewiki+'\n')

	for i, id in enumerate(ids):
		row = citiesDF.loc[citiesDF['city_id']==id]
		
		# title = row.name.values[0]
		# print(getData(row))
		
		text = template.render(getData(row))
		
		# writePage(title, text, fobj)	
		fobj1.write('\t'+text + '\n\n\n')
		
	# fobj.write('</mediawiki>')
	# fobj.close()
	fobj1.close()

if __name__ == '__main__':
	main()