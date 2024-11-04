from wondaris_sdk import wndrs_data_source
import os
from dotenv import load_dotenv

# Attempt to load a .env file into the environment variables
load_dotenv()

"""
    Instantiate the data source, setting the baseURL (optional),
    data source & data set slugs (from Wondaris Centralise)
    and the token (in this example from en environment variable)
"""
dataSource = wndrs_data_source.WndrsDataSource({
    'baseURL': 'https://centralise.platform.wondaris.com/api/oauth/v1.0/gcs',
    'dataSource': 'demo-data-source',
    'dataSet': 'demo-data-set',
    'token': os.environ.get('TOKEN'),
})

try:
    # Upload the file
    dataSource.upload_to_wondaris_file_store('./example.csv')

    print('upload success')
except Exception as e:
    print(e)
