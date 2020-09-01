from django.utils.deprecation import MiddlewareMixin

class AppMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print ('Request---------------',request)
        return None

    def process_response(self,request, response):
        print ('Request****************',request)
        print('Response****************', response)
        return None
