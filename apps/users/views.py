from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.users.models import User
from apps.users.serialisers import UsersSerializer,RegisterSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    
    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterSerializer
        return UsersSerializer
    