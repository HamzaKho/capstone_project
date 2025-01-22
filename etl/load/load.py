import pandas as pd
from .connect_to_db import connect_to_db
from .save_to_db import save_to_db

def load():
    #connect to db
    engine = connect_to_db()
    # Load the data
    filename = "top_tracks_transformed.csv"
    df = pd.read_csv(f'etl/data/{filename}')
    #save to table
    save_to_db(df, "hamza_capstone", engine, "student")
