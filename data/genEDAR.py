import pickle
import sweetviz as sv 

citiesDF = pickle.load(open('./citiesDF.pkl', 'rb'))
report = sv.analyze([citiesDF, 'Cities'])


report.show_html()