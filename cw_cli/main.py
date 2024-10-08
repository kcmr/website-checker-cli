#!/usr/bin/env python3
import requests
import hashlib
import json
import sys
from pathlib import Path

CONFIG_DIR = Path.home() / ".cw_cli"
CONFIG_FILE = CONFIG_DIR / "config.json"

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def get_website_hash(url):
    response = requests.get(url)
    return hashlib.md5(response.content).hexdigest()

def check_website_changes(url, stored_hash):
    current_hash = get_website_hash(url)
    if current_hash != stored_hash:
        print(f"¡El contenido de {url} ha cambiado!")
        return current_hash
    else:
        print(f"No se han detectado cambios en {url}.")
        return stored_hash

def add_url_to_config(config, url):
    if url not in config:
        config[url] = get_website_hash(url)
        save_config(config)
        print(f"Se ha añadido la URL: {url}")
    return config

def main():
    config = load_config()

    # Comprobar si se ha proporcionado una URL como argumento
    if len(sys.argv) > 1:
        url = sys.argv[1]
        config = add_url_to_config(config, url)

    if not config:
        url = input("Introduce la URL de la web que quieres comprobar: ")
        config = add_url_to_config(config, url)
    else:
        print("URLs guardadas:")
        for i, url in enumerate(config.keys(), 1):
            print(f"{i}. {url}")
        
        choice = int(input("Selecciona el número de la URL que quieres comprobar (0 para añadir una nueva): "))
        if choice == 0:
            url = input("Introduce la nueva URL: ")
            config = add_url_to_config(config, url)
        else:
            url = list(config.keys())[choice - 1]
        
        config[url] = check_website_changes(url, config[url])
        save_config(config)

if __name__ == "__main__":
    main()
