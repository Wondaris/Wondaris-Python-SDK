# wondaris_sdk
> This is the SDK that Wondaris Team has developed for applications using Python for the Wondaris services.
> 
> This SDK simplifies uploading files to Wondaris File Storage via the Tus protocol, making it easy to integrate into your Python projects.

# Prerequisites

1. Firstly, you need to be an active Wondaris customer and have an account on https://centralise.platform.wondaris.com.
2. You need to create a data source of type "Wondaris File Storage" on the Centralise, and then create a dataset within that source.
3. Create a token that has the appropriate scope to allow access and manipulation of the dataset you have created.

# Installation

## Install

Install the package using a package manager, such as `pip`:

```
$ pip install git+ssh://git@github.com/Wondaris/Wondaris-Python-SDK.git
```

After that, you can load the package:

```python
from wondaris_sdk import wndrs_data_source
```

# Usage

This document contains an introduction and example about how to use wondaris_sdk:

## Example: Simple file upload
```python
import os

dataSource = wndrs_data_source.WndrsDataSource({
    'baseURL': 'https://centralise.platform.wondaris.com/api/oauth/v1.0/gcs',
    'dataSource': 'demo-data-source',
    'dataSet': 'demo-data-set',
    'token': os.environ.get('TOKEN'),
})

# path to file which you want to upload
pathToFile = './example.csv'

try:
    # Upload the file
    dataSource.upload_to_wondaris_file_store(pathToFile)

    print('upload success')
except Exception as e:
    print(e)
```

## Tus Options
> You can add additional options for customization and control in your application

### headers

_Default value:_ `{Authorization: 'Bearer ' + wondarisToken}`

An object with custom header values used in all requests. For example:

```python
headers = {
    'Content-Type': 'application/json',
}

try:
    # Upload the file
    dataSource.upload_to_wondaris_file_store(pathToFile, headers=headers)

    print('upload success')
except Exception as e:
    print(e)
```

#### chunk_size

_Default value:_ ` 30 * 1024 * 1024` Bytes

A number indicating the maximum size of a `PATCH` request body in bytes. With value (`Infinity`) means that tuspy will try to upload the entire file in one request. This setting is also required if the input file is a reader/readable stream.

**Warning:** **Do not set this value**, unless you are being forced to. The only two valid reasons for setting `chunk_size` are:

- You are passing a reader or readable stream as input to tuspy and it will complain that it "cannot create source for stream without a finite value for the chunkSize option" if you leave `chunk_size` empty.
- You are using a tus server or proxy with a limit on how big request bodies may be.

In all other cases, **do not set this value** as it will hurt your upload performance. If in doubt, leave this value to the default or contact us for help.

If you are required to specify a value, consider this:

- A small chunk size (less than a few MBs) may reduce the upload performance dramatically. Each `PATCH` request can only carry little data, which requires more HTTP requests to transmit the whole file. All of these HTTP requests add overhead to the upload process. In addition, if the server has hard limits (such as the minimum 5 MB chunk size imposed by S3), specifying a chunk size which below outside those hard limits will cause chunked uploads to fail.
- A large chunk size (more than a GB) is problematic when a reader/readable stream is used as the input file. In these cases, tus-js-client will create an in-memory buffer with the size of `chunk_size`. This buffer is used to resume the upload if it gets interrupted. A large chunk size means a larger memory usage in this situation. Choosing a good value depends on the application and is a trade-off between available memory and upload performance.

_Example:_
```python
from sys import maxsize as MAXSIZE

try:
    # Upload the file
    dataSource.upload_to_wondaris_file_store(pathToFile, chunk_size=MAXSIZE)

    print('upload success')
except Exception as e:
    print(e)
```

#### metadata

_Default value:_ `{filename: realFilename}`

An object with string values used as additional meta data which will be passed along to the server when (and only when) creating a new upload. Can be used for filenames, file types etc, for example:

```python
metadata = {
    'filetype': "image/png",
    'userId': "1234567",
}

try:
    # Upload the file
    dataSource.upload_to_wondaris_file_store(pathToFile, metadata=metadata)

    print('upload success')
except Exception as e:
    print(e)
```

  - retries (int):
            The number of attempts the uploader should make in the case of a failed upload.
            If not specified, it defaults to 0.

#### retries

_Default value:_ `0`

The number of attempts the uploader should make in the case of a failed upload.


```python
try:
    # Upload the file
    dataSource.upload_to_wondaris_file_store(pathToFile, retries=1)

    print('upload success')
except Exception as e:
    print(e)
```
