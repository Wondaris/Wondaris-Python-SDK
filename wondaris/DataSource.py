import requests
import os

from tusclient import client
from typing import Dict, Optional

class DataSource:
    configs = {}

    def __init__(self, configs: Optional[Dict[str, str]] = None):
       self.set_configs(configs)

    def set_configs(self, configs: Dict[str, str]):
        self.configs = {
            'baseURL': 'https://centralise.platform.wondaris.com/api/oauth/v1.0/gcs',
            **self.configs,
            **configs,
        }

        return self

    def validate(self):
        if 'dataSet' not in self.configs or not self.configs['dataSet']:
            raise Exception('dataSet is required')

        if 'dataSource' not in self.configs or not self.configs['dataSource']:
            raise Exception('dataSource is required')

        if 'token' not in self.configs or not self.configs['token']:
            raise Exception('token is required')

        return self

    def get_upload_info(self):
        url = f'{self.configs["baseURL"]}/{self.configs["dataSource"]}/{self.configs["dataSet"]}'
        headers = {
            'Authorization': f'Bearer {self.configs["token"]}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        session = requests.Session()

        response = session.post(url=url, headers=headers)

        response.raise_for_status()

        return response.json()

    def upload_to_wondaris_file_store(self, file_path, *args, **kwargs):
        if not os.path.isfile(file_path):
            raise Exception('File not found')

        upload_info = self.validate().get_upload_info()

        upload_info['url'] = 'http://127.0.0.1:8080/upload'

        headers = {
            **(kwargs.get('headers', {}) or {}),
            'Authorization': upload_info["short_token"],
        }

        metadata = {
            **(kwargs.get('metadata', {}) or {}),
            'filename': os.path.basename(file_path),
        }

        chunk_size = kwargs.get('chunk_size', 30 * 1024 * 1024)

        my_client = client.TusClient(url=upload_info['url'], headers=headers)
        uploader = my_client.uploader(file_path=file_path,
                           metadata=metadata,
                            # retry_delays=[0, 1000, 3000, 5000],
                           chunk_size=chunk_size,
                           *args, **kwargs)

        uploader.upload()

        print('upload complete')

