
#Leap year Program

n = input('Which year do you want to know whether is leap? :')

def leapyear(n):

	if n % 400 == 0 :
		return True
	if n % 100 == 0 :
		return True
	if n % 4 == 0 :
		return True 
	else :
		return False

print leapyear(n)
