def caminos_recursivo(lab, f, c):
    global ops
    filas, cols = len(lab), len(lab[0])
    ops += 1
    if f >= filas or c >= cols:      
        return 0
    if lab[f][c] == 0:               
        return 0
    if f == filas - 1 and c == cols - 1:  
        return 1

    return caminos_recursivo(lab, f + 1, c) + caminos_recursivo(lab, f, c + 1)


def caminos_memo(lab, f, c, memo):
    global ops
    filas, cols = len(lab), len(lab[0])
    ops += 1
    if f >= filas or c >= cols:
        return 0
    if lab[f][c] == 0:
        return 0
    if f == filas - 1 and c == cols - 1:
        return 1

    if memo[f][c] != -1:             
        return memo[f][c]

    memo[f][c] = (caminos_memo(lab, f + 1, c, memo) +
                  caminos_memo(lab, f, c + 1, memo))
    return memo[f][c]



laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

memo = [[-1] * len(laberinto[0]) for _ in range(len(laberinto))]
ops = 0
print("Recursivo:", caminos_recursivo(laberinto, 0, 0))   
print(f"Operaciones: {ops}")
ops = 0
print("Memoizado:", caminos_memo(laberinto, 0, 0, memo))  
print(f"Operaciones: {ops}")