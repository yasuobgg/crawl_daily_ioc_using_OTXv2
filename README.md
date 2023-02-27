# Crawl indicator 
### Crawl daily ioc from Alientvault OTX and save to mongodb

## Use:

### using postman to get indicators from mongodb

### GET {ip}:5000/app

### body -> raw JSON
```
{
    "indicator":"d38a9b4d0c17c954080b86bb79a25272"
}

```

## Response:
### sample
```
[
    {
        "created": "2017-08-24T09:27:23",
        "indicator": "d38a9b4d0c17c954080b86bb79a25272",
        "type": "FileHash-MD5"
    },
    {
        "created": "2017-08-24T09:27:23",
        "indicator": "d38a9b4d0c17c954080b86bb79a25272",
        "type": "FileHash-MD5"
    }
]

```