def validate_data(df, schema):
    required_cols = schema.get("required", [])
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
