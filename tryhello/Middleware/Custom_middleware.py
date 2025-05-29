# middleware run as stack in sequence mentioned in project settings.py

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Adding a logging statement before the view is called")

        response = self.get_response(request)
        response['X-Custom-Header'] = 'FirstProject'
        print("X-Custom-Header added to the response")
        return response