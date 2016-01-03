from rest_framework import routers
from context.apps.articles.views import ArticleViewSet, PublisherViewSet
from context.apps.feeds.views import GlobalFeedViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='article')
router.register(r'publishers', PublisherViewSet, base_name='publisher')
router.register(r'feeds', GlobalFeedViewSet, base_name='feed')
