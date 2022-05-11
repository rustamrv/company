from django.http import HttpResponse
from django.shortcuts import render
from .models import Employees
from django.db.models import Q
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ViewList(View):

    def get(self, request):
        if request.method == 'GET':
            pos = Employees.objects.all().order_by('department')
            page = request.GET.get('page')
            if page is None:
                page = 1
            paginator = Paginator(pos, 50)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                data = paginator.page(paginator.num_pages)

            content = {
                "data": data,
                'page': page
            }
            return render(request, "employees/employees.html", content)

    @staticmethod
    def search_list(request):
        if request.method == 'GET':
            search = request.GET.get('search')

            pos = Employees.objects.filter(Q(name=search) | Q(surname=search)
                                           | Q(position__name=search) | Q(department__name=search))

            page = request.GET.get('page')
            if page is None:
                page = 1
            paginator = Paginator(pos, 50)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                data = paginator.page(paginator.num_pages)

            content = {
                "data": data,
                'page': page
            }
            return render(request, "employees/employees_search.html", content)

    @staticmethod
    def sort(request):
        if request.method == 'GET':
            sort_by = request.GET.get('sort_by')
            pos = Employees.objects.all().order_by(sort_by)
            page = request.GET.get('page')
            if page is None:
                page = 1
            paginator = Paginator(pos, 50)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                data = paginator.page(paginator.num_pages)

            content = {
                "data": data,
                'page': page
            }
            return render(request, "employees/employees.html", content)

    @staticmethod
    def get_detail(request, id):
        try:
            content = Employees.objects.get(id=id)
        except Employees.DoesNotExist:
            raise HttpResponse("Employees does not exist")

        return render(request, 'employees/employees_details.html', {'instance': content})
