from ingest import load_data
from validate import validate_data
from transform import transform_data

def run_pipeline(file_path, schema):
    df = load_data(file_path)
    validate_data(df, schema)
    df = transform_data(df)
    return df
