from django.shortcuts import render
from django.views.generic import *
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

    """ FOR MORE, VISIT https://ccbv.co.uk/projects/Django/4.0/django.views.generic.base/TemplateView/"""






# GENERIC BASE
class MainObjectView(View):

    """ Optional props """
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        return

    def post(self, request, *args, **kwargs):
        return

    def put(self, request, *args, **kwargs):
        return

    def delete(self, request, *args, **kwargs):
        return






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
        """ redirect action """
        return super(LinkPreloadView, self).get_redirect_url(**kwargs)

    """ Optional methods """
    def post(self, request, *args, **kwargs):
        """ action """
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ action """
        return self.get(request, *args, **kwargs)

    """ FOR MORE, VISIT https://ccbv.co.uk/projects/Django/4.0/django.views.generic.base/RedirectView/"""






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

    """ FOR MORE, VISIT https://ccbv.co.uk/projects/Django/4.0/django.views.generic.detail/DetailView/"""






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

    """ FOR MORE, VISIT https://ccbv.co.uk/projects/Django/4.0/django.views.generic.list/ListView/"""






# GENERIC EDIT
class ObjectFormView(FormView):

    template_name = ''
    form_class = None
    success_url = '/'

    """ Optional props """
    fields = None
    http_method_names = ['get', 'post', 'put']
    content_type = None	
    extra_context = None
    template_engine = None

    def form_valid(self, form):
        form.save()
        return super(ObjectFormView, self).form_valid(form)

    """ Optional methods """
    def get_context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context['title'] = 'Index'
        return context

    def get_form_class(self):
        # Return the form class to use.
        return None

    def get_success_url(self):
        return '/' 

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    	
    def put(self, *args, **kwargs):
        """ action if needed """
        return self.post(*args, **kwargs)

    """ FOR MORE, VISIT https://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/FormView/"""






# GENERIC EDIT
class ObjectCreateView(CreateView):

    model = None
    template_name = ''
    success_url = '/'

    """ Optional props """
    form_class = None
    context_object_name = ''
    fields = None
    http_method_names = ['get', 'post', 'put']
    content_type = None	
    extra_context = None
    template_engine = None


    """ 
        Optional methods ( same as FormView methods ) 
        But no need for form validaion methods in this class

    """


    """ FOR MORE, VISIT https://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/CreateView/"""