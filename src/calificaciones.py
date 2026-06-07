UMBRAL_APROBADO = 75

def calcular_promedio(notas: list) -> dict:
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    
    promedio = sum(notas) / len(notas)
    
    return {
        "promedio": round(promedio, 2),
        "estado": "Aprobado" if promedio >= UMBRAL_APROBADO else "Reprobado"
    }