from src.mlproject.logger import logging  # use your custom logger
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("The execution has started")
    print("✅ Script executed. Check the logs folder.")

    try:
        # Initialize and run data ingestion
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception occurred during execution")
        raise CustomException(e, sys)