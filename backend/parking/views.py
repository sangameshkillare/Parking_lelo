from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ParkingSpace

def parking_list(request):
    parkings = ParkingSpace.objects.all()
    return render(request, 'parking/parking_list.html', {'parkings': parkings})




from django.shortcuts import redirect
from .forms import BookingForm
from .models import Booking

def book_parking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            # calculate total price if not free
            if not booking.parking_space.is_free:
                hours = (booking.end_time - booking.start_time).seconds / 3600
                booking.total_price = hours * booking.parking_space.price_per_hour
            booking.save()
            return redirect('parking_list')
    else:
        form = BookingForm()
    return render(request, 'parking/book_parking.html', {'form': form})
