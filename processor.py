import argparse
import json
import logging

import pandas as pd

from transformers import TRANSFORM_FUNCTIONS, TransformType


def is_valid_transformation(column_data, transform_func, sample_size=5):
    # Sample a few non-null values from the column
    samples = column_data.dropna().sample(min(sample_size, len(column_data)), random_state=42)
    for value in samples:
        try:
            transform_func(value)
        except Exception:
            return False
    return True


def transform_columns(df: pd.DataFrame, transform_config: dict) -> pd.DataFrame:
    """
    Applies specified transformations to the columns of a DataFrame.

    @param df: pd.DataFrame - The DataFrame containing the data to be transformed.
    @param transform_config: dict - A dictionary where keys are column names and values are transformation names.
    @return: pd.DataFrame - The transformed DataFrame.
    """
    logging.info("Transforming columns...")
    for column, transformation in transform_config.items():
        # Check if the column exists in the DataFrame
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in CSV.")

        # Check if the transformation is supported
        if transformation not in TransformType:
            raise ValueError(f"Transformation '{transformation}' is not supported.")

        # Get the transformation function
        transform_func = TRANSFORM_FUNCTIONS.get(transformation)
        if not transform_func:
            raise ValueError(f"Transformation '{transformation}' is not supported.")

        # Dynamically check if the transformation is valid for the column
        if not is_valid_transformation(df[column], transform_func):
            raise ValueError(
                f"Transformation '{transformation}' is not valid for column '{column}' based on sampled data."
            )

        # Apply the transformation function to the column
        logging.info(f"Applying transformation function to column: {column}")
        df[column] = df[column].apply(transform_func)
    return df


def filter_columns(df: pd.DataFrame, desired_columns: list) -> pd.DataFrame:
    """
    Filters the DataFrame to only include specified columns.

    @param df: pd.DataFrame - The DataFrame to filter.
    @param desired_columns: list - A list of column names to retain in the DataFrame.
    @return: pd.DataFrame - The filtered DataFrame containing only the desired columns.

    @raises ValueError: If any of the desired columns are not present in the DataFrame.
    """
    logging.info("Filtering columns...")
    missing_cols = [col for col in desired_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"These columns are not present in the CSV file: {missing_cols}")

    return df[desired_columns]


def process_csv(args: argparse.Namespace) -> None:
    """
    Processes a CSV file by applying transformations and filtering columns, then writes the result to an output file.

    @param args: argparse.Namespace - The command-line arguments containing input and output paths,
                                      transformation configuration, and desired columns.
    @return: None
    """
    logging.info("Processing CSV file...")
    # Get the input path of the CSV file
    input_path = args.input
    # Get the output path for the CSV file
    output_path = args.output

    # Initialize transform_config and desired_columns
    transform_config = {}
    desired_columns = None

    # Check config input
    if args.config_file:
        logging.info(f"Using config file: {args.config_file}")
        # Read the config file
        with open(args.config_file, "r") as file:
            config = json.load(file)
            transform_config = config.get("transform", {})
            desired_columns = config.get("columns", None)
    else:
        logging.info(f"Using cli arguments: {args.transform}")
        # Get the transform config from the transform argument
        transform_config = json.loads(args.transform)
        # Get the desired columns from the columns argument
        desired_columns = args.columns.split(",") if args.columns else None

    # Read the input CSV file
    logging.info(f"Reading input CSV file: {input_path}")
    df = pd.read_csv(input_path)

    # Transform the CSV file columns
    df = transform_columns(df, transform_config)

    # Filter the CSV file columns
    if desired_columns:
        df = filter_columns(df, desired_columns)

    # Write the transformed CSV file to the output path
    logging.info(f"Writing transformed CSV file to: {output_path}")
    df.to_csv(output_path, index=False)

    logging.info(f"Output CSV successfully generated to: {output_path}")
    return
