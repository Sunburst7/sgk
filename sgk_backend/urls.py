from django.urls import path

from . import views

urlpatterns = [
    # QQ群部分
    path('queryByNum', views.query_by_QunNum, name='query_by_QunNum'),
    path('queryByCreateDate',views.query_by_CreateDate,name='query_by_CreateDate'),
    path('queryByTitle',views.query_by_Title,name='query_by_Title'),
    path('queryByQunText',views.query_by_QunText,name='query_by_QunText'),
    path('defaultQuery',views.default_query),

    # QQ号部分路由
    path('defaultQuery2',views.default_query2),
    path('queryByQQNum',views.query_by_QQNum),
    path('queryByNick',views.query_by_Nick),
    path('queryByAge',views.query_by_Age),
    path('queryByQunNum',views.query_by_QunNum2),

    #数据分析部分
    path('analyzeQQNum',views.analyzeQQNum)
]