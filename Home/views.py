from Home.serializers import UserSerializer
from .models import User
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .pagination import CustomPagination

# Create your views here.




class UserListCreate(ListCreateAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.GET.get('name'):
            queryset = queryset.filter(
                Q(first_name__icontains=self.request.GET.get('name')) | Q(last_name__icontains=self.request.GET.get('name'))
            )
        if self.request.GET.get('sort'):
            queryset = queryset.order_by(self.request.GET.get('sort'))
        return queryset


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
