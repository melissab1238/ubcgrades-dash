import requests
import json
import pandas as pd


def load_dataframe(input_type="api", **kwargs):
    """Loads dataframe from api or csv
    If grabbed from api, normalizes json api data into table format for dataframe.

    :param input_type: input type - 'api' or 'csv'
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * *csv_path* (``string``) --
          csv path to database
    """
    input_types = ["api", "csv"]
    if input_type not in input_types:
        raise ValueError("Invalid input type. Expected one of: %s" % sim_types)
    if input_type == "csv":
        csv_path = kwargs.get("csv_path")
        df = pd.read_csv(csv_path)
    else:
        campuses = ["UBCV", "UBCO"]
        yearSessionsResponse = requests.get(
            "https://ubcgrades.com/api/v3/yearsessions/UBCV"
        )
        yearSessions = yearSessionsResponse.json()
        data = []
        for campus in campuses:
            for yearSession in yearSessions:
                url = f"https://ubcgrades.com/api/v3/grades/{campus}/{yearSession}"
                response = requests.get(url)
                jsonData = response.json()
                data.extend(jsonData)  # TODO: add yearSession to object
        df = pd.json_normalize(data)
    return df
