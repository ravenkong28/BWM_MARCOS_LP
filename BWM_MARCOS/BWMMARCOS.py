from scipy.optimize import linprog
import numpy as np
from  collections import OrderedDict
import copy

def calculate_f_ki(ki_plus, ki_minus):
     f_ki_plus = ki_plus / (ki_minus + ki_plus)
     f_ki_minus = ki_minus / (ki_minus + ki_plus)
     
     f_ki = (ki_plus + ki_minus) / (1 + ((1 - f_ki_plus) / f_ki_plus) + ((1 - f_ki_minus) / f_ki_minus))

     return f_ki_plus, f_ki_minus, f_ki

def BWM(compared2best, compared2worst):
     cb = OrderedDict()
     cw = OrderedDict()
     allkeys = list(compared2best.keys())
     # allkeys = sorted(compared2best.keys());
     print(f"All keys sorted = {allkeys}\n\n")
     
     for kk in allkeys:
          cb[kk] = compared2best[kk]
          cw[kk] = compared2worst[kk]
          
     print(f"cb = {cb} \ncw = {cw} \n\n")
     
     colSize = np.size(allkeys)
     rowSize = 4*colSize-5
     mat = np.zeros((rowSize-1, colSize+1), dtype=np.double);
     
     print(f'ColSize = {colSize},  rowSize = {rowSize},\n mat = \n{mat}\n\n')
     
     bloc = 0; bkey=''
     wloc = 0; wkey=''
     #     get the best criteria location
     bkey =  min(compared2best, key=compared2best.get);
     print(f"{compared2best}\n get = {compared2best.get}\n\n")
     bloc = allkeys.index(bkey)
     
     print (f'bkey = {bkey}, bloc = {bloc}\n\n')
     
     # get the worst criteria location
     wkey = min(compared2worst, key=compared2worst.get)
     wloc = allkeys.index(wkey)
     
     
     print (f'wkey = {wkey}, wloc = {wloc}\n\n')
     
     cb_copy = cb.copy()
     
     print (f'cb_copy = {cb_copy}\n\n')
     
     cb_copy.pop(bkey, None)
     
     print (f'cb_copy now = {cb_copy}\n\n')
     tmpmat = np.zeros((len(cb_copy.keys()), colSize+1), dtype=np.double)
     tmpmat1 = np.zeros((len(cb_copy.keys()), colSize+1), dtype=np.double)
     
     
     print (f'tmpmat = {tmpmat},\ntmpmat1 = {tmpmat1},\n\n')
     for idx in np.arange(len(cb_copy.keys())):
          itmp = allkeys.index(list(cb_copy.keys())[idx])
          tmpmat[idx, bloc] = 1.0
          tmpmat[idx, itmp] = -cb_copy[list(cb_copy.keys())[idx]]
          tmpmat[idx, colSize] = -1.0
     # tmpmat1 = tmpmat.copy()
     for idx in np.arange(len(cb_copy.keys())):
          itmp = allkeys.index(list(cb_copy.keys())[idx])
          tmpmat1[idx, bloc] = -1.0
          tmpmat1[idx, itmp] = cb_copy[list(cb_copy.keys())[idx]]
          tmpmat1[idx, colSize] = -1.0
     
     print (f'AFTER\ntmpmat = {tmpmat},\ntmpmat1 = {tmpmat1},\n\n')
     mat[0:2*colSize-2,:] = np.concatenate((tmpmat, tmpmat1), axis=0)
     print(f'After mat= {mat}')
     
     #----------------------------------------------------------------------------------------
     cw_copy = cw.copy();
     
     print (f'cw_copy = {cw_copy}\n\n')
     
     cw_copy.pop(bkey, None);
     cw_copy.pop(wkey, None);
     
     print (f'cw_copy now = {cw_copy}\n\n')
     
     tmpmat  = np.zeros((len(cw_copy.keys()), colSize+1), dtype=np.double);
     tmpmat1 = np.zeros((len(cw_copy.keys()), colSize+1), dtype=np.double);
     for idx in np.arange(len(cw_copy.keys())):  
          itmp = allkeys.index(list(cw_copy.keys())[idx]);
          tmpmat[idx, itmp] = 1;
          tmpmat[idx, wloc] = -cw_copy[list(cw_copy.keys())[idx]];
          tmpmat[idx, colSize] = -1.0;
     for idx in np.arange(len(cw_copy.keys())):  
          itmp = allkeys.index(list(cw_copy.keys())[idx]);
          tmpmat1[idx, itmp] = -1;
          tmpmat1[idx, wloc] = cw_copy[list(cw_copy.keys())[idx]];
          tmpmat1[idx, colSize] = -1.0;
     mat[2*colSize-2:,:] = np.concatenate((tmpmat, tmpmat1), axis=0);
     Aeq = np.ones((1, colSize+1), dtype=np.double);
     Aeq[0,-1] = 0.;
     beq = np.array([1]); 
     bub = np.zeros((rowSize-1), dtype=np.double);
     cc = np.zeros((colSize+1), dtype=np.double)
     cc[-1] = 1; 
     res = linprog(cc, A_eq=Aeq, b_eq=beq, A_ub=mat, b_ub=bub, \
                    bounds=(0, None), options={"disp": False});
     sol1 = res['x']
     outp = dict()
     ii = 0
     for x in allkeys:
          outp[x] = np.asscalar(sol1[ii])
          ii += 1
     return(outp, np.asscalar(sol1[ii]))

def MARCOS(num_variables_data, supplier_list, kriteria_list, weight_dict):
     result_data = {}
     num_variables_iter = iter(num_variables_data)

     for supplier in supplier_list:
          supplier_data = {}
          for kriteria in kriteria_list:
               # Assign the value to the corresponding criterion for the current supplier
               supplier_data[kriteria.nama_kriteria] = next(num_variables_iter)

          result_data[supplier.nama] = supplier_data                         

          result_data[f'{supplier.nama}'] = supplier_data
     
     print("Original Result Data:")
     print(result_data)
     
     max_values = {}
     min_values = {}

     for criterion, kriteria in zip(result_data[supplier.nama].keys(), kriteria_list):
          criterion_values = [int(data[criterion]) for data in result_data.values()]

          if (kriteria.jenis_kriteria == "Benefit"):
               max_values[criterion] = max(criterion_values)
               min_values[criterion] = min(criterion_values)
          elif (kriteria.jenis_kriteria == "Cost"):
               max_values[criterion] = min(criterion_values)
               min_values[criterion] = max(criterion_values)

     # Print the results
     print("\nMax Values:")
     print(max_values)
     print("\nMin Values:")
     print(min_values)
     
     # Create a new dictionary for normalized values
     normalized_result_data = {}

     # Loop through each supplier in the original result data
     for supplier, data in result_data.items():
          normalized_supplier_data = {}

          # Loop through each criterion in the supplier data
          for criterion, value in data.items():
               # Normalize the value based on jenis_kriteria
               if kriteria_list.get(nama_kriteria=criterion).jenis_kriteria == "Benefit":
                    normalized_value = int(value) / max_values[criterion]
               elif kriteria_list.get(nama_kriteria=criterion).jenis_kriteria == "Cost":
                    normalized_value = max_values[criterion]/ int(value)
               
               normalized_supplier_data[criterion] = normalized_value

          normalized_result_data[supplier] = normalized_supplier_data

     print("\nNormalized Result Data:")
     print(normalized_result_data)
     
     
     weighted_result_data = {}
     weighted_result_data_copy = {}

     # Loop through each supplier in the original result data
     for supplier, data in normalized_result_data.items():
          weighted_supplier_data = {}

          # Loop through each criterion in the supplier data
          for criterion, normalized_value in data.items():
               # Multiply the normalized value by its corresponding weight
               weighted_value = normalized_value * weight_dict[criterion]

               weighted_supplier_data[criterion] = weighted_value

          # Create a copy of the data before modifying it
          weighted_supplier_data_copy = copy.deepcopy(weighted_supplier_data)

          # Add the 'total' key with the sum of values for the current supplier
          weighted_supplier_data['total'] = sum(weighted_supplier_data.values())

          # Store the modified data in the dictionaries
          weighted_result_data[supplier] = weighted_supplier_data
          weighted_result_data_copy[supplier] = weighted_supplier_data_copy

     print("\nWeighted Result Data:")
     print(weighted_result_data)
     print("\nWeighted Result Data Copy:")
     print(weighted_result_data_copy)
     
     max_weighted_values = {}
     min_weighted_values = {}

     for criterion in weighted_result_data_copy[next(iter(weighted_result_data_copy))].keys():
          # Extract values for the current criterion and convert them to floats
          criterion_values = [float(data[criterion]) for data in weighted_result_data_copy.values()]

          # Find the maximum and minimum values for the current criterion
          max_weighted_values[criterion] = max(criterion_values)
          min_weighted_values[criterion] = min(criterion_values)

     # Print the results
     print("Max Values (Copy):")
     print(max_weighted_values)
     print("\nMin Values (Copy):")
     print(min_weighted_values)
     
     sum_max_weighted_values = sum(max_weighted_values.values())         
     sum_min_weighted_values = sum(min_weighted_values.values())
     
     # Print the results
     print("Sum of Min Values:")
     print(sum_max_weighted_values)
     print("\nSum of Max Values:")
     print(sum_min_weighted_values)

     
     ki_values_per_supplier = {}

     for supplier, data in weighted_result_data.items():
          # Create a dictionary to store Ki+ and Ki- values for the current supplier
          ki_values = {}

          # Calculate Ki+ and Ki- for the 'total' criterion
          ki_plus_total = data['total'] / (sum_max_weighted_values)
          ki_minus_total = data['total'] / (sum_min_weighted_values)

          ki_values['total'] = {"Ki+": ki_plus_total, "Ki-": ki_minus_total}

          # Store the Ki+ and Ki- values for the current supplier
          ki_values_per_supplier[supplier] = ki_values

     # Print the Ki+ and Ki- values for each supplier
     print("\nKi+ and Ki- Values for Each Supplier:")
     print(ki_values_per_supplier)
     
     
     result_utility_dict = {}

     for supplier, ki_values in ki_values_per_supplier.items():
          ki_plus = ki_values['total']['Ki+']
          ki_minus = ki_values['total']['Ki-']

          f_ki_plus, f_ki_minus, f_ki = calculate_f_ki(ki_plus, ki_minus)

          supplier_result = {
               'ki+': f_ki_plus,
               'ki-': f_ki_minus,
               'ki': f_ki
          }

          result_utility_dict[supplier] = supplier_result

     print("\n\nresult_utility_dict")
     print(result_utility_dict)
     
     result_utility_dict_copy = copy.deepcopy(result_utility_dict)
     
     # Menambahkan peringkat berdasarkan nilai ki
     ranked_result = sorted(result_utility_dict_copy.items(), key=lambda x: x[1]['ki'], reverse=True)

     # Menghasilkan dictionary baru dengan tambahan peringkat
     result_with_rank = {}
     for rank, (supplier, values) in enumerate(ranked_result, start=1):
          result_with_rank[supplier] = {
               'ki': values['ki'],
               'rank': rank
          }
     # Menampilkan hasil
     print("\n\nresult_with_rank")
     print(result_with_rank)
     
     return result_data, max_values, min_values, normalized_result_data, weighted_result_data, max_weighted_values, min_weighted_values, sum_max_weighted_values, sum_min_weighted_values, ki_values_per_supplier, result_utility_dict, result_with_rank




