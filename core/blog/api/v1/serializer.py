from rest_framework import serializers
from ...models import Post,Category
from accounts.models import Profile

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']
    
class PostSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source='get_snippet')
    relaiteve_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    # The code below is to show the url for postdetails of each post
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model= Post
        fields = ['id','author','image','title','content','category','snippet','status','relaiteve_url','absolute_url','created_date','published_date']
        read_only_fields = ['author']
        # read_only_fields = ['content']
    # The function is to show the url for postdetails of each post
    def get_abs_url(self,obj):
        request = self.context.get('request')            
        return request.build_absolute_uri(obj.pk)
    '''
    This function is for when we want to make a change in the displayed data, not in 
    sending the data or making a change in the displayed data in the postlist with detailedlist.
    '''
    def to_representation(self, instance):
        request = self.context.get('request')
        print(request.__dict__)
        rep = super().to_representation(instance)
        #Detection of a request for a list of items or an item
        '''
        parser_context': {'view': <blog.api.v1.views.PostViewSet object at 
        0x7fc8033a5b10>, 'args': (), 'kwargs': {'pk': '2'}
        '''
        # PostDetail 
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet',None)
            rep.pop('relaiteve_url',None)
            rep.pop('absolute_url',None)
        # PostList    
        else:
            rep.pop('content',None)
        # The code below to show the category name in each post instead of the id field
        rep['category'] = CategorySerializer(instance.category,context={'request':request}).data
        return rep
    
    '''
    This function is for that when creating a post, there is no need to enter the author,
    and the email account with which we entered the site is automatically placed in the author field.
    '''
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)    
        
