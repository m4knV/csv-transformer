import logging


def setup_logger():
    """Set up the logger"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("project.log"), logging.StreamHandler()],
    )
