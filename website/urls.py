from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("contact-us/", views.contact_us_page_view, name="contact_us"),
    path("product/", views.product_page_view, name="product"),
    path("services/", views.services_page_view, name="services"),
    path("about/", views.about_page_view, name="about_us"),
    path("service-seo/", views.service_seo_view, name="service_seo"),
    path("service-digital-marketing/", views.service_digital_marketing_view, name="service_digital_marketing"),
    path("web-development/", views.service_web_development_view, name="service_web_development"),
]
