import feedparser
import sys
from datetime import datetime
import requests
import hashlib
import os

RSS_URL = "https://eoicalahorra.es/feed/"
WEBSITE_URL = "https://eoicalahorra.es/"
CACHE_FILE = "website_cache.txt"

def fetch_rss_feed(url, num_entries=5):
    feed = feedparser.parse(url)
    
    print(f"Últimas {num_entries} publicaciones de {feed.feed.title}:\n")
    
    for entry in feed.entries[:num_entries]:
        print(f"Título: {entry.title}")
        publication_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
        formatted_date = publication_date.strftime("%d de %B de %Y a las %H:%M")
        print(f"Fecha: {formatted_date}")
        print(f"Enlace: {entry.link}")
        print("\n---\n")

def check_website_changes():
    response = requests.get(WEBSITE_URL)
    current_content = response.text
    current_hash = hashlib.md5(current_content.encode()).hexdigest()

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cached_hash = f.read().strip()
        
        if current_hash != cached_hash:
            print("¡El contenido de la página principal ha cambiado!")
        else:
            print("No se han detectado cambios en la página principal.")
    else:
        print("Primera ejecución: se creará el archivo de caché.")

    with open(CACHE_FILE, 'w') as f:
        f.write(current_hash)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        check_website_changes()
    else:
        num_entries = 5  # Valor por defecto
        
        if len(sys.argv) > 1:
            try:
                num_entries = int(sys.argv[1])
            except ValueError:
                print("Por favor, introduce un número válido de entradas.")
                sys.exit(1)
        
        fetch_rss_feed(RSS_URL, num_entries)
