# Custom-Random-Generator
Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want a random number between 1 to 10 100times then it should give number more than 5 73times and less than 5 27times.

# Algorithm:

Step 1 : Take input from user:

  1.1 := lower limit
  
  1.2 := upper limit

Step 2 : Calculating mid value for biased probability
  mid_val := (a+b)/2

Step 3 : Calculate random number within range 1 to 100 using Linear congruential generator(Pseudo-random Number Genrator)
  p := lcg_to_range(1,100)
Step 4 : Check whether the number lies above 73 or not and calculate random number in specified range accordingly

              if p>73:
			  random_list.append(int(obj.lcg_to_range(l_lim,mid_val-1)))
			  l_len+=1
		  else:
			  random_list.append(int(obj.lcg_to_range(mid_val+1,u_lim)))
			  u_len+=1
	  
Step 5 : Display l_len(# of numbers less than mid_val), u_len(# of numbers greater than mid_val) and Random_list

Explanation:

    First take the lower limit and upper limit of range from user. Calculate mid value from these two limits to separate the range into two parts upper range and lower range. Calculate the middle value of range.

    Start the for loop that is to be run 100 times(It can be run as many times the user wants). In this loop random number is generated using Linear congruential generator(LCG) method in which an equation is used ie [new_seed = (c + a * previous_seed) % mod] and then 'new_seed' generated from this equation is put into [random = number / mod] (which will give output value between 0 and 1). And this value is put into a formula [lower limit + value * (upper limit - lower limit + 1)] to calculate random number in given desired range.

    The above method describes generation of random numbers. All the constants(a,c,m) are taken from wikipedia.
    A number in range 1 to 100 is generated using LCG in every iteration which is unbiased i.e., each number in range 1 to 100 is equally likely to be chosen. Now, if the random number is greater than 73(total of 27 choices(100-73)) then again a random number is chosen in range [lowerlimit,middle value), otherwise a number is randomly chosen in range(middle value,upperlimit]. This ensures a 73/100 i.e., 73% biasness on numbers greater than middle value and a 27/100 i.e., 27% biasness on numbers less than middle value.
    
    All numbers are stored in a list and finally displayed along with their counts based on whether they are less than or greater than middle value of the range. 

    Then print final_list ie concatenated list of max_list and min_list

