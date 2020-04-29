import os
import pandas as pd
import airtable
import geocoder

AIRTABLE_BASE_ID = "appQy6EXyIOwI0Top"
AIRTABLE_TABLE_NAME = "customers"
airtable_api = airtable.Airtable(
    AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=os.getenv('AIRTABLE_API_KEY')
)


def get_data():
    data = airtable_api.get_all()
    return pd.DataFrame(
        [
            {
                "products": record["fields"]["Product"],
                "lat": record["fields"]["Latitude"],
                "long": record["fields"]["Longitude"],
                "customer_name": record["fields"]["Customer Name"],
            }
            for record in data
            if len(record["fields"].keys()) > 0
        ]
    )
