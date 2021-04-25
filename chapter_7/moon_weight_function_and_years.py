def mooon_weight(weight, increase, years, step):
	for year in range(1, years+1, step):
		w = weight + year
		print('Year %s is %f' % (year, w*0.165))


years = int(input("How many years?"))
weight = int(input("What is your weight?"))
step = int(input("How many steps?"))

mooon_weight(weight,0.165,years, step)




