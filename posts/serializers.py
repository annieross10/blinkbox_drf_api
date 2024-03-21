class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    savedpost_count = serializers.ReadOnlyField()
    loves_count = serializers.SerializerMethodField()
    laughs_count = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_loves_count(self, obj):
        return Love.objects.filter(post=obj).count()

    def get_love_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            love = Love.objects.filter(owner=user, post=obj).first()
            return love.id if love else None
        return None

    def get_laughs_count(self, obj):
        return Laugh.objects.filter(post=obj).count()

    def get_laugh_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            laugh = Laugh.objects.filter(owner=user, post=obj).first()
            return laugh.id if laugh else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at',
            'title', 'content', 'image', 
            'like_id', 'likes_count', 'savedpost_count',
            'loves_count', 'laughs_count',
        ]
