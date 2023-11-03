import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

"""
Common constant variables for training pipeline
"""

TARGET_COLUMN = 'class'
PIPELINE_NAME = 'sensor'
ARTIFACT_DIR = 'artifact'
FILE_NAME = 'sensor.csv'

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
MODEL_FILE_NAME = 'model.pkl'
SCHEMA_FILE_PATH = os.path.join('config', 'schema.yaml')
SCHEMA_DROP_COLS = 'drop_columns'

"""
Data Ingestion related constants
"""

DATA_INGETION_COLLECTION_NAME: str = 'sensor'
DATA_INGETION_DIR_NAME: str = 'data_ingetion'
DATA_INGETION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

