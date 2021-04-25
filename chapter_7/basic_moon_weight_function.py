weight=int(input("What is your weight?"))
# weight_factor=float(input("Moon weight factor?"))
year_gap=int(input("After how many years?"))

def moon_weight(initial_weight, factor, year_gap):
	for year in range(1,16, year_gap):
		initial_weight = initial_weight + year_gap
		moon_weight = initial_weight * factor
		print('Year %s is %s' % (year, moon_weight))
		
print(moon_weight(weight, 0.165, year_gap))
