from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, DetailView, ListView
# Create your views here.

# GENERIC BASE
class IndexView(TemplateView):

    template_name = 'index.html'

    """ Optional props """
    content_type = 'text/html'
    template_engine= ''
    response_class = None

    """ Optional methods """
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Django CBV'
        return context


# GENERIC BASE
class LinkPreloadView(RedirectView):

    pattern_name = 'index'

    """ Optional props """
    url = 'https://www.hassanelabdallah.com/'
    http_method_names = ['get', 'post', 'put']
    permanent = False
    template_engine = None
    content_type = 'text/html'

    def get_redirect_url(self, **kwargs):

        """ 
            Redirect action, ex: number of visitors
        """

        return super(LinkPreloadView, self).get_redirect_url(**kwargs)

    """ Optional props """
    def post(self, request, *args, **kwargs):
        """ action """
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ action """
        return self.get(request, *args, **kwargs)


# GENERIC DETAIL
class ObjectDetailView(DetailView):

    model = None
    template_name = ''

    """ Optional props """
    context_object_name = 'Object'
    http_method_names = ['get']   
    response_class = None
    queryset = None
    content_type = 'text/html'
    pk_url_kwarg = 'pk'
    template_engine = None

    """ Optional methods """
    def get_context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context['title'] = 'Index'
        return context
        
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = self.get_queryset()
        return obj 

    def get_queryset(self,**kwargs):
        pk = self.kwargs.get('pk')
        return



# GENERIC LIST
class ObjectListView(ListView):

    model = None
    template_name = ''

    """ Optional props """
    paginate_by = 1 # recommended to use
    allow_empty = True
    http_method_names = ['get'] 
    context_object_name = 'Object'
    queryset = None
    template_engine = None
    content_type = 'text/html'

    """ Optional methods """
    def get_context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context['title'] = 'Index'
        return context

    def get_allow_empty(self):
        """
        Return ``True`` if the view should display empty lists and ``False``
        if a 404 should be raised instead.
        """
        return self.allow_empty
        
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = self.get_queryset()
        return obj 

    def get_queryset(self,**kwargs):
        pk = self.kwargs.get('pk')
        return