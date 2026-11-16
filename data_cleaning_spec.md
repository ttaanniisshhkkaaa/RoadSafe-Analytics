# Data Cleaning Specification

## Common transformations

- Column names are trimmed, lower-cased, and converted to `snake_case`.
- Common missing-value markers such as blank strings, `N/A`, `NULL`, `-`, and `?` are converted to missing values.
- Leading and trailing whitespace is removed from text fields.
- Completely empty rows and columns are removed.
- Exact duplicate rows are removed.
- Numeric-looking columns are converted to numeric data types where safe.

## Dataset-specific transformations

### Collisions

- Collision records are deduplicated using `accident_index` when available.
- Collision identifiers and essential road, weather, location, and severity fields are retained.

### Vehicles

- Vehicle records are deduplicated using `accident_index` and `vehicle_reference` when available.
- Vehicle characteristics and driver-related fields are retained.

### Casualties

- Casualty records are deduplicated using `accident_index`, `vehicle_reference`, and `casualty_reference` when available.
- Age, gender, injury severity, and casualty characteristics are retained.

## Output format

Cleaned datasets are stored as Parquet files because Parquet preserves column types and is efficient for analytical work.

