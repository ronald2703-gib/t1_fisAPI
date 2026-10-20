import requests

BASE_URL = "http://127.0.0.1:8000/trainees"

def mostrar_menu():
    print("\n--- GESTIÓN DE APRENDICES (CONSOLA) ---")
    print("1. Registrar nuevo aprendiz")
    print("2. Listar todos los aprendices")
    print("3. Buscar aprendiz por ID")
    print("4. Actualizar aprendiz")
    print("5. Eliminar aprendiz")
    print("6. Salir")

def registrar_aprendiz():
    print("\n--- Registrar Aprendiz ---")
    document = input("Documento: ")
    name = input("Nombre: ")
    firstname = input("Primer nombre: ")
    email = input("Email: ")
    
    while True:
        try:
            age = int(input("Edad: "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero válido para la edad.")
            
    program = input("Programa: ")
    
    while True:
        try:
            record_number = int(input("Número de ficha: "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero válido para la ficha.")

    payload = {
        "document": document,
        "name": name,
        "firstname": firstname,
        "email": email,
        "age": age,
        "program": program,
        "record_number": record_number
    }

    try:
        response = requests.post(BASE_URL, json=payload)
        if response.status_code in [200, 201]:
            print("¡Aprendiz registrado con éxito!")
            print(response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print("Error al conectar con la API:", e)

def listar_aprendices():
    print("\n--- Lista de Aprendices ---")
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            aprendices = response.json()
            for item in aprendices:
                print(item)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print("Error al conectar con la API:", e)

def buscar_aprendiz():
    print("\n--- Buscar Aprendiz por ID ---")
    aprendiz_id = input("Ingrese el ID del aprendiz: ")
    try:
        response = requests.get(f"{BASE_URL}/{aprendiz_id}")
        if response.status_code == 200:
            print("Aprendiz encontrado:")
            print(response.json())
        else:
            print("Aprendiz no encontrado o error:", response.status_code)
    except Exception as e:
        print("Error al conectar con la API:", e)

def actualizar_aprendiz():
    print("\n--- Actualizar Aprendiz ---")
    aprendiz_id = input("Ingrese el ID del aprendiz a actualizar: ")
    
    print("Deja el campo vacío si no deseas actualizarlo.")
    document = input("Nuevo Documento: ")
    name = input("Nuevo Nombre: ")
    firstname = input("Nuevo Primer Nombre: ")
    lastname = input("Nuevo Apellido: ")
    email = input("Nuevo Email: ")
    age_str = input("Nueva Edad: ")
    program = input("Nuevo Programa: ")
    record_str = input("Nuevo Número de ficha: ")

    payload = {}
    if document: payload["document"] = document
    if name: payload["name"] = name
    if firstname: payload["firstname"] = firstname
    if lastname: payload["lastname"] = lastname
    if email: payload["email"] = email
    if age_str: payload["age"] = int(age_str)
    if program: payload["program"] = program
    if record_str: payload["record_number"] = int(record_str)

    try:
        response = requests.put(f"{BASE_URL}/{aprendiz_id}", json=payload)
        if response.status_code == 200:
            print("¡Aprendiz actualizado con éxito!")
            print(response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print("Error al conectar con la API:", e)

def eliminar_aprendiz():
    print("\n--- Eliminar Aprendiz ---")
    aprendiz_id = input("Ingrese el ID del aprendiz a eliminar: ")
    try:
        response = requests.delete(f"{BASE_URL}/{aprendiz_id}")
        if response.status_code in [200, 204]:
            print("Aprendiz eliminado exitosamente.")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print("Error al conectar con la API:", e)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_aprendiz()
        elif opcion == "2":
            listar_aprendices()
        elif opcion == "3":
            buscar_aprendiz()
        elif opcion == "4":
            actualizar_aprendiz()
        elif opcion == "5":
            eliminar_aprendiz()
        elif opcion == "6":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()