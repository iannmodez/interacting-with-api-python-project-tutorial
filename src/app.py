import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()



# 1) Connect to the database here using the SQLAlchemy's create_engine function

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function

from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Corrige la siguiente línea, cambia 'con' a 'sp'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

artist_id = "5K4W6rqBFWDnAN6FQUkS6x"

response = sp.artist_top_tracks("3TVXtAsR1Inumwj472S9r4")
if response:
    # Mantén el objeto "tracks" de la respuesta
    tracks = response["tracks"]
    # Selecciona, para cada canción, los datos que te interesan y descarta el resto
    tracks = [{k: (v / (1000 * 60)) % 60 if k == "duration_ms" else v for k, v in track.items() if
               k in ["name", "popularity", "duration_ms"]} for track in tracks]

import pandas as pd

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(["popularity"], inplace=True)

print(tracks_df.head(3))

import matplotlib.pyplot as plt

# Cambia la visualización a Matplotlib
plt.scatter(tracks_df["popularity"], tracks_df["duration_ms"])
plt.xlabel("Popularity")
plt.ylabel("Duration (ms)")
plt.title("Popularity vs Duration")
plt.savefig("scatter_plot.png")
plt.show()



