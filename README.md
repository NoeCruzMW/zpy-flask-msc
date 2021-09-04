<p align="center">
  <a  href="https://github.com/NoeCruzMW/zpy-flask-msc-docs"><img width="150" src="https://lh3.googleusercontent.com/a-/AOh14GjLO5qYYR5nQl5hgavUKz4Dv3LVzWDvGtV4xNam=s600-k-no-rp-mo" alt="Zurck'z"></a>
</p>
<p align="center">
    <em>ZPy Flask MSC, Layer for build microservices</em>
</p>
<p align="center"></p>

---

# ZPy Flask MSC

> Zurck'z Py Flask Micro Services Core

This package contains some helpers features for build python microservices using Flask framework

ZPy use the following packages:

- pycryptodome
- Flask
- marshmallow
- cx-Oracle

## Requirements

- Python 3.6+
- Boto 3+
- Oracle Client

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install py flask micro service core .

```bash
pip install boto3
pip install zpy
```

## Features

Contains some helper features with specific integrations.

- Api
  - Api Builder
  - Response Builder
  - Models
  - Hooks
  - Middlewares
  - Exceptions
  - Repositories
    - Only oracle repository implementation for functions calling.
- Cloud Implementations
  - AWS Services
    - S3
    - SSM
    - Firehose
    - SQS
- Custom
  - Plugings
- Database
  - Only Oracle implementation
    - Functions executor
- Logger
  - Stream
- Utils
  - Collections
  - Cipher
  - Functions
  - gzip

## Basic Usage

```python
#Define api
@api(base='/v1', config=config,hooks=hk,middlewares=mw)
def create_api():
    #Define all dependencies for enterprise resources
    service = CompanyService(repository=CompanyRepositoryImpl(db))
    #Set all supported resource for this web service.
    return \
    [
        ZResource('/', CompanyResource,service=service),
        ...
    ]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

[Noé Cruz](https://www.linkedin.com/in/zurckz/)
