import pandas as pd
import logging
import seaborn as sns
import matplotlib.pyplot as plt

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
        print(f"the data set contain this null values {df.isnull().sum()}")
    except Exception as e:
        logger.error(f"error occured :{e}")
def combine_and_explore(df_oil, df_OECD, df_CPI_U, df_unep):
    logger.info("Combining and performing an exploratory analysis of the combined data")
    try:
        # Ensure Price_Returns column exists
        if 'Price_Returns' not in df_oil.columns:
            df_oil['Price_Returns'] = df_oil['Price'].pct_change()
        
        # Convert all data to monthly frequency if not already
        df_oil = df_oil.resample('M').mean()
        df_OECD = df_OECD.resample('M').mean()
        df_CPI_U = df_CPI_U.resample('M').mean()
        df_unep = df_unep.resample('M').mean()
        
        # Align date ranges across all DataFrames (1987 onward)
        start_date = max(df_oil.index.min(), df_OECD.index.min(), df_CPI_U.index.min(), df_unep.index.min())
        end_date = min(df_oil.index.max(), df_OECD.index.max(), df_CPI_U.index.max(), df_unep.index.max())
        
        # Filter all DataFrames to the common date range
        df_oil = df_oil.loc[start_date:end_date]
        df_OECD = df_OECD.loc[start_date:end_date]
        df_CPI_U = df_CPI_U.loc[start_date:end_date]
        df_unep = df_unep.loc[start_date:end_date]
        
        # Combine the datasets
        combined_df = pd.concat([df_oil['Price_Returns'], df_OECD, df_CPI_U, df_unep], axis=1)
        
        # Fill NaN values with forward fill
        combined_df.fillna(method='ffill', inplace=True)

        sns.heatmap(combined_df.corr(), annot=True, cmap="coolwarm")
        plt.show()
        
        return combined_df
    except Exception as e:
        logger.error(f"An error occurred while combining and performing the exploratory analysis: {e}")
        return None

    
