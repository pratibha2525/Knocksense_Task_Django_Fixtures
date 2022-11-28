from django.shortcuts import render
from myapp.models import NewsArticles, Like, User, Locality, City, userRole
from myapp.serializers import NewsArticlesSerializer, LikeSerializer, UserSerializer, LocalitySerializer, CitySerializer
# from newsArticle_new.myproject.myproject.settings import CACHE_TTL
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache



# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
## User model
class UserAPI(APIView):
    def get(self, request):
        userobj = User.objects.all()
        userserializerobj = UserSerializer(userobj, many=True)
        return Response(userserializerobj.data)

class Usercreate(APIView):
    def post(self, request):
        serializer1 = UserSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get_pk(self, pk):
        try: 
            return User.objects.get(pk=pk)
        except:
            return Response({
                'error':'User does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        username = self.get_pk(pk)
        serializer1 = UserSerializer(username)
        return Response(serializer1.data)


    def put(self, request, pk):
        # username = self.get_pk(pk)
        username = User.objects.get(pk=pk)
        serializer1 = UserSerializer(username, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        username = self.get_pk(pk)
        username.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


# NewsArticles Models

class newsAPI(APIView):
    def get(self, request):
        news = NewsArticles.objects.all()
        serializerobj = NewsArticlesSerializer(news, many=True)
        result = serializerobj.data
        return Response(result)


class newsCreate(APIView):
    def post(self, request):
        serializer2 = NewsArticlesSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response({'msg':'Data Created...'}, status=status.HTTP_201_CREATED)
            # return Response(serializer2.data, status=status.HTTP_201_created)
        else:
            # return Response({'msg':'User is not available..'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
                
        # else:
        #     return Response({'msg':'User is not available..'}, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)      
        # if serializer2.is_valid():  
        #     serializer2.save()
        #     return Response({'msg':'Data Created...'}, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

class newsDetail(APIView):

    def get_n_pk(self, pk):
        try: 
            return NewsArticles.objects.get(pk=pk)
        except:
            return Response({
                'error':'Article does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        news = self.get_n_pk(pk)
        serializer1 = NewsArticlesSerializer(news)
        return Response(serializer1.data)

    def put(self, request, pk):
        # username = self.get_n_pk(pk)
        news = NewsArticles.objects.get(pk=pk)
        serializer1 = NewsArticlesSerializer(news, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        news = self.get_n_pk(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# Like Models

class LikeAPI(APIView):
    def get(self, request):
        like = Like.objects.all()
        serializerobj = LikeSerializer(like, many=True)
        result = serializerobj.data
        return Response(result)


class LikeCreate(APIView):
    def post(self, request):
        serializer2 = LikeSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response({'msg':'Data Created...'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeDetail(APIView):

    def get_pk(self, pk):
        try: 
            return Like.objects.get(pk=pk)
        except:
            return Response({
                'error':'Article does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        like = self.get_pk(pk)
        serializer1 = LikeSerializer(like)
        return Response(serializer1.data)

    def put(self, request, pk):
        # username = self.get_pk(pk)
        like = Like.objects.get(pk=pk)
        serializer1 = LikeSerializer(like, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        like = self.get_pk(pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

#### Joins like

class join(APIView):
    def get(self, request, pk):

        likedetail = User.objects.filter(
            user_id__in=Like.objects.filter(
                news_id__in=NewsArticles.objects.filter(
                    news_id=pk
                )
            )
        )
        data = []
        for i in likedetail:
            data_dict = {}
            data_dict["name"] = i.user_name
            print(i.user_name)
            data.append(data_dict)

        return Response(data)


# class join(APIView):
#     def get(self, request, pk):

#         likedetail = Like.objects.filter(
#             news_id=pk
#       )
#         data = []
#         for i in likedetail:
#             data_dict = {}
#             data_dict["id"] = i.id
#             data_dict["user_id"] = i.user_id
#             data_dict["news_id"] = i.news_id
#             data.append(data_dict)

#         return Response(data)

########## Locality
## Locality model
class LocalityAPI(APIView):
    def get(self, request):
        localityobj = Locality.objects.all()
        lserializerobj = LocalitySerializer(localityobj, many=True)
        return Response(lserializerobj.data)

class Localitycreate(APIView):
    def post(self, request):
        serializer1 = LocalitySerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

class LocalityDetail(APIView):

    def get_pk(self, pk):
        try: 
            return Locality.objects.get(pk=pk)
        except:
            return Response({
                'error':'User does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        localityname = self.get_pk(pk)
        serializer1 = LocalitySerializer(localityname)
        return Response(serializer1.data)


    def put(self, request, pk):
        localityname = Locality.objects.get(pk=pk)
        serializer1 = LocalitySerializer(localityname, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        localityname = self.get_pk(pk)
        localityname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


## City model
class CityAPI(APIView):
    def get(self, request):
        cityobj = City.objects.all()
        cityserializer = CitySerializer(cityobj, many=True)
        return Response(cityserializer.data)

class Citycreate(APIView):
    def post(self, request):
        serializer1 = CitySerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetail(APIView):

    def get_pk(self, pk):
        try: 
            return City.objects.get(pk=pk)
        except:
            return Response({
                'error':'User does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        cityname = self.get_pk(pk)
        serializer1 = CitySerializer(cityname)
        return Response(serializer1.data)


    def put(self, request, pk):
        cityname = City.objects.get(pk=pk)
        serializer1 = CitySerializer(cityname, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cityname = self.get_pk(pk)
        cityname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


#### Joins locality
class joinlocality(APIView):
    def get(self, request, pk):

        likedetail = Locality.objects.filter(
            id=pk
            
      )
        data = []
        for i in likedetail:
            data_dict = {}
            data_dict["id"] = i.id
            data_dict["locality_name"] = i.locality_name
            # data_dict["city_id"] = i.city_id
            data.append(data_dict)

        return Response(data)

   