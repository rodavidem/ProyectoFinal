import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal.settings')
django.setup()

# Importa el modelo Disco
from ProyectoFinal.models import Disco

# Lista de discos a cargar
discos = [
    {"interprete": "The Harmonic Waves", "titulo": "Echoes of Time", "genero": "Ambient"},
    {"interprete": "Eclipse Collective", "titulo": "Night Shadows", "genero": "Electronic"},
    {"interprete": "Electric Echoes", "titulo": "Neon Vibes", "genero": "Pop"},
    {"interprete": "Jazz Masters", "titulo": "Blue Melodies", "genero": "Jazz"},
    {"interprete": "Digital Frequencies", "titulo": "Neon Pulse", "genero": "Techno"},
    {"interprete": "Salsa Groove", "titulo": "Tropical Rhythms", "genero": "Salsa"},
]

# Cargar cada disco en la base de datos
for disco in discos:
    Disco.objects.create(**disco)