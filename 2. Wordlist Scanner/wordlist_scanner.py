import requests

def scan_url(target_url, word):
    """Escanea un sitio web buscando una palabra específica en las rutas."""

    full_url = f"{target_url.rstrip('/')}/{word}"

    try:
        response = requests.get(full_url, timeout=5)

        if response.status_code == 200:
            print(f"Encontrado: {full_url} (Código {response.status_code})")
        elif response.status_code == 403:
            print(f"Acceso denegado: {full_url} (Código {response.status_code})")
        elif response.status_code == 404:
            print(f"No encontrado: {full_url} (Código {response.status_code})")
        else:
            print(f"Estado desconocido: {full_url} (Código {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con {full_url}: {e}")

def read_wordlist(file_path):
    """
    lee un archivo de texto y devuelve una lista de palabras
    filepath: recibe la ruta de nuestra lista de palabras a escanear
    """
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print("archivo inexistente")
        return []
    except Exception as e:
        print("error:", e)
        return []

TARGET_URL = "http://127.0.0.1:8000"
WORDLIST_FILE = "wordlist.txt"    

wordlist = read_wordlist(WORDLIST_FILE)

if wordlist:
    for word in wordlist:
        scan_url(TARGET_URL, word)
else:
    print("No se pudo cargar la lista de palabras. Verifica el archivo.")
