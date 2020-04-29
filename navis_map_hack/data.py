import os
import pandas as pd
import airtable
import geocoder

AIRTABLE_BASE_ID = "appQy6EXyIOwI0Top"
CUSTOMERS = "customers"
PRODUCTS = "products"


def get_airtable_api(table_name):
    return airtable.Airtable(
        AIRTABLE_BASE_ID, table_name, api_key=os.getenv("AIRTABLE_API_KEY")
    )


def get_lat_long(address):
    g = geocoder.osm(address)
    return g.latlng


def process_customer_record(record):
    lat = None
    lng = None

    if "Address" in record["fields"]:
        lat, lng = get_lat_long(record["fields"]["Address"])
    else:
        lat = record["fields"]["Latitude"]
        lng = record["fields"]["Longitude"]

    return {
        "id": record["id"],
        "product": record["fields"]["Product"][0],
        "lat": lat,
        "long": lng,
        "customer_name": record["fields"]["Customer Name"],
    }


def process_product_record(record):
    return {
        "id": record["id"],
        "product": record["fields"]["Name"],
        "customers": record["fields"].get("customers", []),
        "symbol": record["fields"].get("Symbol", None),
    }


def get_data():
    customers = get_airtable_api(CUSTOMERS).get_all()
    products = get_airtable_api(PRODUCTS).get_all()
    return {CUSTOMERS: customers, PRODUCTS: products}


def get_customers(data):
    return pd.DataFrame(
        [
            process_customer_record(record)
            for record in data[CUSTOMERS]
            if len(record["fields"].keys()) > 0
        ]
    )


def get_products(data):
    return pd.DataFrame(
        [
            process_product_record(record)
            for record in data[PRODUCTS]
            if len(record["fields"].keys()) > 0
        ]
    )
