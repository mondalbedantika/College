A = [10 , 20 , 30 , 40 , 50]
B = [5 , 15 , 25 , 35 , 45]
C = []

i = 0
j = 0

while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

while i < len(A):
    C.append(A[i])
    i += 1

while j < len(B):
    C.append(B[j])
    j += 1

print("Merged Array:", C)