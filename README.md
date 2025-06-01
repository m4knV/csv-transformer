# CSV Transformer

## Overview

The CSV Transformer is a command-line tool designed to process CSV files by applying specified transformations to columns and filtering the columns based on user requirements. It supports transformations such as converting UUIDs to integers, redacting sensitive information, and converting timestamps to a standardised format.

- **Column Transformations**: Apply transformations like UUID to integer conversion, redaction of sensitive data, and timestamp conversion.
- **Column Filtering**: Retain only the specified columns in the output CSV, and also change their order
- **Configurable via CLI or Config File**: You can specify transformations and columns directly via command-line arguments or through a JSON configuration file.

## Libraries Used

- **pandas**: Used for data manipulation and analysis, particularly for reading, transforming, and writing CSV files.

- **Faker**: Generates fake data for redacting sensitive information such as names and emails.

- **python-dateutil**: Provides powerful extensions to the standard datetime module, which is used here to parse and convert timestamps.

- **argparse**: Facilitates command-line argument parsing.

## File Structure

- **main.py**: Entry point for running the CSV transformation process.
- **processor.py**: Contains the core logic for processing CSV files, including transformation and filtering functions.
- **cli.py**: Handles command-line argument parsing.
- **logger.py**: Sets up logging for the application.
- **transformers/**: Contains individual transformation functions.
- **tests/**: Unit tests for the transformation functions.

## Setup

### Local Environment Setup

1. **Clone the Repository**: Clone the repository to your local machine.

2. **Create a Virtual Environment**:

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Option 1: Using a Configuration File

#### Format:

```bash
python main.py --input <input_csv_path> --output <output_csv_path> --config-file <config_file_path>
```

To run the CSV Transformer using a configuration file, use the following command:

```bash
python main.py \
  --input ./input/user_sample.csv \
  --output ./output/output.csv \
  --config-file ./config.json
```

- `--config-file`: Path to a JSON config file containing transformation and column specifications.

### Option 2: Using Command-Line Arguments

#### Format:

```bash
python main.py --input <input_csv_path> --output <output_csv_path> --transform <transform_json> --columns <column_list>
```

To run the CSV Transformer using command-line arguments, use the following command:

```bash
python main.py \
  --input ./input/user_sample.csv \
  --output ./output/output.csv \
  --transform '{"user_id": "uuid_to_int", "manager_id": "uuid_to_int", "name": "redact", "email_address": "redact", "start_date": "convert_timestamp", "last_login": "convert_timestamp"}' \
  --columns last_login,start_date,email_address,name,manager_id,user_id

```

### Input and Output Files

- **Input File**: The CSV file you want to process. Specify its path using the `--input` argument.
- **Output File**: The processed CSV file will be saved to the path specified by the `--output` argument.

## Running Tests

To run the unit tests for the transformation functions, use the following command:

```bash
python -m unittest discover tests
```

This will automatically discover and run all test cases in the `tests/` directory.

## Dependencies

Ensure you have the required dependencies installed by running:

```bash
pip install -r requirements.txt
```

## Logging

Logs are generated during the execution of the program and are saved to `project.log`.

## Code Formatting

The project uses `black`, `isort` and `flake8` for code formatting and linting.

## Current Limitations & Future Improvements

### Limitations

- Transformations are done in-memory, meaning everything waits for full load and full transformation before writing the output.

### Future Improvements for large input files

- Use Chunked Processing
  - Instead of pd.read_csv(), use pd.read_csv(..., chunksize=N) to load and process data in chunks ex. 10.000 rows at a time.
- Append transformed chunks directly to the output CSV using mode='a' after the first chunk.
  - That way, we avoid storing transformed chunks in memory unnecessarily.
- Use a small database or file to store and maintain a shared mapping across chunks.
  - That way, we can avoid Global State in Transformers like `uuid_to_int`
- Add chunk-level logging/progress like `tqdm` to indicate progress during large file processing.
- Use Dask for parallel processing to handle large datasets.

---

## License

MIT

## Author

Nikos Makaritis
