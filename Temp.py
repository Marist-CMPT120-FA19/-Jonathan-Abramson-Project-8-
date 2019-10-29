#Designed by Jonathan Abramson
#Cooling/Heating Degree Day Estimates
#Have a go!

def main():
    Temperature = input("Input the average daily temperatures and separate with commas (,): ")
    Temperature = Temperature.split(",")
    cool=0
    heat=0

    for i in Temperature:
        if int(i) < 60 or int(i) > 80:
            if int(i) > 80:
                cool= cool + (int(i)-80)
            else:
                heat = heat + (60-int(i))
                
    print("The current estimate is", cool, "cooling degree days and", heat, "heating degree days.")
    
main()