from typing import Any, Optional
import argparse
import yaml
import requests
import matplotlib.pyplot as plt

class Analysis:
    def __init__(self, config_path):
        # Load the configuration file
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

        # Print the loaded configuration for debugging
        print("Loaded configuration:")
        print(self.config)

        # Access the keys in the configuration dictionary
        api_settings = self.config.get("api_settings", {})

        api_key = api_settings.get("api_key")
        topic = api_settings.get("topic")

        if api_key is None or topic is None:
            raise KeyError("API key or topic not found in the configuration file.")

        base_url = api_settings.get("base_url", "")

        self.url = f"{base_url}?q={topic}&api-key={api_key}"
        self.data = None

    def load_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            self.data = response.json()["response"]["docs"]
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            self.data = None
        return self.data

    def calculate_mean(self, field):
        values = [article[field] for article in self.data if field in article]
        return np.mean(values)

    def perform_regression(self, independent_var, dependent_var):
        x = [article[independent_var] for article in self.data if independent_var in article]
        y = [article[dependent_var] for article in self.data if dependent_var in article]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return {
            "slope": slope,
            "intercept": intercept,
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }

    def plot_data(self, x, y, save_path=None):
        fig, ax = plt.subplots()
        ax.plot(x, y, 'o')
        ax.set_xlabel('Independent Variable')
        ax.set_ylabel('Dependent Variable')
        if save_path:
            plt.savefig(save_path)
        plt.show()
        return fig
