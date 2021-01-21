A = [ [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0] ]

"""
print(A[0][0])


print(A)


print(A[0][0],A[0][1],A[0][2])

print(A[1][0],A[1][1],A[1][2])

print(A[2][0],A[2][1],A[2][2])
"""

br_kolona = len(A)
br_vrsta = len(A[0])

i = 0
j = 0

while i < br_kolona:
    while j < br_vrsta:
        print(A[i][j], end=' ') # A[i][j]=input('Unesite element sa koordinatama',i,j)
        j += 1
    print()
    j = 0 
    i += 1
