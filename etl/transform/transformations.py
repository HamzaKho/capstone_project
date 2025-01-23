import pandas as pd
def remove_features_from_track_name(df):
    df['track_name'] = df['track_name'].str.replace(r'\s*\(.*?\)|\s*\[.*?\]', '', regex=True)
    return df

def add_features_column(df):
    df['features'] = df['artist_name'].apply(lambda x: x.split(', ')[1:] if ',' in x else [])
    return df

def remove_features_from_artist_name(df):
    df['artist_name'] = df['artist_name'].apply(lambda x: x.split(',')[0])
    return df

def add_languages_column(df):
    country_language_mapping = {
        "UK": "English",
        "USA": "English",
        "Brazil": "Portuguese",
        "Spain": "Spanish",
        "Mexico": "Spanish",
        "Portugal": "Portuguese",
        "Australia": "English",
        "Canada": "English, French",
        "France": "French",
        "Germany": "German",
        "Italy": "Italian",
        "Japan": "Japanese",
        "China": "Mandarin",
        "India": "Hindi",
        "Russia": "Russian",
        "Argentina": "Spanish",
        "Chile": "Spanish",
        "Colombia": "Spanish",
        "South Korea": "Korean",
        "Saudi Arabia": "Arabic",
        "Egypt": "Arabic",
        "Turkey": "Turkish",
    }

    df['languages'] = df['region'].map(country_language_mapping).fillna('Unknown')
    return df