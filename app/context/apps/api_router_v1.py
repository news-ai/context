from rest_framework import routers
from context.apps.articles.views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
