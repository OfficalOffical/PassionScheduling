from numpy import random
import schedule


x = random.poisson(lam=4, size=3)
y = random.poisson(lam=10, size=3)



schedule.MLFQ(x,y) #Multilevel feedback Queue scheduling


