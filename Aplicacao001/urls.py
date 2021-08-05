from django.urls import path
#from .views import Pagina_Inicial, Pagina_Inicial_02, Pagina_Inicial_03
from .views import Inicial

urlpatterns = [
    path('', Inicial.as_view(), name='Pagina_Inicial' ),
]