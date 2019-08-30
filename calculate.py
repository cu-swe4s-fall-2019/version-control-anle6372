import math_lib as ml

A = float(input("Pick an number, A: "))

B = float(input("Pick another number, B: "))

sum = ml.add(A, B)
ans = ml.div(sum, A)

print("The value of A summed with B divided by A equals: " + str(ans))
