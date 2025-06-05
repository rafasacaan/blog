---
title: Invocando a Bob Dylan - crea tu primer python package
date: 2025-01-03
summary: "Crea tu propio paquete de python para obtener letras de Bob Dylan cuando más las necesites."
tags: ['tutorial', 'python', 'package' ]
draft: true
---

A veces me pasa que cuando llevo mucho tiempo escribiendo código, necesito invocar a la aleatoriedad para inyectarme una dosis de nueva energía. Se me ocurrió que Bob Dylan sería la la fuente indicada a quien recurrir, es por eso que creé esta librería de python que te devuelve texto en tu terminal con algunas frases aleatorias sacadas de sus canciones para los momentos en qué más lo necesites.

También, dicen que todo buen proyecto nace como un paquete de python. Creo que es buenísima idea crear paquetes de python para poder compartir y, sobre todo, para tratar cada cosa que construimos como un proyecto cerrado, que tiene que cumplir un objetivo. Nada peor que mucho código dado vueltas como un buen plato de tallarines. 

Para crear mi propio paquete del gran Bob quise usar la librería de python `uv`. Su promesa es que reemplaza a `pip`, `poetry` entre otras, y que administra las librerías mucho más rápido (usa Rust por debajo). Más sobre `uv` y de cómo instalarlo [acá](https://github.com/astral-sh/uv).

### Cómo empiezo?

Primero, necesitamos hacer dos cosas:
- Crear una **estructura de directorios** y archivos para nuestra librería/python package
- Crear un **ambiente de python**

Una vez instalado `uv`, podemos ir al lugar donde queremos crear nuestro paquete y escribir en la terminal:

```bash
uv init hey-bob --python 3.8 --package
```

Con esto le estoy diciendo a `uv` que quiero inicializar un proyecto que se llama `hey-bob`, que usa al menos la versión 3.8 de python, y que quiero que tenga la estructura de un paquete de python. El *tree* del proyecto se ve así:

```
    |-- README.md
    |-- pyproject.toml
    |-- src
        |-- hey-bob
            |-- __init__.py
```

Buenísima! Ahora veamos qué hay dentro de `pyproject.toml`.

```
[project]
name = "hey-bob"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "rafasacaan", email = "rafasacaan@gmail.com" }
]
requires-python = ">=3.8"
dependencies = []

[project.scripts]
hey-bob = "hey_bob:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Vemos que tenemos info sobre nuestro proyecto, así como un entry point en `hey_bob:main`. Este entry point será el comando que queremos llamar para que nos devuelvan nuestras letras de Dylan.

Ahora, nos falta crear un ambiente de python adecuado. Para esto en el root de nuestro proyecto escribimos

```
uv venv --python 3.8
```

con lo que aparecerá una nueva carpeta escondida llamada `.venv`. Podemos activar nuestro *environment* de python con 

```
source .venv/bin/activate
```

Para procesar las letras de Bob necesitaremos instalar `pandas`. Por lo tanto, instalemos esta librería usando `uv`.
```
uv add pandas
```

Hasta aquí, tenemos los huesos de nuestra librería de python. Ahora, a lo que vinimos: las letras del gran Bob.

### Quiero mis random *lyrics*
Qué mejor fuente de *datasets* que kaggle. Encontré ahí un [dataset](https://www.kaggle.com/datasets/cloudy17/bob-dylan-songs) con muchísimas letras de las canciones de Bob entre 1961 y el 2020. 

Guardé el *.csv* dentro de `src/hey-bob/data` y creé un script de python en `src/hey-bob/services.py` donde vivirán las funciones principales de la librería.

Pero antes, necesito un jupyter notebook para jugar con los datos y crear una buena función. Para esto instalemos la librería de *jupyter* en modalidad dev del ambiente de python:

```bash
uv add jupyter --dev
```

Después de jugar un rato en el jupyter notebook, creé las siguientes funciones que procesan las canciones, escoge una random, y toma algunas frases de éstas. Nada del otro mundo.

```python
import pandas as pd
import random
from pathlib import Path

def load_pickle():
	current_dir = Path(__file__).parent
	data_file = current_dir / 'data' / 'lyrics.csv'

	if not data_file.exists():
		raise FileNotFoundError(f"Could not find data file at {data_file}")
	
	return pd.read_pickle(data_file)

  

def get_random_lyrics(df, year=None):

	if year is not None:
		available_years = sorted(df['release_year'].unique())
	
		if year not in available_years:
			closest_year = min(available_years, key=lambda x: abs(x - year))
			filtered_df = df[df['release_year'] == closest_year]
		else:
			filtered_df = df[df['release_year'] == year]
	else:
		filtered_df = df
		selected_song = filtered_df.sample(n=1).iloc[0]


	# Extract song data
	song_name, song_year = selected_song.title, selected_song.release_year

	# Split into lines
	lines = [line.strip() for line in selected_song['lyrics'].split('\n') if line.strip()]

	# Select a random starting point
	start_index = random.randint(0, max(0, len(lines) - 4))

	# Get up to 4 consecutive lines
	selected_lines = lines[start_index:start_index + 4]

	# Join the lines with newlines
	selected_text = '\n'.join(selected_lines)

	return song_name, song_year, selected_text
```

Tenemos que indicarle a nuestro paquete las funciones que queremos disponibilizar. Esto lo hacemos en `__init__.py`

```python
from .services import get_random_lyrics, load_pickle
from .__main__ import main

__all__ = ['get_random_lyrics', 'load_pickle']
```

Y también crear nuestro archivo `__main__.py`.

```python
import argparse
from .services import get_random_lyrics, load_pickle

def main():
	parser = argparse.ArgumentParser(description='Get random song lyrics')
	parser.add_argument('--year', type=int, help='Specific year to get lyrics from (optional)', default=None)

	args = parser.parse_args()

	try:
		# Load the data first
		df = load_pickle()

		# Get random verse
		song_name, song_year, text = get_random_lyrics(df, year=args.year)

		# Print with formatting
		print(" ")
		print(text)
		print(f"- '{song_name}', {song_year} - Bob Dylan")
		print(" ")
		return 0
	
	except FileNotFoundError:
		print("Error: Could not find the lyrics data file.")
		return 1

	except Exception as e:
		print(f"Error: {str(e)}")
	return 1


if __name__ == '__main__':
	exit(main())
```


Ahora podemos instalar localmente nuestro paquete y probarlo.
```
uv pip install .
```


Y voilá!  Si le pido una ayuda extra a Bob, me dice:
```
My head is on straight
Most of the time
I’m strong enough not to hate
I don’t build up illusion ’til it makes me sick

- 'Most of the Time', 1989, Bob Dylan
```

### Publicando a PyPl

Para publicar nuestro paquete de python, primero utilizamos `uv build --wheel` que construye el paquete en formato wheel, optimizado para la distribución. 

Luego, con `uv pip install build twine` instalamos las herramientas necesarias: 

- *build* para crear los artefactos de distribución y 
- *twine* para la carga segura a PyPI. 

El comando `python -m build` genera tanto el archivo wheel como el source distribution (sdist) en el directorio 'dist/'. 

Finalmente, `python -m twine upload dist/*` sube todos los artefactos generados a PyPI, donde estarán disponibles para que cualquiera pueda instalarlos usando pip o uv. Durante este último paso, tendrás que autenticarte con tus credenciales de PyPI.

### Conclusión

Ya no tenemos excusa para no hacer paquetes de python. Cualquier idea, por chica que sea, puede ser empaquetada. No tiene que ser muy útil ni resolver los problemas del mundo. Es mejor sólo hacerlo, rápido y barato, y echarla al mundo. 


#### Nota:
`uv` *cachea* las operaciones del *environment*, por lo que puede ser necesario borrar el ambiente y el caché de `uv` y crearlo de nuevo para visualizar los cambios hechos en el código de fuente. Para esto typear en el terminal `rm -rf ~/.cache/uv` y `rm -rf .venv`.



