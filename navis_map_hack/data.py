import os
import pandas as pd
import airtable
import geocoder

AIRTABLE_BASE_ID = "appQy6EXyIOwI0Top"
AIRTABLE_TABLE_NAME = "customers"


def get_airtable_api():
    return airtable.Airtable(
        AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=os.getenv("AIRTABLE_API_KEY")
    )


def get_lat_long(address):
    g = geocoder.osm(address)
    return g.latlng


def process_airtable_record(record):
    lat = None
    lng = None

    if "Address" in record:
        lat, lng = get_lat_long(record["Address"])
    else:
        lat = record["fields"]["Latitude"]
        lng = record["fields"]["Longitude"]

    return {
        "products": record["fields"]["Product"],
        "lat": lat,
        "long": lng,
        "customer_name": record["fields"]["Customer Name"],
    }


def get_data():
    airtable_api = get_airtable_api()
    data = airtable_api.get_all()
    return pd.DataFrame(
        [
            process_airtable_record(record)
            for record in data
            if len(record["fields"].keys()) > 0
        ]
    )
