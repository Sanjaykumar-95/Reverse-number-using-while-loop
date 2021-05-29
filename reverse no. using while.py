#reverse number
n=int(input('enter number'))
sum=0
temp=n
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
print ('reverse number of %d is %d'%(temp,sum))

    
#output
#enter number4567
#reverse number of 4567 is 7654
