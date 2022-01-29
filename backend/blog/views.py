from rest_framework import response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from blog.serializers import BlogpostSerializer
from blog.models import Blogpost

class BlogpostListView(ListAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.order_by('-date_created')
    permission_class = (permissions.AllowAny, )
    lookup_field = 'slug'

class BlogpostDetailView(RetrieveAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.order_by('-date_created')
    permission_class = (permissions.AllowAny, )
    lookup_field = 'slug'

class BlogpostFeaturedView(ListAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all().filter(featured=True)
    permission_class = (permissions.AllowAny, )
    lookup_field = 'slug'

class BlogpostCategoryView(APIView):
    serializer_class = BlogpostSerializer
    permission_class = (permissions.AllowAny, )

    def post(self,request,format = None):
        data = self.request.data
        category = data['category']
        queryset = Blogpost.objects.all().filter(category__iexact = category)

        serializer = BlogpostSerializer(queryset, many = True)
        return response(serializer.data)