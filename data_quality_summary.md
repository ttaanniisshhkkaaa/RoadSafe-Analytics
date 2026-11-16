# Data Quality Summary

## Cleaning actions completed

The Stage 4 cleaning pipeline standardises column names, handles common missing-value markers, removes empty records, removes duplicates, trims text values, and converts numeric-looking columns to numeric types.

## Output datasets

- `collisions_clean.parquet`
- `vehicles_clean.parquet`
- `casualties_clean.parquet`

## Validation

Automated tests check column-name standardisation, duplicate removal, missing-value handling, whitespace removal, required columns, identifier uniqueness, and relationship-key completeness.

## Limitations

- Dataset-specific coded values must be interpreted using the official STATS19 data dictionary.
- Missing geographical values may remain where the source data does not provide a valid location.
- Cleaning does not infer values that are absent from the original data.

