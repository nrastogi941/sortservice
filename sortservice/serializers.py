from rest_framework import serializers


class SortSearchSerializer(serializers.Serializer):
    array = serializers.ListField(
        child=serializers.IntegerField(),
        error_messages={"invalid": "Array must contain only integers."}
    )
    order = serializers.ChoiceField(
        choices=["asc", "desc"],
        error_messages={"invalid_choice": "Order must be either 'asc' or 'desc'."}
    )
    searchValue = serializers.IntegerField()