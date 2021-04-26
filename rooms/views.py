from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"

# def all_rooms(request):
#     page = request.GET.get("page")
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", context={"page": rooms})
#     except EmptyPage:
#         return redirect
