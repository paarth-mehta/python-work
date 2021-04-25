import sys
def mooon_weight(weight, increase, years, step):
	for year in range(1, years+1, step):
		w = weight + year
		print('Year %s is %f' % (year, w*increase))

print("How many years?")
years = int(sys.stdin.readline())

print("Please enter your current Earth weight?")
weight = int(sys.stdin.readline())

print("How many steps?")
step = int(sys.stdin.readline())

print("Please enter the amount your weight might increase each year")
factor = float(sys.stdin.readline())

mooon_weight(weight,factor,years, step)
