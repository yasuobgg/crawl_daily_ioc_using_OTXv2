# Crawl indicator 
### Crawl daily ioc from Alientvault OTX and save to mongodb

## Use:

### using postman to get indicators from mongodb

### POST {ip}:8000/api/v1

### body -> raw JSON
## Query and response
### query with type that not define in the main function
```
{
    "type":"email"
}
```
### Response:
```
{
    "Type error": "Unavailable"
}
```
### query with type defined in the main function
```
{
    "type":"MD5"
}
```
### Response:
```
 {
        "timestamp": 1677554511,
        "type": "MD5",
        "data": [
            "d38a9b4d0c17c954080b86bb79a25272",
            "54b5c261ecbd63118f1a135cb4f091d6",
            "44994d7d75e6c6f215d239bba5d8f411",
            "7166665cf5d69422fb710009161faf64",
            "6467c6df4ba4526c7f7a7bc950bd47eb",
            "e904bf93403c0fb08b9683a9e858c73e",
            "b80aa583591eaf758fd95ab4ea7afe39",
            "760c35a80d758f032d02cf4db12d3e55",
            "d1c27ee7ce18675974edf42d4eea25c6",
            ]
}
```