from .transformations import remove_features_from_track_name, add_features_column, remove_features_from_artist_name
import pandas as pd

def transform():
    filename_input = 'top_tracks.csv'
    filename_output = 'top_tracks_transformed.csv'
    df = pd.read_csv(f'etl/data/{filename_input}')
    #remove features from track_name
    df = remove_features_from_track_name(df)
    #add features column
    df = add_features_column(df)
    #remove features from artist_name
    df = remove_features_from_artist_name(df)
    #save to csv
    df.to_csv(f'etl/data/{filename_output}', index=False)
