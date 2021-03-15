from django.urls import path
from .views import (
    CampaignList,
    CampaignDetail
)

urlpatterns = [
    path('', CampaignList.as_view(), name='campaign'),
    path('<int:id>', CampaignDetail.as_view(), name='campaign_detail')
]