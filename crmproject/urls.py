from django.contrib import admin
from django.urls import path, include
from customer.views import CustomerListCreateAPIView, CustomerDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', CustomerListCreateAPIView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view()),
    path('api/', include('customer.urls'))
]
