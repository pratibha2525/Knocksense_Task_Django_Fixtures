from django.urls import path
from myapp.views import UserAPI,Usercreate,UserDetail,newsAPI,newsCreate,newsDetail,LikeAPI,LikeCreate,LikeDetail,join,LocalityAPI,Localitycreate,LocalityDetail,CityAPI,Citycreate,CityDetail,joinlocality

urlpatterns = [
    path('list/', UserAPI.as_view()), # get user
    path('upost', Usercreate.as_view()), # post user
    path('<int:pk>', UserDetail.as_view()), # get, put, delete user
    path('newslist/', newsAPI.as_view()), # get NewsArticles
    path('newc', newsCreate.as_view()), # post NewsArticles
    path('nd/''<int:pk>', newsDetail.as_view()), # get, put, delete NewsArticles
    path('likeget/', LikeAPI.as_view()), # get like
    path('likep', LikeCreate.as_view()), # post like
    path('ld/<int:pk>', LikeDetail.as_view()), # get, put, delete like
    path('join/<int:pk>', join.as_view()), # join get
    path('locality/', LocalityAPI.as_view()), # get locality
    path('localitypost/', Localitycreate.as_view()), # post locality
    path('localitycrud/<int:pk>', LocalityDetail.as_view()), # locality get, put, delete
    path('city/', CityAPI.as_view()), # get City
    path('citypost/', Citycreate.as_view()), # post City
    path('citycrud/<int:pk>', CityDetail.as_view()), # city crud
    path('joinlocality/<int:pk>', joinlocality.as_view()), # join get
]