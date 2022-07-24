from cgitb import lookup
from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer,BookingListSerializer, BookingDetailSerializer , BookingUpdateSerializer, BookingDeleteSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer

"""Create an API detail view:
Which will display the following fields for the Booking object:
id
flight
date
passengers"""

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDeleteSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"