# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for X in [0,1]:
    for Y in [0,1]:
        for Z in [0,1]:
            left = not (X or Y or Z)
            right = not X and not Y and not Z
            result = left == right
            print(X, Y, Z, 'result:', result)


