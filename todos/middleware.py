class CustomMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type,X-Custom-Header'
        if request.method =="OPTIONS":
            response['Access-Control-Allow-Methods'] = 'GET, POST'
            response['Content-Type'] = 'text/html'
        return response