from solace import Request, PlainTextResponse

def hello_world(request: Request):
    return PlainTextResponse("Hello, World")

