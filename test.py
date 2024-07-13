# Libraries
import math 
import customtkinter
import matplotlib.pyplot as plt

# Input
period = float(0)
principle_amount = float(input("principle amount = "))
interest_rate = float(input("interest amount = "))
time = int(input("time = "))

# Function
def compound_interest(period,principle_amount,interest_rate,time):   
    amounts = []
    cis = []
    for period in range(time):
        amt = principle_amount * (math.pow((1 + (interest_rate/100)),period+1))
        amounts.append(amt)
        ci = amt - principle_amount
        cis.append(ci)
        
    return amounts, cis

# Function call
amounts, cis = compound_interest(period,principle_amount,interest_rate,time)

print("compound amount: ", amounts)
print("cis: ", cis)

# Plotting
plt.bar(range(1, time+1), principle_amount, color='blue')
plt.bar(range(1, time+1), cis, bottom = principle_amount, color ='red')
plt.xlabel('Time Period')
plt.ylabel('Compound Amount')
plt.title('Compound Interest Over Time')
plt.show()
