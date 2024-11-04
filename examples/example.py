import wondaris_sdk
import os
from dotenv import load_dotenv

# Attempt to load a .env file into the environment variables
load_dotenv()

"""
    Instantiate the data source, setting the baseURL (optional),
    data source & data set slugs (from Wondaris Centralise)
    and the token (in this example from en environment variable)
"""
dataSource = wondaris_sdk.data_source.DataSource({
    'baseURL': 'https://mdp.staging.wondaris.com/api/oauth/v1.0/gcs',
    'dataSource': 'demo-staging',
    'dataSet': 'demo-staging',
    'token': os.environ.get('TOKEN'),
})

# Upload the file
dataSource.upload_to_wondaris_file_store('./example.csv')
