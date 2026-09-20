'''Concept: Nested Loop

Ek loop ke andar doosra loop:

for i in range(3):
    for j in range(3):
        print(j)

Outer loop ki har iteration par inner loop poora run hota hai.

🎯 Challenge

Nested for loops use karke ye pattern print karo:

1 2 3
1 2 3
1 2 3'''

for i in range(3):
    for j in range(1,4):
        print(j, end=" ")
    print()