#!/usr/bin/python3

from  other_prime_func import isprime
import matplotlib.pylab as plt

start_num=1
end_num=5000000

start_batch=start_num
increment_mon=999
next_batch=start_batch+increment_mon

checkpoint1=1000
checkpoint2=100000

counter=0
howmany_per_thous=[]
all_primes_list=[]

number=start_num
while number <= end_num:
	isitprime=isprime(number)
	if isitprime:
		all_primes_list.append(number)
		counter+=1
	if number %  checkpoint1 == 0 and number > start_num:
		print ("There are",counter,"primes from",start_batch,"to",next_batch)
		howmany_per_thous.append(counter)
		counter=0
		start_batch+=checkpoint1
		next_batch+=checkpoint1
	if number %  checkpoint2 == 0 and number > start_num:
		print ("The lowest number of primes (per thousand) from",start_num,"to",number,"is",\
	min(howmany_per_thous))
	number+=1

print ("There are",len(all_primes_list),"primes up to",end_num)

thousands=list(range(start_num+increment_mon,end_num+1,checkpoint1))
plt.scatter(thousands,howmany_per_thous,s=40)
plt.title("Number of Primes per 1000")
#plt.xlabel("Thousands")
plt.ylabel("Number of Primes")
plt.axis([start_num, end_num, 0, 200])
plt.show()
