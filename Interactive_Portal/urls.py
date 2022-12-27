"""Interactive_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import details,detailsedit,education,educationedit,skills,skillsedit,experience,experienceedit,projects,projectsedit,awards,awardsedit,publications,publicationsedit,scholarships,scholarshipsedit,activities,activitiesedit,links,linksedit
# , highereducationaction, placementaction, profileaction
from login.views import loginaction
from home.views import activitiesadd,educationadd,skillsadd,experienceadd,projectsadd,awardsadd,publicationsadd,scholarshipsadd,linksadd
from home.views import home,mainProfile,certificatesadd,certificates,certificatesedit,profile,portfolio
from login.views import loginaction,logoutaction,adminlogout,adminlogin,adminpage
from signup.views import signaction,setting,changepassword,adminsignup

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/', adminlogin , name="adminlogin"),
    path('adminsignup/', adminsignup , name="adminsignup"),
    path('adminpage/', adminpage , name="adminpage"),
    path('adminlogout/',adminlogout,name="adminlogout"),
    path('login/',loginaction,name="login"),
    path('logout/',logoutaction,name="logout"),
    path('signup/',signaction,name="signup"),
    path('',home,name="home"),
    path('mainprofile/',mainProfile,name="mainprofile"),
    path('mainprofile/settings/',setting,name="setting"),
    path('mainprofile/settings/changepassword/',changepassword,name="changepassword"),
    path('profile/',profile,name="profile"),
    path('portfolio/',portfolio,name="portfolio"),
    path('profileedit/details/',detailsedit,name="detailsedit"),
    path('profile/details/',details,name="details"),
    path('profileedit/education/<str:id>/',educationedit,name="educationedit"),
    path('profile/education/',education,name="education"),
    path('profileadd/education/',educationadd,name="educationadd"),
    path('profileadd/experience/',experienceadd,name="experienceadd"),
    path('profileedit/experience/<str:id>/',experienceedit,name="experienceedit"),
    path('profile/experience/',experience,name="experience"),
    path('profileedit/skills/<str:id>/',skillsedit,name="skillsedit"),
    path('profileadd/skills/',skillsadd,name="skillsadd"),
    path('profile/skills/',skills,name="skills"),
    path('profileedit/projects/<str:id>/',projectsedit,name="projectsedit"),
    path('profile/projects/',projects,name="projects"),
    path('profileadd/projects/',projectsadd,name="projectsadd"),
    path('profileedit/awards/<str:id>/',awardsedit,name="awardsedit"),
    path('profile/awards/',awards,name="awards"),
    path('profileadd/awards/',awardsadd,name="awardsadd"),
    path('profileedit/publications/<str:id>/',publicationsedit,name="publicationsedit"),
    path('profile/publications/',publications,name="publications"),
    path('profileadd/publications/',publicationsadd,name="publicationsadd"),
    path('profileedit/scholarships/<str:id>/',scholarshipsedit,name="scholarshipsedit"),
    path('profile/scholarships/',scholarships,name="scholarships"),
    path('profileadd/scholarships/',scholarshipsadd,name="scholarshipsadd"),
    path('profileedit/activities/',activitiesadd,name="activitiesadd"),
    path('profileedit/activities/<str:id>/',activitiesedit,name="activitiesedit"),
    path('profile/activities/',activities,name="activities"),
    path('profileedit/links/<str:id>/',linksedit,name="linksedit"),
    path('profile/links/',links,name="links"),
    path('profileadd/links/',linksadd,name="linksadd"),
    path('profileadd/certificates/<str:name>/<str:id>/',certificatesadd,name="certificatesadd"),
    path('profile/certificates/<str:name>/<str:id>/',certificates,name="certificates"),
    path('profile/certificates/<str:name>/<str:id>/<str:cid>',certificatesedit,name="certificatesedit"),

    # path('profile/',profileaction,name="profile"),
    # path('placement/',placementaction,name="placement"),
    # path('highereducation/',highereducationaction,name="highereducation"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)