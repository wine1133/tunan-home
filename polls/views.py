from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contract
from .serializers import ContractSerializer


@api_view(["GET"])
def api_hello(request):
    """供 Vue 前端调用的示例接口。"""
    return Response({
        "message": "你好，Vue！这条数据来自 Django API。",
        "framework": "Django 5.2 + Django REST Framework",
    })


@api_view(["POST"])
def contract_create(request):
    """接收联系表单数据并写入 contract 表。"""
    serializer = ContractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "提交成功", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(
        {"message": "提交失败", "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )