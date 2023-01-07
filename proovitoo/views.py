import datetime

from django.db.models import Sum, Count
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import HeaderForm, detail_formset_create_physical_person, detail_formset_update_physical_person, \
    detail_formset_update_judicial_person, detail_formset_create_judicial_person, detail_formset_view_judicial_person, \
    detail_formset_view_physical_person

from .models import Header, Detail


def index(request):
    company_list = Header.objects.order_by('reg_code')

    context = {
        'company_list': company_list
    }
    return render(request, 'proovitoo/index.html', context)


def create(request):
    if request.method == 'POST':

        form1 = HeaderForm(request.POST)

        formset_p = detail_formset_create_physical_person(request.POST, prefix="create_p")
        formset_j = detail_formset_create_judicial_person(request.POST, prefix="create_j")
        if form1.is_valid():

            f1 = form1.save(commit=False)
            search_string = ''
            for f in formset_p:
                if f.is_valid():
                    try:
                        search_string = search_string + str(f.cleaned_data['shareholder_first_name'])
                        search_string = search_string + " " + str(f.cleaned_data['shareholder_last_name'])
                        search_string = search_string + " " + str(f.cleaned_data['id_code'])
                    except:
                        pass

            for f in formset_j:
                if f.is_valid():
                    try:
                        search_string = search_string + str(f.cleaned_data['shareholder_company_reg_code'])
                        search_string = search_string + "; " + str(f.cleaned_data['shareholder_company_name'])
                    except:
                        pass

            f1.autofill_string = str(f1.reg_code) + " - " + str(f1.name)
            rc = f1.reg_code
            f1.search_string = search_string
            f1.save()

            for f in formset_p:
                f2 = f.save(commit=False)
                if f2.capital:
                    f2.reg_code = f1
                    f2.physical_person = True
                    f2.founder = True
                    f2.autofill_string = str(f2.id_code) + " - " + str(f2.shareholder_first_name) + " " + str(
                        f2.shareholder_last_name)
                    f2.save(f1)

            for f in formset_j:
                f3 = f.save(commit=False)
                if f3.capital:
                    f3.physical_person = False
                    f3.founder = True
                    f3.reg_code = f1
                    f3.save(f1)

            return HttpResponseRedirect("/detail="+rc)
        else:
            raise Exception("Some error")
    else:
        form1 = HeaderForm()
        form1.fields['create_date'].initial = datetime.date.today()
        formset_p = detail_formset_create_physical_person(queryset=Detail.objects.none(), prefix="create_p")
        formset_j = detail_formset_create_judicial_person(queryset=Detail.objects.none(), prefix="create_j")

    return render(request, 'proovitoo/create.html', {'form1': form1, 'formset_p': formset_p, 'formset_j': formset_j})


def update(request, reg_code):
    if request.method == 'POST':
        formset_update_p = detail_formset_update_physical_person(request.POST, prefix="update_p")
        formset_create_p = detail_formset_create_physical_person(request.POST, prefix="create_p")
        formset_update_j = detail_formset_update_judicial_person(request.POST, prefix="update_j")
        formset_create_j = detail_formset_create_judicial_person(request.POST, prefix="create_j")
        c = get_object_or_404(Header, pk=reg_code)
        company = HeaderForm(request.POST, instance=c)

        for fup in formset_update_p:
            if fup.is_valid():
                fup.save()
            else:
                print(fup.errors)
        for fuj in formset_update_j:
            if fuj.is_valid():
                fuj.save()
            else:
                print(fuj.errors)

        for fcp in formset_create_p:
            if fcp.is_valid():
                search_string = str(fcp.cleaned_data['shareholder_first_name'])
                search_string = search_string + "; " + str(fcp.cleaned_data['shareholder_last_name'])
                search_string = search_string + "; " + str(fcp.cleaned_data['id_code'])
                f1 = fcp.save(commit=False)
                if f1.capital:
                    f1.search_string = search_string
                    f1.founder = False
                    f1.physical_person = True
                    f1.reg_code = c
                    f1.save(c)

        for fcj in formset_create_j:
            if fcj.is_valid():
                search_string = str(fcj.cleaned_data['shareholder_company_reg_code'])
                search_string = search_string + "; " + str(fcj.cleaned_data['shareholder_company_name'])
                f2 = fcj.save(commit=False)
                if f2.capital:
                    f2.search_string = search_string
                    f2.founder = False
                    f2.physical_person = False
                    f2.reg_code = c
                    f2.save(c)

        if company.is_valid():
            c = company.save(commit=False)
            c.search_string = str(c.search_string) + "; " + search_string
            c.save()

        return redirect('/detail=' + reg_code + '/')

    else:
        company = get_object_or_404(Header, pk=reg_code)
        formset_update_p = detail_formset_update_physical_person(queryset=Detail.objects.filter(reg_code=reg_code,
                                                                                                physical_person=True),
                                                                 prefix="update_p")
        formset_create_p = detail_formset_create_physical_person(queryset=Detail.objects.none(), prefix="create_p")
        formset_update_j = detail_formset_update_judicial_person(queryset=Detail.objects.filter(reg_code=reg_code,
                                                                                                physical_person=False),
                                                                 prefix="update_j")
        formset_create_j = detail_formset_create_judicial_person(queryset=Detail.objects.none(), prefix="create_j")

    return render(request, 'proovitoo/update.html',
                  {'formset_update_p': formset_update_p, 'formset_create_p': formset_create_p,
                   'formset_update_j': formset_update_j, 'formset_create_j': formset_create_j, 'company': company})


def detail(request, reg_code):
    company = get_object_or_404(Header, pk=reg_code)
    detail_p = detail_formset_view_physical_person(queryset=Detail.objects.filter(reg_code=reg_code,
                                                                                  physical_person=True),
                                                   prefix="detail_p")
    detail_j = detail_formset_view_judicial_person(queryset=Detail.objects.filter(reg_code=reg_code,
                                                                                  physical_person=False),
                                                   prefix="detail_j")
    share_capital = str(Detail.objects.filter(reg_code=reg_code).aggregate(Sum('capital'))["capital__sum"]) + " EUR"
    return render(request, 'proovitoo/detail.html', {'company': company, 'detail_p': detail_p,
                                                     'share_capital': share_capital, 'detail_j': detail_j})


def reg_code_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = Header.objects.filter(reg_code__startswith=q).values_list('autofill_string', flat=True).distinct()
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")


def id_code_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = Detail.objects.filter(id_code__startswith=q).values_list('autofill_string', flat=True).distinct()
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")
