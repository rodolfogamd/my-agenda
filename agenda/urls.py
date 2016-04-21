from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from apps.contacts.rest import ContactsViewSet
from apps.projects.rest import ProjectsViewSet
from apps.skills.rest import SkillsViewSet
from apps.levels.rest import LevelViewSet
from apps.companies.rest import CompanyViewSet
from apps.teams.rest import TeamsViewSet
from apps.groups.rest import GroupsViewSet
from apps.mycontacts.views import MyContactsViewSet
from apps.mygroups.views import MyGroupsViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactsViewSet)
router.register(r'skills', SkillsViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'teams', TeamsViewSet)
router.register(r'groups', GroupsViewSet)
router.register(r'mycontacts', MyContactsViewSet)
router.register(r'mygroups', MyGroupsViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^browser/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
