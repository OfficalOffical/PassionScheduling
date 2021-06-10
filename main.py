from numpy import random
import schedule


x = random.poisson(lam=2, size=5)
y = random.poisson(lam=10, size=5)



schedule.MLFQ(x,y) #Multilevel feedback Queue scheduling



