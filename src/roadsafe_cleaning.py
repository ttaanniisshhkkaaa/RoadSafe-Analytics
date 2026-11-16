from pathlib import Path
import pandas as pd


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Clean one road-safety dataset."""

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Remove completely empty rows and columns
    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces from text values
    text_columns = df.select_dtypes(include=["object"]).columns

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    # Convert empty strings to missing values
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Convert numeric-looking columns to numeric values
    for column in df.columns:
        converted = pd.to_numeric(df[column], errors="coerce")

        if converted.notna().sum() == df[column].notna().sum():
            df[column] = converted

    return df


def clean_csv(input_file: Path, output_file: Path) -> None:
    """Read, clean, and save one CSV file."""

    df = pd.read_csv(input_file)
    cleaned_df = clean_dataframe(df)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(output_file, index=False)

    print(f"Cleaned: {input_file.name}")
    print(f"Saved to: {output_file}")
    print(f"Rows: {len(cleaned_df)}")
    print(f"Columns: {len(cleaned_df.columns)}")