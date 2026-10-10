from rest_framework import serializers

from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "contact",
            "phone",
            "company",
            "project_type",
            "quantity",
            "city",
            "budget",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]