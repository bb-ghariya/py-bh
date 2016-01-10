#program for arithmatic operation
print '------------------'
print 'addition .....1'
print 'subtraction...2'
print 'multiply.......3'
print 'division......4'
print '------------------'
ch=input('enter your choice : ') #
num1=input('enter value for num1 : ')
num2=input('enter value for num2 : ')

# calculate as per the choice
if ch==1: #check for addition
	sum=num1+num2
elif ch==2:
	sub=num1-num2
elif ch==3:
	mul=num1*num2
elif ch==4:
	div=num1/num2
else:
	sum=0
	
#printing the answer
if ch==1:
	print('addition of {0} and {1} is {2}'.format(num1,num2,sum))
elif ch==2:
	print('subtraction of {0} and {1} is {2}'.format(num1,num2,sub))
elif ch==3:
	print('multiplication of {0} and {1} is {2}'.format(num1,num2,mul))
elif ch==4:
	print('division of {0} and {1} is {2}'.format(num1,num2,div))
else:
	print('wrong choice so answer of {0} and {1} is {2}'.format(num1,num2,sum))
