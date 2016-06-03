# Any number that is (2^a)*(5^b) has a finite decimal approximation, and cycle of 1
# Any number that is composite has a cycle as long as its prime factors??

def fin_exp(number):

	#this is true if the number is evenly divisble by 2
	while (number/2.)==(number//2):
		number = number//2

	#the same for 5
	while (number/5.)==(number//5):
		number = number//5

	if number==1:
		return True
    
	else:
		return False

	
def exp_length():

	for num in xrange(1,11):
		
		if(fin_exp(num) is False):
			print num, "Good"	

exp_length()
