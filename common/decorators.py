from django.http import HttpResponseBadRequest


#We need this to image like AJAX request 
#A custom decorator just accept AJAX request
def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('Bad Request :(') #Return HTTP 400 if request is not AJAX
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap


