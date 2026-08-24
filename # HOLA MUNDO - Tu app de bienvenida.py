# HOLA MUNDO - Tu app de bienvenida

def saludo():
    return "COMO ESTÁS HOY?"

if __name__ == "__main__":
    print("Bienvenido a la casa digital...")
    
    if input("¡Hola!, quién eres?"):
        print(f"¡Interesante! {saludo()}")
        input("\nPresiona Enter para continuar...")
