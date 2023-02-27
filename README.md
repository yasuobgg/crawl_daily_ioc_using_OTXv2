# Crawl indicator 
### Crawl daily ioc from Alientvault OTX and save to mongodb

## Use:

### using postman to get indicators from mongodb

### GET {ip}:5678/app

### body -> raw JSON
```
{
    "type":"CVE"
}
```

## Response:
### sample
```
[
    {
        "data": [
            "CVE-2012-0158",
            "CVE-2014-0322",
            "CVE-2012-0773",
            "CVE-2011-3544",
            "CVE-2010-2568"
        ],
        "timestamp": 1677510520,
        "type": "CVE"
    }
]
```