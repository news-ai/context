from rest_framework import routers
from context.apps.articles.views import ArticleViewSet, PublisherViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'publishers', PublisherViewSet)
