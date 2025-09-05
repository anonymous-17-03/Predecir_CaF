import sys, signal

def handler(sig, frame):
    print("\n [!] Saliendo...\n")
    sys.exit(1)
# Ctrl + C
signal.signal(signal.SIGINT, handler)


def celsius_to_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    while True:
        user_input = input("\n [+] Introduce la temperatura en grados Celsius: ")
        if user_input.lower() == 'exit':
            print("\n [!] Saliendo del programa...")
            break
        try:
            celsius = float(user_input)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f" [*] {celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
        except ValueError:
            print(" [!] Por favor, introduce un número válido o 'exit' para salir.")

if __name__ == "__main__":
    main()
