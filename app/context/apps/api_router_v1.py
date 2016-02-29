# Third-party app imports
from rest_framework import routers

# Imports from app
from .feeds.views import GlobalFeedViewSet
from .articles.views import (
    ArticleViewSet,
    AuthorViewSet,
    PublisherFeedViewSet,
    PublisherViewSet,
)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='article')
router.register(r'publishers', PublisherViewSet, base_name='publisher')
router.register(r'feeds', GlobalFeedViewSet, base_name='feed')
router.register(r'authors', AuthorViewSet, base_name='author')
router.register(r'publisherfeeds', PublisherFeedViewSet,
                base_name='publisherfeed')
