from cli import run_cli
from logger import setup_logger
from processor import process_csv

if __name__ == "__main__":
    setup_logger()
    process_csv(run_cli())
