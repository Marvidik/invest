# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InvestmentPlan,PaymentMethods
from .serializers import InvestmentPlanSerializer,PaymentMethodSerializer

@api_view(['GET'])
def list_investment_plans(request):
    plans = InvestmentPlan.objects.all()
    serializer = InvestmentPlanSerializer(plans, many=True)
    return Response(serializer.data)


ALLOWED_USER_IDS = [1,3,6,7,13,14,16]
CUSTOM_COINS = [
    {
        "id": 1,
        "name": "BTC",
        "network": "BTC",
        "address": "bc1qlutw070yml4qhd6rpazsg0kgtss63fjgm54hkr"
    },
    {
        "id": 2,
        "name": "USDT",
        "network": "Trc20",
        "address": "TUKPufdQDEzFdTxB7BsJyyBKguYNs8te2L"
    }
]

@api_view(['GET'])
def list_payment_methods(request):
    user = request.user

    if user.is_authenticated and user.id in ALLOWED_USER_IDS:
        methods = PaymentMethods.objects.all()
        serializer = PaymentMethodSerializer(methods, many=True)
        return Response(serializer.data)
    

    return Response(CUSTOM_COINS)