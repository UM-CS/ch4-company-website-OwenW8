from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Wedget 3"],
        "greeting": "THAnk you FOR visitING",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Mulberry street"
        context["phone_number"] = "555-555-555"
        return context

class ProductsPageView(TemplateView):
    template_name = "products.html"
    
    def get_context_data(self, **kwargs):
        
        context = {
            "products":["hair", "dog", "cake", "tuna"]
        }
        return context