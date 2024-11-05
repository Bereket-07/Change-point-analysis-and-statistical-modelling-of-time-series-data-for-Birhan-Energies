import pandas as pd
import logging
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def price_trend_seasonality(df):
    logger.info("Using ARIMA to capture baseline trends and seasonal patterns.")
    try:
        # Ensure the Date index is in datetime format
        df.index = pd.to_datetime(df.index)

        # Fit ARIMA model
        logger.info("Fitting ARIMA model")
        arima_model = ARIMA(df['Price'], order=(1, 1, 1))
        arima_result = arima_model.fit()

        # Specify forecast start dynamically
        forecast_start = df.index.min()

        # Generate forecast
        logger.info("Generating ARIMA forecast")
        df['ARIMA_Forecast'] = arima_result.predict(start=forecast_start, dynamic=False)

        # Plot the results
        logger.info("Plotting forecast")
        df[['Price', 'ARIMA_Forecast']].plot(figsize=(10, 6), title="ARIMA Model - Price vs Forecast")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.show()

    except Exception as e:
        logger.error(f"Error during ARIMA forecasting: {e}")

def garch_model_for_volatility(df):
    logger.info("GARCH model to capture volatility especially during events and high-uncertinity periods")
    try:
        logger.info("fit the arch model")
        garch_model = arch_model(df['Price_Returns'].dropna(),vol='GARCH' , p=1,q=1)
        garch_result = garch_model.fit()
        logger.info("plot volatility")
        garch_volatility = garch_result.conditional_volatility
        plt.figure(figsize=(10,6))
        plt.plot(garch_volatility)
        plt.title("GARCH Conditional volatility ")
        plt.show()
    except Exception as e:
        logger.error(f"error occured while making the garch model for volatility {e}")


def models_for_regimes_changes(df):
    logger.info("the markov swir=tching ARMIA model for identifing different 'regimes' or periods such as high vs low volatility phases")
    try:
        logger.info("fit markov switiching model")
        markov_model = MarkovSwitchingDynamicRegression(df['Price'] , k_regimes=2)
        markov_result = markov_model.fit()
        markov_result.plot_diagnostics()
        plt.show()
    except Exception as e:
        logger.error(f"error occured while performing the regimes changes {e}")

        


        
