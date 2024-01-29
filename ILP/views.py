from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import lippy as lp
from .calc.gomory3 import gomory

@login_required(login_url='/login')
def lp_perhitungan(request):
     if request.method == 'POST':
          print(request.POST)
          numVariables = request.POST.get('numVariables')
          
          name_variable = [
               request.POST.get(f'name_variable[{j}]', 0) for j in range(int(numVariables))
          ]
          
          return render(request, 'inner/ILP/Perhitungan/indexLP2.html', {
               'title':'Input LP Page 2 of 2',          
               'numVariables' : numVariables,
               'name_variable' : name_variable,
          })

          
     return render(request, 'inner/ILP/Perhitungan/indexLP.html', {
          'title':'Input LP Page 1 of 2',
          })
     
     
@login_required(login_url='/login')
def lp_result(request):
     if request.method == 'POST':
          #Define variable and Constraint
          numVariables = request.POST.get('numVariables')
          numConstraints = 6 + int(numVariables)
          # print(f"numVariables = {numVariables} \n")
          # print(f"numConstraints {numConstraints}\n")
          
          name_variable = request.POST.getlist('name_variable') 
          # print(f"name_variable = {name_variable} \n")
          
          
          ##VARIABLES VALUE
          supplier_1_values_max = [-1 if flower_type in request.POST.getlist('supplier_1') else 0 for flower_type in name_variable]
          supplier_2_values_max = [-1 if flower_type in request.POST.getlist('supplier_2') else 0 for flower_type in name_variable]
          supplier_3_values_max = [-1 if flower_type in request.POST.getlist('supplier_3') else 0 for flower_type in name_variable]
          supplier_1_values_min = [1 if flower_type in request.POST.getlist('supplier_1') else 0 for flower_type in name_variable]
          supplier_2_values_min = [1 if flower_type in request.POST.getlist('supplier_2') else 0 for flower_type in name_variable]
          supplier_3_values_min = [1 if flower_type in request.POST.getlist('supplier_3') else 0 for flower_type in name_variable]

          identity_matrix = [[1 if j == i else 0 for j in range(int(numVariables))] for i in range(int(numVariables))]
          print(f"identity_matrix = {identity_matrix} \n")

          combined_variables = [supplier_1_values_max, supplier_2_values_max, supplier_3_values_max, supplier_1_values_min, supplier_2_values_min, supplier_3_values_min ] + identity_matrix
     
          print(f"combined_variables = {combined_variables} \n")
          
          
          ##variables_objective VALUE
          variables_objective = [-1 * int(val) for val in request.POST.getlist('variables_objective')]
          print(f"variables_objective = {variables_objective} \n")
          
          
          ##RHS VALUE
          rhs_min = request.POST.getlist('accomodate_value_rhs_min')
          for i in range(3):
               rhs_min[i] = str(-1 * int(rhs_min[i]))
          rhs_max = request.POST.getlist('accomodate_value_rhs_max')
          
          rhs = request.POST.getlist('accomodate_value_rhs')
          
          combined_rhs = [rhs_min + rhs_max + rhs]
          print(f"combined_rhs = {combined_rhs}")
          
          notfound = False
          result = 0
          solution_variable=0
          solution, simplex, dual, text = gomory(int(numVariables), int(numConstraints), combined_rhs, variables_objective, combined_variables)
          if(text != "No feasible solution exists"):
               result = sum(x * y for x, y in zip(variables_objective, solution))
               result *= -1
               print(f"solution = {solution},\nname_variable = {name_variable}\n\n")
               solution_variable = list(zip(name_variable, solution))
               print(f"solution_variable = {solution_variable}\n\n")
          else :
               notfound = True
               
          return render(request, 'inner/ILP/Perhitungan/resultLP.html', {
               'title': 'Result of Calculation Linear Programming Page',
               'result': result,
               'solution_variable' : solution_variable,
               'notfound' : notfound
          })
          