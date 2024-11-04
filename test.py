from wondaris import DataSource

dataSource = DataSource.DataSource({
    'baseURL': 'https://mdp.staging.wondaris.com/api/oauth/v1.0/gcs',
    'dataSource': 'demo-staging',
    'dataSet': 'demo-staging',
    'token': 'acf7ed13-e7c4-4b4e-828e-7a51f0fa9c18',
})

dataSource.upload_to_wondaris_file_store('./example.csv')