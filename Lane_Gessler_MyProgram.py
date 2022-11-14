from Lane_Gessler_Stats import mean
from Lane_Gessler_Stats import median

d = open("Lane_Gessler_output.txt","w")

f = open("500DayFruitData.txt")
r=f.read()
r=r.split()
#opens "500DayFruitData.txt and splits the text file into entrys for a list after every space
# r hold all of the data in the form of a list

#print(mean(r))
#print(median(r))
# I spent one hour trying to figure out how to put a list through the functions.
mean = mean(r)
median = median(r)

d.write("The mean number of apples eaten is ")
d.write(str(mean))

d.write("\nThe median number of apples eaten is ")
d.write(str(median))

#another hour spent here

d.close()
