from django.urls import path
from .views import parking_list
from .views import book_parking

urlpatterns = [
    path('', parking_list, name='parking_list'),
     path('', parking_list, name='parking_list'),
    path('book/', book_parking, name='book_parking'),
]



# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse

# # Temporary home view (to fix NoReverseMatch for 'home')
# def home_view(request):
#     return HttpResponse("Welcome to Parking Lelo Home Page")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),  # include accounts app urls
#     path('parking/', include('parking.urls')),    # include parking app urls
#     path('', home_view, name='home'),             # ✅ named "home"
# ]
