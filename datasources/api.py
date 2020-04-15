from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Sum, Max
from .utils import success, error
import pandas as pd
import json
import datetime

class GetStateLevelCases(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        try:
            response = []
            data = BaseData.objects.values('state').order_by('state')\
                                   .annotate(confirmed=Max('confirmed_cases'))
            print(data)
            for d in data:
                t = dict()
                t["name"] = d["state"]
                t["value"] = d["confirmed"]
                response.append(t)
            return Response(response)
        except KeyError:
            return Response(error("No State provided in query param"))


class GetDistrictLevelCases(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        try:
            response = []
            state = request.query_params["state"]
            data = BaseData.objects.filter(state=state).values('district').order_by('district')\
                                   .annotate(confirmed=Sum('confirmed_cases'))
            for d in data:
                t = {}
                t["name"] = d["state"]
                t["value"] = d["confirmed"]
                response.append(t)
            return Response(response)
        except KeyError:
            return Response(error("No State provided in query param"))


class GetCountryLevelCases(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        try:
            response = []
            country = request.query_params["country"]
            print(country)
            data = BaseData.objects.filter(country=country).order_by('date').values()
            df = pd.DataFrame.from_records(data)
            df["cases"] = df.groupby(['state'])['confirmed_cases'].diff(1).fillna(df["confirmed_cases"])
            df2 = df.groupby('date')["cases"].sum()
            df2 = df2.to_frame()
            df2["median"] = df2.rolling(5).median().fillna(0)
            df2["growth_factor"] = (df2["cases"] / df2["cases"].shift(1)).fillna(0)
            df3 = df2.tail(20)
            # print(df)
            # for d in data:
            #     t = dict()
            #     t["name"] = d["state"]
            #     t["value"] = d["confirmed_cases"]
            #     response.append(t)

            data = json.loads(df3.to_json(orient='table'))
            for d in data["data"]:
                d["date"] = d["date"].split("T")[0]
            return Response(data["data"])
        except KeyError:
            return Response(error("No State provided in query param"))


class GetDistrictLevelRefreshCases(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        try:
            response = []
            state = request.query_params["state"]
            data = StateRefreshData.objects.filter(state=state)
            print(data)
            for d in data:
                t = {}
                t["name"] = d.district
                t["value"] = d.confirmed_cases
                response.append(t)
            return Response(response)
        except KeyError:
            return Response(error("No State provided in query param"))


class GetConsolidatedData(APIView):

    def get(self, request, format=None):
        try:
            response = []
            entity = request.query_params["view"]
            data = ConsolidatedData.objects.get(entity=entity)
            serializer = ConsolidatedDataSerializer(data)
            return Response(serializer.data)
        except KeyError:
            return Response(error("No State provided in query param"))


class GetComparisionData(APIView):

    def get(self, request, format=None):
        try:
            data = ComparisionData.objects.all()
            serializer = ComparisionDataSerializer(data,many=True)
            return Response(serializer.data)
        except KeyError:
            return Response(error("No State provided in query param"))


class GetStateWiseComparisionData(APIView):

    def get(self, request, format=None):
        try:

            data = StateWiseData.objects.all()
            serializer = StateWiseComparisionSerializer(data, many=True)
            return Response(serializer.data)
        except KeyError:
            return Response(error("No State provided in query param"))


class GetAgeWiseData(APIView):

    def get(self, request, format=None):
        try:
            data = AgeWiseData.objects.all()
            serializer = AgeWiseSerializer(data, many=True)
            return Response(serializer.data)
        except KeyError:
            return Response(error("No State provided in query param"))