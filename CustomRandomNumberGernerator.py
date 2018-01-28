import math
import time

class RandomNumberGenerator:
    def __init__(self, seed=time.time(), a=1664525, c=1013904223, m=math.pow(2,32)):
        # initialise variables
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def lcg(self):
        # Creating PRNG using LCG
        self.seed = int(self.c + self.seed * self.a) % self.m
        random = 0
        random = self.seed / self.m
        return random

    def lcg_to_range(self,min,max):
        # Generating random number in given range
        lcg = self.lcg()
        random = min + lcg * (max-min+1)
        return random

if __name__ == "__main__":
    obj = RandomNumberGenerator()
    l_len = 0
    u_len = 0
    random_list = []
    l_lim = int(input("Enter Lower value of range\n"))
    u_lim =int(input("Enter Upper value of range\n"))
    mid_val = (l_lim + u_lim) / 2
    for i in range(100):
		p = int(obj.lcg_to_range(1,100))
		if p>73:
			random_list.append(int(obj.lcg_to_range(l_lim,mid_val-1)))
			l_len+=1
		else:
			random_list.append(int(obj.lcg_to_range(mid_val+1,u_lim)))
			u_len+=1
    print("No. of elements <"+str(mid_val)+" "+str(l_len))
    print("No. of elements >"+str(mid_val)+" "+str(u_len))
    print("Random list: ")
    print(random_list)
