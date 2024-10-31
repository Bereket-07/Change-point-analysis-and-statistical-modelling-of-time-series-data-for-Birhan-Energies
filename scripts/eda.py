import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def load_data(path):
    logger.info("loading the data")
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logger.error(f"error occured : {e}")
def overview_of_the_data(df):
    logger.info("overview of the data")
    try:
        print(f"the the shape of the data is {df.shape}")
        print(f"the description of the data {df.describe()}")
        print(f"the data type of the data set {df.dtypes}")
    except Exception as e:
        logger.error(f"error occured :{e}")
