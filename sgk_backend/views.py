import json
import time
from django.shortcuts import render

# Create your views here.
import json
from .models import Group,Account
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

# 默认查询前10条数据
def default_query(request):
    groups = Group.objects.all()[:10]
    list_groups = []
    for group in groups:
        dict_group = {
            'QunNum': group.QunNum,
            'MastQQ': group.MastQQ,
            'CreateDate': group.CreateDate,
            'Title': group.Title,
            'Class': group.Class,
            'QunText': group.QunText
        }
        list_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(list_groups, safe=False)
    return response


def query_by_QunNum(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    group = Group.objects.get(QunNum=index)
    dict_group = {
        'QunNum': group.QunNum,
        'MastQQ':group.MastQQ,
        'CreateDate':group.CreateDate,
        'Title':group.Title,
        'Class':group.Class,
        'QunText':group.QunText
    }
    # 返回一个json
    response = JsonResponse(dict_group)
    return response

def query_by_CreateDate(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    groups = Group.objects.filter(CreateDate=index)
    list_groups = []
    for group in groups:
        dict_group = {
            'QunNum': group.QunNum,
            'MastQQ':group.MastQQ,
            'CreateDate':group.CreateDate,
            'Title':group.Title,
            'Class':group.Class,
            'QunText':group.QunText
        }
        list_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(list_groups,safe=False)
    return response

def query_by_Title(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果 icontains实现模糊查询
    groups = Group.objects.filter(Title__icontains=index)
    list_groups = []
    for group in groups:
        dict_group = {
            'QunNum': group.QunNum,
            'MastQQ':group.MastQQ,
            'CreateDate':group.CreateDate,
            'Title':group.Title,
            'Class':group.Class,
            'QunText':group.QunText
        }
        list_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(list_groups,safe=False)
    return response

def query_by_QunText(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果  icontains实现模糊查询
    groups = Group.objects.filter(QunText__icontains=index)
    list_groups = []
    for group in groups:
        dict_group = {
            'QunNum': group.QunNum,
            'MastQQ':group.MastQQ,
            'CreateDate':group.CreateDate,
            'Title':group.Title,
            'Class':group.Class,
            'QunText':group.QunText
        }
        list_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(list_groups,safe=False)
    return response


# QQ号部分！
# 默认查询前10条数据
def default_query2(request):
    accounts = Account.objects.all()[:10]
    accounts_groups = []
    for account in accounts:
        dict_group = {
            'QQNum': account.QQNum,
            'Nick': account.Nick,
            'Age': account.Age,
            'Gender': account.Gender,
            'Auth': account.Auth,
            'QunNum': account.QunNum
        }
        accounts_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    print(accounts)
    response = JsonResponse(accounts_groups, safe=False)
    return response

def query_by_QQNum(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    account = Account.objects.get(QQNum=index)
    dict_group = {
        'QQNum': account.QQNum,
        'Nick': account.Nick,
        'Age': account.Age,
        'Gender': account.Gender,
        'Auth': account.Auth,
        'QunNum': account.QunNum
    }
    # 返回一个json
    response = JsonResponse(dict_group)
    return response

def query_by_Nick(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    accounts = Account.objects.filter(Nick__icontains=index)
    accounts_groups = []
    for account in accounts:
        dict_group = {
            'QQNum': account.QQNum,
            'Nick': account.Nick,
            'Age': account.Age,
            'Gender': account.Gender,
            'Auth': account.Auth,
            'QunNum': account.QunNum
        }
        accounts_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(accounts_groups, safe=False)
    return response

def query_by_Age(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    accounts = Account.objects.filter(Age=index)
    accounts_groups = []
    for account in accounts:
        dict_group = {
            'QQNum': account.QQNum,
            'Nick': account.Nick,
            'Age': account.Age,
            'Gender': account.Gender,
            'Auth': account.Auth,
            'QunNum': account.QunNum
        }
        accounts_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(accounts_groups, safe=False)
    return response

def query_by_QunNum2(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    accounts = Account.objects.filter(QunNum=index)
    accounts_groups = []
    for account in accounts:
        dict_group = {
            'QQNum': account.QQNum,
            'Nick': account.Nick,
            'Age': account.Age,
            'Gender': account.Gender,
            'Auth': account.Auth,
            'QunNum': account.QunNum
        }
        accounts_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(accounts_groups, safe=False)
    return response

def analyzeQQNum(request):
    # 获取查询的值
    index = request.POST.get('index')
    # 得到查询的结果
    accounts = Account.objects.filter(QunNum=index)
    accounts_groups = []
    for account in accounts:
        dict_group = {
            'QQNum': account.QQNum,
            'Nick': account.Nick,
            'Age': account.Age,
            'Gender': account.Gender,
        }
        accounts_groups.append(dict_group)
    # 返回一个json(不是列表格式的)
    response = JsonResponse(accounts_groups, safe=False)
    return response

