#print ("Hola Usuario,cual es tu nombre?")
#nombre = input("Por favor, ingresa tu nombre: ")
#print("Bienvenido al digimundo:", nombre)
#edad = input("cual es tu edad?  ")
#print("ya veo tu edad es:", edad)
#print ("conoces lo que es un digimon?")
#digiknow = input("(si/no)").strip().lower()
#if digiknow in ["si","si"]:
 #   print("genial,procederemos a escoger un compañero")

#elif digiknow == "no":  
 #   print("Los Digimon son criaturas principalmente compuestas de datos que yacen en un espacio digital conocido como el Digimundo. Existen diferentes servidores, por lo que existen diferentes mundos Digimon con cada uno su temática diferente.")      

# Diccionario con la lista de Digimon y sus evoluciones
digimons = {
    "Terriermon": [
        {"nombre": "Terriermon", "nivel": "Child", "estadisticas": {"ATK": 50, "DEF": 40, "Velocidad": 45, "ATK SPE": 55}, "nivel_evolutivo": "Gargomon"},
        {"nombre": "Gargomon", "nivel": "Champion", "estadisticas": {"ATK": 80, "DEF": 60, "Velocidad": 70, "ATK SPE": 85}, "nivel_evolutivo": "Rapidmon (Golden Armor)"},
        {"nombre": "Rapidmon (Golden Armor)", "nivel": "Armor", "estadisticas": {"ATK": 90, "DEF": 70, "Velocidad": 95, "ATK SPE": 100}, "nivel_evolutivo": "Rapidmon"},
        {"nombre": "Rapidmon", "nivel": "Ultimate", "estadisticas": {"ATK": 95, "DEF": 75, "Velocidad": 100, "ATK SPE": 105}, "nivel_evolutivo": "Rapidmon X"},
        {"nombre": "Rapidmon X", "nivel": "Mega", "estadisticas": {"ATK": 100, "DEF": 80, "Velocidad": 110, "ATK SPE": 115}, "nivel_evolutivo": "MegaGargomon"},
        {"nombre": "MegaGargomon", "nivel": "Mega", "estadisticas": {"ATK": 110, "DEF": 90, "Velocidad": 100, "ATK SPE": 120}, "nivel_evolutivo": None}
    ],
    "Renamon": [
        {"nombre": "Renamon", "nivel": "Child", "estadisticas": {"ATK": 55, "DEF": 35, "Velocidad": 50, "ATK SPE": 60}, "nivel_evolutivo": "Kyubimon"},
        {"nombre": "Kyubimon", "nivel": "Champion", "estadisticas": {"ATK": 75, "DEF": 50, "Velocidad": 80, "ATK SPE": 90}, "nivel_evolutivo": "Taomon"},
        {"nombre": "Taomon", "nivel": "Ultimate", "estadisticas": {"ATK": 90, "DEF": 65, "Velocidad": 85, "ATK SPE": 100}, "nivel_evolutivo": "Sakuyamon"},
        {"nombre": "Sakuyamon", "nivel": "Mega", "estadisticas": {"ATK": 110, "DEF": 80, "Velocidad": 95, "ATK SPE": 120}, "nivel_evolutivo": None}
    ],
    "Guilmon": [
        {"nombre": "Guilmon", "nivel": "Child", "estadisticas": {"ATK": 60, "DEF": 45, "Velocidad": 40, "ATK SPE": 50}, "nivel_evolutivo": "Growlmon"},
        {"nombre": "Growlmon", "nivel": "Champion", "estadisticas": {"ATK": 85, "DEF": 65, "Velocidad": 55, "ATK SPE": 75}, "nivel_evolutivo": "WarGrowlmon"},
        {"nombre": "WarGrowlmon", "nivel": "Ultimate", "estadisticas": {"ATK": 100, "DEF": 80, "Velocidad": 70, "ATK SPE": 90}, "nivel_evolutivo": "Gallantmon"},
        {"nombre": "Gallantmon", "nivel": "Mega", "estadisticas": {"ATK": 120, "DEF": 95, "Velocidad": 85, "ATK SPE": 130}, "nivel_evolutivo": "Gallantmon Crimson Mode"},
        {"nombre": "Gallantmon Crimson Mode", "nivel": "Mega", "estadisticas": {"ATK": 140, "DEF": 110, "Velocidad": 100, "ATK SPE": 150}, "nivel_evolutivo": "Gallantmon X"},
        {"nombre": "Gallantmon X", "nivel": "Mega", "estadisticas": {"ATK": 150, "DEF": 120, "Velocidad": 110, "ATK SPE": 160}, "nivel_evolutivo": None}
    ],
    "Impmon": [
        {"nombre": "Impmon", "nivel": "Child", "estadisticas": {"ATK": 50, "DEF": 30, "Velocidad": 60, "ATK SPE": 70}, "nivel_evolutivo": "Wizardmon"},
        {"nombre": "Wizardmon", "nivel": "Champion", "estadisticas": {"ATK": 70, "DEF": 45, "Velocidad": 80, "ATK SPE": 85}, "nivel_evolutivo": "Baalmon"},
        {"nombre": "Baalmon", "nivel": "Ultimate", "estadisticas": {"ATK": 90, "DEF": 60, "Velocidad": 90, "ATK SPE": 100}, "nivel_evolutivo": "Beelzemon"},
        {"nombre": "Beelzemon", "nivel": "Mega", "estadisticas": {"ATK": 120, "DEF": 85, "Velocidad": 100, "ATK SPE": 130}, "nivel_evolutivo": "Beelzemon Blast Mode"},
        {"nombre": "Beelzemon Blast Mode", "nivel": "Mega", "estadisticas": {"ATK": 140, "DEF": 100, "Velocidad": 110, "ATK SPE": 150}, "nivel_evolutivo": "Beelzemon X"},
        {"nombre": "Beelzemon X", "nivel": "Mega", "estadisticas": {"ATK": 150, "DEF": 120, "Velocidad": 115, "ATK SPE": 160}, "nivel_evolutivo": None}
    ]
}

# Función para mostrar evoluciones
def mostrar_evoluciones(digimon):
    print(f"\nEvoluciones de {digimon}:")
    for evolucion in digimons[digimon]:
        print(f"{evolucion['nombre']} - Nivel: {evolucion['nivel']}, ATK: {evolucion['estadisticas']['ATK']}, ATK SPE: {evolucion['estadisticas']['ATK SPE']}")

# Función para obtener una respuesta válida del usuario para la selección
def obtener_seleccion():
    while True:
        seleccion = input("\nElige el número de tu compañero (1-4): ").strip()
        if seleccion in ["1", "2", "3", "4"]:
            return seleccion
        else:
            print("Sin selección, selecciona un número válido.")

# Función para gestionar la selección y confirmación del Digimon
def seleccionar_digimon():
    seleccion_valida = False
    while not seleccion_valida:
        print("\nEstos son los Digimons que puedes elegir:")
        print("1. Terriermon")
        print("2. Renamon")
        print("3. Guilmon")
        print("4. Impmon")

        seleccion = obtener_seleccion()

        if seleccion == "1":
            mostrar_evoluciones("Terriermon")
        elif seleccion == "2":
            mostrar_evoluciones("Renamon")
        elif seleccion == "3":
            mostrar_evoluciones("Guilmon")
        elif seleccion == "4":
            mostrar_evoluciones("Impmon")

        while True:
            confirmar = input("\n¿Deseas confirmar tu selección? (sí/no): ").strip().lower()
            if confirmar == "si":
                print("¡Excelente! Has confirmado tu selección.")
                print("DIGITAL GATE OPEN! TU AVENTURA COMIENZA")
                seleccion_valida = True  # Selección confirmada
                break  # Sale del ciclo de confirmación
            elif confirmar == "no":
                print("Has decidido cambiar de opinión, selecciona nuevamente un Digimon.")
                break  # Vuelve a elegir el Digimon
            else:
                print("Por favor, responde con 'si' o 'no'.")
    return True  # Retorna True solo cuando se confirma la selección

# Función principal para gestionar la interacción con el usuario
def main():
    print("Hola Usuario, ¿cuál es tu nombre?")
    nombre = input("Por favor, ingresa tu nombre: ")
    print("Bienvenido al digimundo:", nombre)

    edad = input("¿Cuál es tu edad? ")
    print("Ya veo, tu edad es:", edad)

    print("¿Conoces lo que es un Digimon?")
    digiknow = input("(sí/no): ").strip().lower()

    if digiknow in ["si", "si"]:
        print("¡Genial! Procederemos a escoger un compañero.")
        seleccion_valida = seleccionar_digimon()

    elif digiknow == "no":
        print("Los Digimon son criaturas principalmente compuestas de datos que yacen en un espacio digital conocido como el Digimundo. Existen diferentes servidores, por lo que existen diferentes mundos Digimon con cada uno su temática diferente.")
        
        # Después de la explicación, permite escoger un Digimon
        seleccion_valida = seleccionar_digimon()

    if seleccion_valida:
        print("Gracias por tu selección. ¡Que disfrutes tu aventura en el Digimundo!")

# Llamada a la función principal
main()
