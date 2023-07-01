from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Post,Category
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .serializer import *
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.shortcuts import get_object_or_404
from .permission import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import DefaultPagination
from .filters import ProductFilter
'''
@api_view(['GET', 'POST'])
def postList(request):
    if request.method == 'GET':        
        posts = Post.objects.filter(status=1)
        # many = true,means that more than one object will be displayed on the web page
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''


'''
@api_view(['GET', 'PUT','DELETE'])
def postDetail(request, id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'Detail': f'post {id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        post = Post.objects.get(pk=id)
        # The code below is to convert the post and the changes made in it to Json
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
    elif request.method == "DELETE":
        post = Post.objects.get(pk=id)
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)
'''


"""class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request):
        posts = Post.objects.filter(status=1)
        # many = true,means that more than one object will be displayed on the web page
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""
    
# class PostDetail(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self,request,id):
#         try:
#             post = Post.objects.get(pk=id)
#             serializer = self.serializer_class(post)
#             return Response(serializer.data)
#         except Post.DoesNotExist:
#             return Response({'Detail': f'post {id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     def put(self,request,id):
#         post = Post.objects.get(pk=id)
#         # The code below is to convert the post and the changes made in it to Json
#         serializer = self.serializer_class(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(request.data)
#     def delete(self,request,id):
#         post = Post.objects.get(pk=id)
#         post.delete()
#         return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)

# class PostViewSet(ViewSet):
#     queryset = Post.objects.all()
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def list(self, request):
#         serializers = self.serializer_class(self.queryset,many=True)
#         return Response(serializers.data)
    
#     def retrieve(self, request,pk=None):
#         post_object = get_object_or_404(self.queryset,pk=pk)
#         serializers = self.serializer_class(post_object)
#         return Response(serializers.data)
#     def update(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)


# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

    
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.filter(status=1)
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields = ['category', 'author','status']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination
    filterset_class = ProductFilter


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]