from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from datetime import datetime, timedelta,date

from books.models import Books

class client_books(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        ret_list = []
        res_books = Books.objects.filter(status=1,reservado_por=request.user.id)#.values('data_reserva','nome')
        if res_books.exists():
            for item in res_books:
                d1 = datetime.strptime(str(date.today()), "%Y-%m-%d")
                d2 = datetime.strptime(str(item.data_reserva), "%Y-%m-%d")
                dias_atraso = abs((d2 - d1).days)
                if int(dias_atraso) == 0:
                    item.multa = 0
                elif int(dias_atraso) <= 3:
                    item.multa = 3 + int(dias_atraso) * 0.2
                elif int(dias_atraso) <= 5:
                    item.multa = 5 + int(dias_atraso) * 0.4
                else:
                    item.multa = 7 + int(dias_atraso) * 0.6
                
                ret_list.append(item)

        qs_json = serializers.serialize('json', ret_list)
        return HttpResponse(qs_json, content_type='application/json')
