from django.shortcuts import render, get_object_or_404, redirect
from .models import Kriteria, Supplier
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .BWMMARCOS import BWM, MARCOS
from django.http import HttpResponseBadRequest
# from ..blog.models import 

def home(request):
     return render(request, 'home.html', {'active_page': 'home'})

# def about(request):
#      return render(request, 'about.html', {'active_page': 'about'})

# CRUD KRITERIA
@login_required(login_url='/login')
def view_kriteria(request):
     kriteria_list = Kriteria.objects.filter(user=request.user)
     return render(request, 'inner/BWM-MARCOS/kriteria/index.html', {'title':'List of Criteria Page', 'kriteria_list': kriteria_list})


@login_required(login_url='/login')
def create_kriteria(request):
     if request.method == 'POST':
          nama_kriteria = request.POST.get('nama_kriteria')
          jenis_kriteria = request.POST.get('jenis_kriteria')

          if Kriteria.objects.filter(user=request.user, nama_kriteria=nama_kriteria).exists() or \
             Kriteria.objects.filter(user=request.user, user_specific_kode_kriteria__icontains=f"{request.user.id}-{nama_kriteria}").exists():
               messages.error(request, 'The criteria with this name already exist.')
          else:
               Kriteria.objects.create(user=request.user, nama_kriteria=nama_kriteria, jenis_kriteria=jenis_kriteria)
               messages.success(request, 'The criteria have been successfully created')
               return redirect('view_kriteria')

     return render(request, 'inner/BWM-MARCOS/kriteria/create.html', {'title': 'Create Criteria Page'})


@login_required(login_url='/login')
def edit_kriteria(request, pk):
     if pk is None:
          return HttpResponseBadRequest("Data criteria is not valid")

     try:
          kriteria = get_object_or_404(Kriteria, pk=pk, user=request.user)
     except ValueError:
          return HttpResponseBadRequest("Data criteria is not valid")
     
     if request.method == 'POST':
          nama_kriteria = request.POST.get('nama_kriteria')
          jenis_kriteria = request.POST.get('jenis_kriteria')

          existing_kriteria = Kriteria.objects.exclude(pk=kriteria.pk)

          if existing_kriteria.filter(user=request.user, nama_kriteria=nama_kriteria).exists() or \
             existing_kriteria.filter(user=request.user, user_specific_kode_kriteria__icontains=f"{request.user.id}-{nama_kriteria}").exists():
               messages.error(request, 'The criteria with this name already exists.')
          if not messages.get_messages(request):
               kriteria.nama_kriteria = nama_kriteria
               kriteria.jenis_kriteria = jenis_kriteria
               kriteria.save()
               messages.success(request, 'Criteria changed successfully')
               return redirect('view_kriteria')

     return render(request, 'inner/BWM-MARCOS/kriteria/edit.html', {'title': 'Edit Criteria Page', 'kriteria': kriteria})

@login_required(login_url='/login')
def delete_kriteria(request, pk):
     if pk is None:
          return HttpResponseBadRequest("Data criteria is not valid")

     try:
          kriteria = get_object_or_404(Kriteria, pk=pk, user=request.user)
     except ValueError:
          return HttpResponseBadRequest("Data criteria is not valid")
     

     if request.method == 'POST':
          kriteria.delete()
          messages.success(request, 'Criteria successfully deleted')
          return redirect('view_kriteria')
     return redirect('view_kriteria')

# CRUD Supplier
@login_required(login_url='/login')
def view_supplier(request):
     supplier_list = Supplier.objects.filter(user=request.user)
     return render(request, 'inner/supplier/index.html', {'title':'List of Supplier Page', 'supplier_list': supplier_list})

@login_required(login_url='/login')
def create_supplier(request):
     if request.method == 'POST':
          nama = request.POST.get('nama')
          alamat = request.POST.get('alamat')
          nomor_telepon = request.POST.get('nomor_telepon')

          if Supplier.objects.filter(user=request.user, nama=nama).exists():
               messages.error(request, 'The name already exists.')
          else:
               Supplier.objects.create(user=request.user, nama=nama, alamat=alamat, nomor_telepon=nomor_telepon)
               messages.success(request, 'The supplier has been successfully created')
               return redirect('view_supplier')

     return render(request, 'inner/supplier/create.html', {'title':'Create Supplier Page'})

@login_required(login_url='/login')
def edit_supplier(request, pk):
     if pk is None:
          return HttpResponseBadRequest("Data supplier is not valid")

     try:
          supplier = get_object_or_404(Supplier, pk=pk, user=request.user)
     except ValueError:
          return HttpResponseBadRequest("Data supplier is not valid")

     if request.method == 'POST':
          nama = request.POST.get('nama')
          alamat = request.POST.get('alamat')
          nomor_telepon = request.POST.get('nomor_telepon')

          existing_supplier = Supplier.objects.exclude(pk=supplier.pk)

          if existing_supplier.filter(user=request.user, nama=nama).exists():
               messages.error(request, 'The supplier with this name already exists.')
          if not messages.get_messages(request):
               supplier.nama = nama
               supplier.alamat = alamat
               supplier.nomor_telepon = nomor_telepon
               supplier.save()
               messages.success(request, 'Supplier changed successfully')
               return redirect('view_supplier')

     return render(request, 'inner/supplier/edit.html', {'title':'Edit Supplier Page', 'supplier': supplier})

@login_required(login_url='/login')
def delete_supplier(request, pk):
     if pk is None:
          return HttpResponseBadRequest("Data supplier is not valid")

     try:
          supplier = get_object_or_404(Supplier, pk=pk, user=request.user)
     except ValueError:
          return HttpResponseBadRequest("Data supplier is not valid")
     

     if request.method == 'POST':
          supplier.delete()
          messages.success(request, 'Supplier successfully deleted')
          return redirect('view_supplier')





#PERHITUNGAN
@login_required(login_url='/login')
def select_kriteria(request):
     if request.method == 'POST':
          print("TAHAP INPUT PART 1")
          print(request.POST)
          selected_kriteria_list = request.POST.getlist('selected_kriteria')
          selected_supplier_list = request.POST.getlist('selected_supplier')
          
          if len(selected_kriteria_list) < 3 or len(selected_kriteria_list) > 9:
               messages.error(request, 'Choose at least 3 criteria and at most 9 criteria')
               return redirect('select_kriteria')
          elif len(selected_supplier_list) < 2:
               messages.error(request, 'Choose at least 2 supplier')
               return redirect('select_kriteria')
          
          selected_kriteria_data = Kriteria.objects.filter(id__in=selected_kriteria_list)
          selected_supplier_data = Supplier.objects.filter(id__in=selected_supplier_list)
          
          return render(request, 'inner/BWM-MARCOS/Perhitungan/index.html', {'title': 'Calculation Page Step 2', 'selected_kriteria_data': selected_kriteria_data,'selected_supplier_data': selected_supplier_data})
          
     else :
          kriteria_list = Kriteria.objects.filter(user=request.user)
          supplier_list = Supplier.objects.filter(user=request.user)

          if len(kriteria_list) < 3:
               messages.error(request, 'The number of criteria must be at least 3 to perform calculations.')
               return redirect('view_kriteria')
          elif len(supplier_list) < 2:
               messages.error(request, 'The number of supplier must be at least 2 so it can compare to perform calculation.')
               return redirect('view_supplier')
          return render(request, 'inner/BWM-MARCOS/Perhitungan/select.html', {'title': 'Calculation Page Step 1', 'kriteria_list': kriteria_list, 'supplier_list': supplier_list})

@login_required(login_url='/login')
def input_kriteria(request):
     if request.method == 'POST':
          print(request.POST)
          print(f"selected_kriteria_data = {request.POST.getlist('selected_kriteria_data')}")
          print(f"selected_supplier_data = {request.POST.getlist('selected_supplier_data')}")
          
          filtered_kriteria_data = request.POST.getlist('selected_kriteria_data')
          filtered_supplier_data = request.POST.getlist('selected_supplier_data')
          
          selected_kriteria_data = Kriteria.objects.filter(id__in=filtered_kriteria_data)
          selected_supplier_data = Supplier.objects.filter(id__in=filtered_supplier_data)
          for kriteria in selected_kriteria_data:
               print(f"Selected Kriteria ID: {kriteria.id}, Name: {kriteria.nama_kriteria}")
          for kriteria in selected_supplier_data:
               print(f"Selected Kriteria ID: {kriteria.id}, Name: {kriteria.nama}")
          
          best_kriteria = request.POST.get('best_kriteria')
          worst_kriteria = request.POST.get('worst_kriteria')
          
          if best_kriteria == worst_kriteria:
               messages.error(request, 'Best criteria and worst criteria cannot be the same.')
               best_kriteria = False
               worst_kriteria = False
          

          return render(request, 'inner/BWM-MARCOS/Perhitungan/index.html', {
               'title': 'Calculation Page Step 2', 
               'selected_kriteria_data': selected_kriteria_data, 
               'selected_supplier_data': selected_supplier_data,
               'best': best_kriteria,
               'worst': worst_kriteria,
               })
     return render(request, 'inner/BWM-MARCOS/Perhitungan/index.html')


@login_required(login_url='/login')
def result(request):
     if request.method == 'POST':
          print(request.POST)
          filtered_kriteria_data = request.POST.getlist('selected_kriteria_data')
          filtered_supplier_data = request.POST.getlist('selected_supplier_data')
          
          kriteria_list = Kriteria.objects.filter(id__in=filtered_kriteria_data)
          supplier_list = Supplier.objects.filter(id__in=filtered_supplier_data)
          
          # kriteria_list = Kriteria.objects.filter(user=request.user)
          # supplier_list = Supplier.objects.filter(user=request.user)
          print(f"kriteria_list = {kriteria_list}")
          print(f"supplier_list = {supplier_list}")

          # BWM
          nama_kriteria_values = [kriteria.nama_kriteria for kriteria in kriteria_list]
          
          bobot_kriteria_best_values = request.POST.getlist('bobot_kriteria_best')
          bobot_kriteria_worst_values = request.POST.getlist('bobot_kriteria_worst')
          
          pairs1 = zip(nama_kriteria_values, bobot_kriteria_best_values)
          pairs2 = zip(nama_kriteria_values, bobot_kriteria_worst_values)

          compared2best = {name: int(value) for name, value in pairs1}
          compared2worst = {name: int(value) for name, value in pairs2}

          print(f"compared2best = {compared2best}")
          print(f"compared2worst = {compared2worst}")
          
          weight_dict, zeta = BWM(compared2best, compared2worst)
          
          #MARCOS
          num_variables_data = request.POST.getlist('numVariables')
          print(f"weight_dict = {weight_dict}")
          print(f"num_variables_data = {num_variables_data}")
          
          a,b,c,d,e,f,g,h,i,j,k,l = MARCOS(num_variables_data, supplier_list, kriteria_list, weight_dict)

          return render(request, 'inner/BWM-MARCOS/Perhitungan/result.html', {
               'title': 'Result of Calculation Page',
               'kriteria_list': kriteria_list,
               'supplier_list': supplier_list,
               'weight_dict': weight_dict,
               'consistency': zeta,
               'num_variables_data': num_variables_data,
               'bobot_kriteria_best_values': bobot_kriteria_best_values,
               'bobot_kriteria_worst_values': bobot_kriteria_worst_values,
               'result_data': a,
               'max_values': b,
               'min_values': c,
               'normalized_result_data': d,
               'weighted_result_data': e,
               'max_weighted_values': f,
               'min_weighted_values': g,
               'sum_max_weighted_values': h,
               'sum_min_weighted_values': i,
               'ki_values_per_supplier': j,
               'result_utility_dict': k,
               'result_with_rank': l
          })

     messages.error(request, 'You must input the best criteria, worst criteria, and the value first')
     return redirect('input_kriteria')






@login_required(login_url='/login')
def detail(request):
     return render(request, 'inner/BWM-MARCOS/detail/detail.html')

@login_required(login_url='/login')
def detail_BWMMARCOS(request):
     return render(request, 'inner/BWM-MARCOS/detail/detail_BWM.html')

@login_required(login_url='/login')
def detail_ILP(request):
     return render(request, 'inner/BWM-MARCOS/detail/detail_ILP.html')