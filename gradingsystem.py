print ("Enter marks obtaied here in five subjects")
One = int(input())
Two = int(input())
three = int(input())
four = int(input())
five = int(input())

tot = One+Two+three+four+five
avg = tot/5

if avg>=91 and avg<100:
    print ("your grade is A1")
elif avg>=81 and avg<91:
    print (" your grade is A2")

else: 
    print ("invalid input")
