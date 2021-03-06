"""koword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import ExamBookListView, ExamUnitListView, ExamWordListView, ExamFinishView, ExamRecordView

urlpatterns = [
    url(r'^booklist/$', ExamBookListView.as_view(), name='exam_booklist'),
    url(r'^unitlist/(?P<book_id>\d+)$', ExamUnitListView.as_view(), name='exam_unitlist'),
    url(r'^wordlist/(?P<book_id>\d+)/(?P<word_unit>\d+)$', ExamWordListView.as_view(), name='exam_wordlist'),
    url(r'^traverse/(?P<book_id>\d+)/(?P<word_unit>\d+)/(?P<user_id>\d+)$', ExamFinishView.as_view(), name='exam_traverse'),
    url(r'^record/$', ExamRecordView.as_view(), name='exam_record'),
]
