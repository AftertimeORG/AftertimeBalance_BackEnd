from django.urls import path
from . import apiREST

urlpatterns = [
    path('vehicle/ship', apiREST.ShipPosition.as_view()),
    path('vehicle/ship/track', apiREST.ShipTrack.as_view()),
    path('vehicle/map/ships', apiREST.ShipsOnMap.as_view()),
    path('ping', apiREST.Ping.as_view()),
    # path('balance/substances', apiREST.BalanceListView.as_view()),
    # path('people', apiREST.PostListView.as_view()),
    # path('people/<str:pk>', apiREST.PeopleRetrieveUpdateDeleteView.as_view()),
    # path('location', apiREST.LocationsAL.as_view()),
    # path('location/<str:pk>', apiREST.LocationsRGUD.as_view()),
    # path('companies', apiREST.CompaniesListView.as_view()),
    # path('companies/<str:pk>', apiREST.CompaniesRetrieveUpdateDeleteView.as_view()),
    # path('search-requests', apiREST.SearchRequestsView.as_view()),
    # path('search-requests/<str:pk>', apiREST.SearchRequestsRGUD.as_view()),
    # path('thread-task/ping', apiREST.ThreadTaskPing.as_view()),
    # path('thread-task/send-all-task-for-processing', apiREST.ThreadTaskSendAllTaskForProcessing.as_view()),
]
