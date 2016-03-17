# Third-party app imports
from rest_framework import routers

# Imports from app
from .feeds.views import FeedViewSet
from .entities.views import TypeViewSet, EntityViewSet, EntityScoreViewSet
from .articles.views import (
    ArticleViewSet,
    AuthorViewSet,
    PublisherFeedViewSet,
    PublisherViewSet,
)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='article')
router.register(r'publishers', PublisherViewSet, base_name='publisher')
router.register(r'feeds', FeedViewSet, base_name='feeds')
router.register(r'authors', AuthorViewSet, base_name='author')
router.register(r'publisherfeeds', PublisherFeedViewSet,
                base_name='publisherfeed')
router.register(r'types', TypeViewSet, base_name='type')
router.register(r'entities', EntityViewSet, base_name='entity')
router.register(r'entityscores', EntityScoreViewSet, base_name='entityscore')
