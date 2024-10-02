# RSS Fetcher para EOI Calahorra

Esta aplicación de línea de comandos obtiene las últimas publicaciones del feed RSS de la Escuela Oficial de Idiomas de Calahorra.

## Uso

La aplicación tiene dos modos de uso:

1. Obtener entradas del feed RSS:

```bash
python src/main.py [número_de_entradas]
```

Si no se especifica el número de entradas, se mostrarán las 5 más recientes por defecto.

2. Comprobar cambios en la página principal:

```bash
python src/main.py check
```

Este comando compara el contenido actual de la página principal de EOI Calahorra con una versión anterior almacenada en caché, e informa si ha habido cambios.

## Desarrollo

Este proyecto está configurado para ser desarrollado en un devcontainer. Asegúrese de tener Docker y Visual Studio Code con la extensión Remote - Containers instalados.

1. Abra el proyecto en Visual Studio Code.
2. Cuando se le solicite, seleccione "Reopen in Container".
3. El contenedor se construirá y configurará automáticamente.
4. Una vez dentro del contenedor, puede ejecutar la aplicación como se describe en la sección de Uso.

## Dependencias

Las dependencias del proyecto se encuentran listadas en el archivo `requirements.txt`. Para instalarlas, ejecute:

```bash
pip install -r requirements.txt
```
