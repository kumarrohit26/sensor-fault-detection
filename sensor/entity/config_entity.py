from sensor.constant import training_pipeline
import os
from datetime import datetime

class TrainingPipeLineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime('%Y_%m_%d_%H_%M_%S')
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipeLineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGETION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGETION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
        )
        self.test_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = training_pipeline.DATA_INGETION_COLLECTION_NAME