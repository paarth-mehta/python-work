weight=int(input("What is your weight?"))
for year in range(1,16):
 weight = weight + 1
 moon_weight = weight * 0.165
 print('Year %s is %s' % (year, moon_weight))
