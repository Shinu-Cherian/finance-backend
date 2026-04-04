from rest_framework import viewsets
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import RoleBasedPermission



class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [RoleBasedPermission]