#!/usr/bin/python3

""" 								  """

""" Title: /prime_euler_49.py					  """
""" Description: Solution for https://projecteuler.net/problem=49 """
""" 								  """

from collections import defaultdict
from prime_func import is_prime


""" Bounds of the problem is from 1000 to 1000 """
endnum=10000
primes_list=[]

""" Figure out if each number is prime                     """
""" Spoiler: Whittle count to 1061 from 9000 possibilities """

for number in range(1000, endnum):
	isitprime=is_prime(number)
	if isitprime == 'prime':
		primes_list.append(number)
#Members are simply 4-digit primes : (4799)

""" Create dict (prime_dict) with each prime being a member of a list of values  """
""" that is keyed by the numerically sorted numbers shared by the primes.	 """
""" NOTE: Convert each prime's string to digits, sort,concat back and join them  """
""" and store in dict again as we did primes_list above			         """
""" Spoiler: We now have 336 unique sets				    	 """

prime_dict = defaultdict(list)
for each_prime in primes_list:
	digits = [int(x) for x in str(each_prime)]
	digits.sort()
	digits = [str(x) for x in digits]
	digits_sorted=str.join('',digits)
	prime_dict[digits_sorted].append(each_prime)
#Members look like:
#4799 : [9497, 9479])
#0113 : [1013,1031,1103,1301]

"""
#save for debugging
	for key,list in prime_dict.items():
		print ("k:",key)	
		for x in list:  
			print ("vals:",x)	
"""

""" 
Get a visual to scroll through and then massage the data. Reading the problem it seems like 
the numbers should also share a delta of 3300 but it could be 'some common delta'. Here we 
get some candidates to focus on. You should see a pattern emerge like a sore thumb.
Spoiler: Down to 174
"""

for prime_combos in prime_dict.values():
	if len(prime_combos) > 2:
		#We need only look at sets with 3 values or more
		#Make a copy of the list to reduce visual confusion
		cp_prime_combos=prime_combos

		delta_prime_pairs=[]
		for prime in cp_prime_combos:
			delta_prime_pairs.extend(
				{abs(other_prime - prime): (other_prime, prime)}
				for other_prime in cp_prime_combos
			)
		#Members look like: 2700 [(6337, 3637)]
		#                 : 2700 [(6373, 3673)]
		#                 : 2700 [(3637, 6337)]

		delta_dict = defaultdict(list)
		for dicts in delta_prime_pairs:	
			for delta,prime_tuple in dicts.items():
				delta_dict[delta].append(prime_tuple)
		#
		#Group the primes that have common deltas together
		#Members look like: 
		#Delta [(prime1,prime2)....
		#2700 [(6337, 3637), (6373, 3673), (3637, 6337), (3673, 6373)]
		#270  [(5417, 5147), (5147, 5417), (5741, 5471), (5471, 5741)]
		#

		#At this point we can clearly see patterns based on the delta betwen primes 
		#when printing the deltas and members.

		#Pull out the data and unpack 
		#Having run the numbers I can see the delta is 3330 that solves this puzzle.
		for delta, num_pairs in delta_dict.items():
			#print (delta,num_pairs)
			#if delta == 3330:
			#if len(num_pairs) == 4:
			if delta != 0 and len(num_pairs) >= 3:
				M=[ x for t in num_pairs for x in t]
				M=[ int(x) for x in M ]
				M=sorted(M)
				#print (M)
				L=[]
				for x in M:
					 if x not in L:
						 L.append(x)
				#print(L)
				if L[0] + delta == L[1] and L[1] + delta == L[2]:
					print("Winner:",L[0],L[1],L[2])
