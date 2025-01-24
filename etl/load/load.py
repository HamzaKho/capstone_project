import pandas as pd
from .connect_to_db import connect_to_db
from .save_to_db import save_to_db
from .keep_only_updates import keep_only_updates

def load():
    #connect to db
    engine = connect_to_db()
    # Load the data
    filename = "top_tracks_transformed.csv"
    df = pd.read_csv(f'etl/data/{filename}')
    #save to table
    only_updates = keep_only_updates(df, "hamza_capstone", engine, "student")
    if not only_updates.empty:
        save_to_db(only_updates, "hamza_capstone", engine, "student")
    else:
        print("No new or updated rows to save.")
