from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SortSearchSerializer
from typing import List


from django.http import HttpResponse

def home(request):
    return HttpResponse("Up and running!")



def bubble_sort(array: List[int], order: str) -> List[int]:
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (order == "asc" and array[j] > array[j + 1]) or (order == "desc" and array[j] < array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def linear_search(array: List[int], target: int) -> bool:
    return target in array



class SortServiceView(APIView):
    def post(self, request):
        serializer = SortSearchSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            sorted_array = bubble_sort(validated_data["array"], validated_data["order"])
            search_found = linear_search(sorted_array, validated_data["searchValue"])
            response = {
                "sortedArray": sorted_array,
                "searchFound": search_found,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
