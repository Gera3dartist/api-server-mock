
POST /register 
{
    "email": <str>
    "password": <str>
}

GET /me
{
    email: <str>,
    "id": <uuid>
    "name": <str>
}

GET /projects
[
    {
        "resource_id": <str>,
        "created_at": <str>,
        "prefix": <str>,
        "id": <str>
        "owner": {
            "email": <str>,
            "id":  <str>,
            "name": <str>,
        }
        
    }
]

##  GET  /projects/<project_id:str>/resources
[
    {
    "id": <str>,
    "name": <str>,
    "schmema": {
        "fields: [
            {
                "name": <str>,
                "type": FIELD_TYPES,
                "default": DEFAULT_FACTORY
            }
        ]
    "count": <int>
    "mock_data_id": <str>  # id of document/row where data is stored
    "endpoints": [
        {
            "url": <str>,
            "method": <str>,
            "enanbled": <bool>,
        },
        {..}
    ]
    }
]



##  POST  /projects/<project_id:str>/resources
{
    "name": <str>
    "schmema": {
        "fields: [
            {
                "name": <str>,
                "type": FIELD_TYPES,
                "default": DEFAULT_FACTORY
            }
        ]
    "count": <int>
    "endpoints": [
        {
            "url": <str>,
            "method": <str>,
            "enanbled": <bool>,
        },
        {..}
    ]
    }
}
