from django.shortcuts import render
from .models import Employee
from django.contrib import messages
from django.db.models import Q


def index(request):
    employees = Employee.objects.all()
    search_query = ""
    if request.method == "POST":
        if "create" in request.POST:
            name = request.POST.get("name")
            clg = request.POST.get("clg")
            age = request.POST.get("age")
            passout = request.POST.get("pass")
            addr = request.POST.get("addr")
            phone = request.POST.get("phone")
            Employee.objects.create(
                ename=name,
                cname=clg,
                age=age,
                passout=passout,
                addr=addr,
                econtact=phone,
            )
            messages.success(request, "Student added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            student = Employee.objects.get(eid=id)
            student.ename = name
            student.save()
            messages.success(request, "student updated successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Employee.objects.get(eid=id).delete()
            messages.success(request, "student deleted successfully")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            employees = Employee.objects.filter(Q(eid__icontains=search_query))

    context = {"employees": employees, "search_query": search_query}
    return render(request, "index.html", context=context)
