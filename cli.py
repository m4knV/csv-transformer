import argparse


def run_cli() -> argparse.Namespace:
    """
    Parses command-line arguments for transforming a CSV file.

    @return: An argparse.Namespace object containing the parsed command-line arguments.

    Command-line arguments:
    - --input: Path to the input CSV file. This argument is required.
    - --output: Path to the output CSV file. This argument is required.
    - --transform: A JSON string specifying the transformation configuration. This argument is optional.
    - --columns: A comma-separated list of column names in the desired output order. This argument is optional.
    - --config-file: Path to a JSON config file. This argument is optional.
    """
    parser = argparse.ArgumentParser(description="Transform a CSV file")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to output CSV file")
    parser.add_argument("--transform", required=False, help="Transform config as JSON string")
    parser.add_argument(
        "--columns", required=False, help="Comma-separated column names in the desired output order"
    )
    parser.add_argument("--config-file", required=False, help="Path to a JSON config file")

    return parser.parse_args()
