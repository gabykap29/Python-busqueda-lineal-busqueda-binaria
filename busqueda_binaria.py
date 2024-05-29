def busqueda_binaria(lista, objetivo):
    # Inicializa los índices de la izquierda y derecha para el rango de búsqueda
    izquierda, derecha = 0, len(lista) - 1
    
    # Mientras el índice izquierdo sea menor o igual al índice derecho
    while izquierda <= derecha:
        # Calcula el índice medio del rango actual
        medio = (izquierda + derecha) // 2
        
        # Si el elemento en el índice medio es igual al objetivo, devuelve el índice medio
        if lista[medio] == objetivo:
            return medio
        
        # Si el elemento en el índice medio es menor que el objetivo, 
        # ajusta el índice izquierdo para descartar la mitad inferior del rango
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        
        # Si el elemento en el índice medio es mayor que el objetivo, 
        # ajusta el índice derecho para descartar la mitad superior del rango
        else:
            derecha = medio - 1
    
    # Si se recorre toda la lista sin encontrar el objetivo, devuelve -1
    return -1
