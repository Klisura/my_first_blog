from .models import Post
from .models import Topic
def posts(request):
    return {'posts':Post.objects.all()}

def topics(request):
    return {'topics':Topic.objects.all()}