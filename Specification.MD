Reference Index Page:
```
[
   {
      "resourceTreeId":"6249643b20197bb462724bf3",
      "name":"todo API",
      "prefix":"/api/v1",
      "isPublic":true,
      "createdAt":"2022-04-03T09:09:15.289Z",
      "id":"6249643b20197bb462724bf4",
      "owner":{
         "id":"5d4908df2d59e50014f20f06",
         "name":"Gera3dartist",
         "email":null
      },
      "collaborators":[
         
      ]
   }
]
```


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
