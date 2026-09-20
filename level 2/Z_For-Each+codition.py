'''Problem

List:

numbers = [12, 7, 25, 40, 9, 18, 31]

for loop use karke:

Even numbers → print "Even:" ke saath
Odd numbers → print "Odd:" ke saath
📤 Expected Output
Even: 12
Odd: 7
Odd: 25
Even: 40
Odd: 9
Even: 18
Odd: 31'''

numbers = [12,7,25,40,9,18,31]
for number in numbers:
    if number % 2 == 0:
        print("Even:",number)
    else:
        print("Odd:",number)

   