from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData
import sys, os
from pandas import DataFrame
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)
        
    def export_data_into_feature_store(self) -> DataFrame:
        """
        Export mongo db collection record as dataframe into feature
        """
        try:
            logging.info('exporting data from mongodb to feature store')
            sensor_data = SensorData()
            dataframe = sensor_data.collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # Creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info('Data exported from mongodb to feature store')
            return dataframe
        except Exception as e:
            raise SensorException(e, sys)
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        """
        Feature store dataset is split into train and test data
        """
        try:
            logging.info('Performing train test split on dataframe')
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio
            )
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info('Exporting Train and test data to file')
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.test_file_path, index=False, header=True
            )
            logging.info('Exported Train and test data')

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            data_ingstion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path, test_file_path=self.data_ingestion_config.test_file_path)
            return data_ingstion_artifact
        except Exception as e:
            raise SensorException(e, sys)
