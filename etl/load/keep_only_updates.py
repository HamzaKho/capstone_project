import pandas as pd

def keep_only_updates(new_df, table_name, engine, schema_name):
    try:
        query = f"SELECT * FROM {schema_name}.{table_name}"
        current_df = pd.read_sql(query, engine)
        concat_df = pd.concat([current_df, new_df], axis=0)
        concat_df.drop_duplicates(subset=['track_id', 'region'], keep=False, inplace=True)
        return concat_df
    except Exception as e:
        raise RuntimeError(f"Failed to compare new data with the current database data: {e}")