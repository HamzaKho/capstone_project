import pandas as pd

def save_to_db(df, table_name, engine, schema_name):
    try:
        # Save to the table
        df.to_sql(table_name, engine, if_exists='append', index=False, schema = schema_name)
        print(f"Data successfully saved to the '{table_name}' table.")
    except Exception as e:
        raise RuntimeError(f"Failed to save data to the database: {e}")