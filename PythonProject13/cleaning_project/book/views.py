from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def home(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succe')
        else:
            # Temporary print statement to debug in your terminal terminal window
            print("❌ Form Errors:", form.errors.as_data())
    else:
        form = BookingForm()

    return render(request, 'home.html', {
        'form': form,
    })

def succe(request):
    # Match this function to your success URL name pattern
    return render(request, 'succe.html')


def dach(request):
    # Fetch all bookings to show in table
    all_bookings = Booking.objects.all().order_by('-date')
    return render(request, 'dach.html', {'appointments': all_bookings})