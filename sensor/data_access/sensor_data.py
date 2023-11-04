from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException
import sys
from typing import Optional
import pandas as pd
import numpy as np
import json

class SensorData:
    """
    This class helps to export data from mongodb as pandas dataframe
    """
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SensorException(e, sys)
        
    def save_csv_file(self, filepath, collection_name: str, database_name: Optional[str] = None):
        try:
            dataframe = pd.read_csv(filepath)
            dataframe.reset_index(drop=True, inplace=True)
            records = list(json.loads(dataframe.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise SensorException(e, sys)
        
    def collection_as_dataframe(self, collection_name:str, database_name:Optional[str] = None) -> pd.DataFrame:
        """
        export entie collection as dataframe

        Returns:
            pd.DataFrame: collection as dataframe
        """
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.tolist():
                df = df.drop(columns=['_id'], axis=1)
            
            df.replace({"na": np.nan}, inplace=True)

            return df
        except Exception as e:
            raise SensorException(e, sys)
        