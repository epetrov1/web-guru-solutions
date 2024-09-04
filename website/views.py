from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse



def home_page_view(request):
    return render(request, "website/home.html")

# def contact_us_page_view(request):
#     return render(request, "website/contact_us_page.html")

def product_page_view(request):
    return render(request, "website/product.html")

def services_page_view(request):
    return render(request, "website/services_page.html")

def about_page_view(request):
    return render(request, "website/about_page.html")

def service_seo_view(request):
    return render(request, "website/service_seo.html")

def service_digital_marketing_view(request):
    return render(request, "website/service_digital_marketing.html")

def service_web_development_view(request):
    return render(request, "website/service_web_development.html")


#Contact view +sending emails
def contact_us_page_view(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #sender 
            ['office@.web-guru-solutions.com'], #receivers
            )        

        return render(request, "website/contact_us_page.html", {'message_name': message_name})
    else:
        return render(request, "website/contact_us_page.html")