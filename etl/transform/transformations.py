def remove_features_from_track_name(df):
    df['track_name'] = df['track_name'].str.replace(r'\s*\(.*?\)|\s*\[.*?\]', '', regex=True)
    return df

def add_features_column(df):
    df['features'] = df['artist_name'].apply(lambda x: x.split(', ')[1:] if ',' in x else [])
    return df

def remove_features_from_artist_name(df):
    df['artist_name'] = df['artist_name'].apply(lambda x: x.split(',')[0])
    return df