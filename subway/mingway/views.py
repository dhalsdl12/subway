from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os, json, logging

class MingSubway(APIView):
    def get(self, request, format=None):
        return Response("Ming's Subway", status=status.HTTP_200_OK)