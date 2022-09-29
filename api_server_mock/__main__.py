import uvicorn

if __name__ == '__main__':
    uvicorn.run('api_server_mock.resources:app', debug=True, reload=True, port=8080)
