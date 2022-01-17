import sqlite3
from datetime import datetime
from uuid import uuid4
from itertools import chain

from django.shortcuts import render, get_object_or_404

from .models import Service
# Create your views here.


def service_list_view(request):
    query = request.GET.get('q', None)
    objs = Service.objects.all()
    if (query is not None):
        objs_list = []
        db = sqlite3.connect('db.sqlite3')
        db.execute("""INSERT INTO LOGS (id, service_id, type, content, date)
                      VALUES (?, ?, ?, ?, ?);""",
                   (str(uuid4()), None, 'search', query, datetime.now()))
        db.commit()
        db.close()
        for obj in objs:
            if (query.lower() in obj.name.lower()):
                objs_list.append(obj)
        none_model = Service.objects.none()
        objs = list(chain(none_model, objs_list))
    context = {
        'objects': objs
    }
    return render(request, "services/template/service_list.html", context)


def service_detail_view(request, id):
    obj = get_object_or_404(Service, id=id)
    db = sqlite3.connect('db.sqlite3')
    db.execute("""INSERT INTO LOGS (id, service_id, type, content, date)
                  VALUES (?, ?, ?, ?, ?);""",
               (str(uuid4()), obj.id, 'view', '', datetime.now()))
    db.commit()
    db.close()
    context = {
        'object': obj
    }
    return render(request, "services/template/service_detail.html", context)

