from jinja2 import Environment, FileSystemLoader
import pickle
from genXML import tewiki, writePage
import ast
import time 

def getData_Intro(row, data):
	intro_data = {
			"city_name" : row.te_city_name.values[0], 
			"en_city_name" : row.city_name.values[0],
			"country_name" : row.te_country_name.values[0],
			"state_name" : row.te_state_name.values[0],
			"continent_name" : row.te_continent_name.values[0],
			"area" : str(row.area.values[0]),
			"population" : str(row.population.values[0]),
			"population_acc_to_year" : str(row.population_acc_to_year.values[0]),
			"is_state_capital" : row.is_state_capital.values[0],
			"is_country_capital" : row.is_country_capital.values[0],
			"other_names" : row.te_other_names.values[0],
			"GWCR_ranking" : row.te_GWCR_ranking.values[0],
			"elevation": row.elevation.values[0],
			"settlement_type" : row.te_settlement_type.values[0],
			"founder" : row.te_founder.values[0]
		}
	data.update(intro_data)
	return data

def getData_demographics(row,data):
	demographics_data = {
			"population_density" : row.populationdensity.values[0],
			"unemployment_rate" : row.unemployment_rate.values[0],
			"population_rank" : row.population_rank.values[0],
			"demonym" : row.te_demonym.values[0]
	} 
	data.update(demographics_data)
	return data

def getData_governance(row,data):
	governance_data = {
			"govType" : row.te_govType.values[0],
			"leaderName" : row.te_leaderName.values[0],
			"govBody" : row.te_govBody.values[0],
			"leaderTitle" : row.te_leaderTitle.values[0]
	}
	data.update(governance_data)
	return data

def getData_climate(row,data):
	climate_data = {
			"recHigh" : row.recHigh.values[0],
			"recLow" : row.recLow.values[0],
			"avgHighM" : row.avgHighM.values[0],
			"avgLowM" : row.avgLowM.values[0],
			"dailyMeanY": row.dailyMeanY.values[0],
			"meanMSunShineY": row.meanMSunShineY.values[0],
			"avgRelHumidity" : row.avgRelHumidity.values[0],
			"avgUVIdx" : row.avgUVIdx.values[0],
			"summer": row.te_summer.values[0],
			"winter": row.te_winter.values[0],
	}
	for key in climate_data:
		climate_data[key] = climate_data[key].replace("Â","")
	data.update(climate_data)
	return data

def getData_climateTable(row,data):
	cli_data = row.climate_dict.values[0]
	cli_data = ast.literal_eval(cli_data)
	table_data = {}
	for i in cli_data.keys():
		temp_key = "_".join(i.replace("Â°","").split(" "))
		table_data[temp_key] = cli_data[i]
	data.update(table_data)
	return data

def clean_notables(s):
	i=0
	l="1234567890."
	while s[i] in l and i<len(s):
		i+=1
		# print(s[i:])
	return s[i:]

def getData_notables(row,data):
	notables_data1 = {
		"places" : ast.literal_eval(row.te_Notableplaces.values[0]),
		"stadiums_im" : ast.literal_eval(row.te_Stadiums_image_cap.values[0]),
		"beaches_im" : ast.literal_eval(row.te_Beach_image_cap.values[0])
	}
	try:
		notables_data1["places"] = list(map(clean_notables,notables_data1["places"]))
	except:
		notables_data1["places"] = []
	
	notables_data2 = {
		"stadiums" : ast.literal_eval(row.te_Stadiums.values[0]),
		"beaches" : ast.literal_eval(row.te_Beach.values[0])
	}
	for key in notables_data2:
		try:
			for entry in notables_data2[key]:
				entry[1] = round(entry[1])
		except:
			notables_data2[key] = []

	data.update(notables_data1)
	data.update(notables_data2)
	return data

def getData_transport(row,data):
	trans_data = {
		"airports" : ast.literal_eval(row.te_Airports.values[0]),
		"busstands" : ast.literal_eval(row.te_Busstand.values[0]),
		"ports" : ast.literal_eval(row.te_Ports.values[0]),
		"railways" : ast.literal_eval(row.te_Railway_station.values[0]),
	}
	trans_img_data = {
		"airports_im" : ast.literal_eval(row.te_Airports_image_cap.values[0]),
		"busstands_im" : ast.literal_eval(row.te_Busstand_image_cap.values[0]),
		"ports_im" : ast.literal_eval(row.te_Ports_image_cap.values[0]),
		"railways_im" : ast.literal_eval(row.te_Railway_station_image_cap.values[0]),
	}
	for key in trans_data:
		try:
			for entry in trans_data[key]:
				entry[1] = round(entry[1])
		except:
			trans_data[key] = []		
	
	data.update(trans_data)
	data.update(trans_img_data)
	return data

def getData_gallery(row,data):
	gallery_data = {
		"gallery" : ast.literal_eval(row.te_gallery.values[0])
	}
	data.update(gallery_data)
	return data

def getInfoBox(id):
	try:
		f = open("./infoboxes1/"+id+".txt","r",encoding='utf-8')
		l = f.readlines()
		s = ""
		for i in l:
			s+=i
		return s
	except:
		return ""

def main():
	s_time = time.time()
	# Load Jinga template 
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader)
	introTemplate = env.get_template('Introduction.j2')
	demoTemplate = env.get_template('Demographics.j2')
	govTemplate = env.get_template('governance.j2')
	cli_dataTemplate = env.get_template('climate.j2')
	cli_dictTemplate = env.get_template('climateTable.j2')
	notablesTemplate = env.get_template('notablePlaces.j2')
	transportTemplate = env.get_template('transport.j2')
	galleryTemplate =env.get_template('gallery.j2')
	referencesTemplate = env.get_template('references.j2')
	
	citiesDF =pickle.load(open('./data/citiesDF.pkl', 'rb'))
	
	ids = citiesDF.Id.tolist()[:20]

	# File object creation
	# sample text file to review the output.
	# fobj1 = open("output.txt" , "w" , encoding= "utf-8")

	#file object for writing xml file (use this after reviewing the articles) 
	fobj = open('cities.xml', 'w' , encoding="utf-8")
	fobj.write(tewiki+'\n')


	for i, id in enumerate(ids):
		row = citiesDF.loc[citiesDF['Id']==id]
		cli_table_check = row.climate_dict.values[0]

		title = row.te_city_name.values[0]
		# print(getData(row))
		data = {}
		data = getData_Intro(row,data)
		data = getData_demographics(row,data)
		data = getData_governance(row,data)
		data = getData_climate(row,data)
		if cli_table_check!="None":
			data = getData_climateTable(row,data)
		data = getData_notables(row,data)
		data = getData_transport(row,data)
		data = getData_gallery(row,data)
		data["places_reference"] = row.places_reference.values[0] 
		# print(data, len(data))

		# for key in data.keys():
		# 	print(key,"-",data[key])
		climateTableText=""

		introText= introTemplate.render(data)
		demographicsText = demoTemplate.render(data)
		governanceText = govTemplate.render(data)
		climateDataText = cli_dataTemplate.render(data)
		if cli_table_check!="None":
			climateTableText = cli_dictTemplate.render(data)
		notablesText = notablesTemplate.render(data)
		transportText = transportTemplate.render(data)
		galleryText = galleryTemplate.render(data)
		infoboxText = getInfoBox(row.Id.values[0])
		referencesText = referencesTemplate.render(data)
		text = infoboxText+'\n'+introText+'\n'+demographicsText +'\n'+governanceText+'\n'+climateDataText+'\n'+climateTableText+'\n'+notablesText+'\n'+transportText+'\n'+galleryText+'\n'+referencesText
		writePage(title, text, fobj)	
		# fobj1.write('\n' +text + '\n\n\n')
		
	fobj.write('</mediawiki>')
	fobj.close()
	# fobj1.close()
	e_time = time.time()
	print(e_time-s_time)

if __name__ == '__main__':
	main()