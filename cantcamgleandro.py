def imprimir(mat):
    for x in mat:
        print(x)
    print()
    

def labcam_memo(f, c, N, M, obstaculos, tabla):
    if f >= N or c >= M or obstaculos[f][c]:
        return 0
    
    if f == N - 1 and c == M - 1:
        return 1
    
    if tabla[f][c] != -1:
        return tabla[f][c]
    
    caminos_derecha = labcam_memo(f, c + 1, N, M, obstaculos, tabla)
    caminos_abajo = labcam_memo(f + 1, c, N, M, obstaculos, tabla)
    
    tabla[f][c] = caminos_derecha + caminos_abajo
    #imprimir(tabla)
    return tabla[f][c]

# --- PROGRAMA PRINCIPAL (MAIN) ---
if __name__ == "__main__":
    # Definir dimensiones del laberinto (por ejemplo, 6x6)
    N, M = 8, 8
    
    """
    # Matriz de obstáculos (False = camino libre, True = casilla bloqueada)
    obstaculos = [[False * M for _ in range(M)] for _ in range(N)]
    
    # Simulando algunos obstáculos (casillas del laberinto)
    obstaculos[1][2] = True
    obstaculos[2][4] = True
    obstaculos[4][1] = True
    """
    obstaculos = [
    [False, False, False, False, False, False, False, False],
    [False, False, True, False, False, False, True, False],
    [False, False, False, False, True, False, False, False],
    [True, False, True, False, False, True, False, False],
    [False, False, True, False, False, False, False, False],
    [False, False, False, True, True, False, True, False],
    [False, True, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False]
]

    tabla = [[-1 for _ in range(M)] for _ in range(N)]
    
    # Posición inicial (0, 0)
    inicio_f, inicio_c = 0, 0
    
    # Ejecutar la función
    total_caminos = labcam_memo(inicio_f, inicio_c, N, M, obstaculos, tabla)
    print(f"La cantidad total de caminos posibles es: {total_caminos}")
    imprimir(tabla)