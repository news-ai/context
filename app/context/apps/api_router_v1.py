from rest_framework import routers
from context.apps.articles.views import ArticleViewSet, PublisherViewSet
from context.apps.feeds.views import GlobalFeedViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'feeds', GlobalFeedViewSet, base_name='feeds')
