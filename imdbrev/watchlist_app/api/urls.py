from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from imdbrev.watchlist_app.api.view import UserReview
# from imdbrev.watchlist_app.api.view import ReviewDetail
# from imdbrev.watchlist_app.api.view import ReviewList
# from imdbrev.watchlist_app.models import Review
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.view import WatchListGV,WatchListAV, WatchDetailAV,StreamPlatformVS,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate,UserReview

router=DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
     path('list/',WatchListAV.as_view(),name='movie-list'),
     path('<int:pk>/',WatchDetailAV.as_view() ,name='movie-detail'),
     path('list2/',WatchListGV.as_view() ,name='watch-list'),

      path('', include(router.urls)),
     # path('stream/',StreamPlatformAV.as_view(),name='stream-list'),
     # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),

     # path('review/',ReviewList.as_view(),name='review-list'),
     # path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),

     path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
     path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
     path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

     path('reviews//', UserReview.as_view(), name='review-detail'),
]