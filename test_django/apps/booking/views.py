from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Booking

def index(request):
    latest_booking_list = Booking.objects.order_by('-pub_date')[:5]
    return render(request, 'booking/list.html', {'latest_booking_list': latest_booking_list})

def detail(request, booking_id):
    try:
        a = Booking.objects.get(id = booking_id)
    except:
        raise Http404("Бронирование не найдено!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'booking/detail.html', {'booking': a, 'latest_comments_list': latest_comments_list})

    
    
def leave_comment(request, booking_id):
    try:
        a = Booking.objects.get(id = booking_id)
    except:
        raise Http404("Бронирование не найдено!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'],
                         booking_date_input = request.POST['booking_date_input'], booking_time_input = request.POST['booking_time_input'], booking_hours = request.POST['booking_hours'])

    return HttpResponseRedirect(reverse('booking:detail', args = (a.id,)))


    

