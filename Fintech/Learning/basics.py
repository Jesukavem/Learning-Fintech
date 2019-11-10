#Let's say you get 5% interest from your bank every year, what is it worth after 5?
#We could use a loop to print the value at each point
p = 100
r = .05
A = p
for t in range(5):
    A = A*(1+r)
    print(A)


#We might also wonder how much it increases by each period
p = 100
r = .05
A = p
for t in range(5):
    last = A
    A = A*(1+r)
    print(A-last)
#Notice how the amount of interest we get each period goes up. It grows with our investment

#Notice that using the equation yields the same result
#But we change the range to match the time periods
p = 100
r = .05
for t in range(1,6):
    print(p*(1+r)**t)

#Function for present value
def compoundInterest(p,r,t):
    A = p*(1+r)**t
    return A
print(compoundInterest(100,.05,5))


#Let's make a list of years we want to see the value of our investment over
t = list(range(26))
print(t)


#And use list comprehension to get each year's values
r = .1
P = 100
A = [compoundInterest(P,r,x) for x in t]
print(A)


import matplotlib.pyplot as plt
plt.plot(t,A)
plt.xlabel("t")
plt.ylabel("Value")
plt.title("Compound Interest")
plt.show()