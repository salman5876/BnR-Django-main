from rest_framework.views import APIView
from django.db.models import Q
from categories.models import CategoriesBrandNames
from rest_framework import status, permissions
from rest_framework.response import Response

class GetBrandsNames(APIView):

    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        try:
            exclude_list = ['', 'Total', '00', 'NO BRAND', 'No Brand', 'Does Not Apply', 'Does not apply', 'Not Available',
                            'Unbranded', 'Unknown', 'Unknown', '0.0', 'PackagingSuppliesByMail', 'NA', 'na', 'N/A', 'Ship Now Supply',]
            exclude_list = [name.strip() for name in exclude_list]
            # specific_letters = ['s/ref',]
            x = CategoriesBrandNames.objects.exclude(
                Q(brand_name__in=exclude_list) |
                Q(brand_name__isnull=True) |
                Q(brand_name=None) |
                Q(brand_name__startswith='s/ref') |
                Q(brand_name__exact='')
                # ).values('brand_name').annotate(count=Count('brand_name')).order_by('-count')
                # ).values_list('brand_name', flat=True).annotate(count=Count('brand_name')).order_by('-count')
            ).values('id', 'brand_name') #.order_by('-products_count')
            print(x.count())
            print(x)
            return Response(x, status.HTTP_200_OK)

        except Exception as e:
            return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)

