from testapp.models import *
from rest_framework import status
from rest_framework.response import Response
def info_save(data):
    try:
        from django.db.models import Q
        obj = Info.objects.filter(Q(email=data.get('email')) | Q(contact_no=data.get('contact_no')))
        if obj:
            return obj
        else:
            info = Info(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                gender=data.get('gender'),
                email=data.get('email'),
                contact_no=data.get('contact_no'),
                bio_description=data.get('bio_description'),
                id_proof=data.get('id_proof'),
                photo=data.get('photo'),
            )
            info.save()
            return info

    except Exception as e:
        return Response({'is_success': False, 'message': 'something went wrong', 'data': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def  get_info():
    obj = Info.objects.all().values()
    return obj
