#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallonsUsed = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter the cost per gallon:\t"))

mpg = miles_driven / gallonsUsed
cost_per_gallon * gallonsUsed

gas_cost = gallonsUsed * cost_per_gallon

cost_per_mile = gas_cost / miles_driven
            
# format and display the result
print()
print("Miles Per Gallon:\t" + str(mpg))
print("Total Gas Cost:\t\t" +str(gas_cost))
print("Cost Per Mile:\t\t" +str(cost_per_mile))
print("Bye")