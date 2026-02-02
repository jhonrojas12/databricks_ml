def validate_dataframe(df, target_column: str):
    columns = df.columns

    if target_column not in columns:
        raise ValueError(f"Target column '{target_column}' not found")

    if len(columns) < 2:
        raise ValueError("Dataset must have at least one feature")