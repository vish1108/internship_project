from django.urls import path
from .views import TaskListCreateView, TaskDetailView, RecentCompletedTasksView
from django.urls import path
from rest_framework.documentation import include_docs_urls
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


urlpatterns = [
    path("", TaskListCreateView.as_view(), name="task-list-create"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("recent-completed/", RecentCompletedTasksView.as_view(), name="recent-completed"),
    path('docs/', include_docs_urls(title='Internship Project API')),
]


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Internship Project API",
#       default_version='v1',
#       description="API docs",
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

# urlpatterns += [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]
