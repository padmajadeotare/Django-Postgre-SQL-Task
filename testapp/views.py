from django.shortcuts import render,redirect
from django.views.generic import View
from . forms import *
from testapp.forms import *
from testapp.validation import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class InfoView(APIView):

    @staticmethod
    def post(request):
        data = request.data
        if data:
            try:
                info = info_save(data)
                return Response({"is_success": True, "message": 'Successfully save', "data": 'info'},
                                status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"is_success": False, "message": 'something went wrong', "data": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({"is_success": False, "message": 'Payload is empty', "data": ''},
                            status=status.HTTP_200_OK)


    @staticmethod
    def get(request):
        """
            get data from Info model of postgres database

        """
        rows = get_info()
        if rows:
            return Response({"is_success": True, 'message': "Successfully found data", 'data': rows},
                                status=status.HTTP_200_OK)
        else:
            return Response({"is_success": False, 'message': "Data not found", 'data': rows},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InformView(View):
    form_class = InfoForm
    template_name = 'testapp/home.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/infoview/')

        return render(request, self.template_name, {'form' : form})
