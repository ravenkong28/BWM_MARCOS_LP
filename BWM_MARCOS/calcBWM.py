#!/usr/bin/env python3
#==========================================================================================
'''
Author: Ahsan Khan
This is simple function that generates the matrices required to be solved in the
Best Worst method and then solves the linear optimization problem using scipy linprog 
routine. This function accepts two dictionaries as inputs. One dictionary contains
the names of the parameters and corresponding scores compared to the BEST parameter.
The other dictionary similarly contains names of the parameters, and corresponding scores 
compared to the WORST parameter. This function does not check for input accuracy/consistency.
It outputs the calculated wight of each parameter as the first element of the tuple 
and return the weights in a dictionary in the form {parameter: weight}. The second element
of the tuple is the consistency index. 
 || This is just a prototype ||
'''
#==========================================================================================
from scipy.optimize import linprog
import numpy as np
from  collections import OrderedDict
import numpy as np


def calc_weight(compared2best, compared2worst):
     cb = OrderedDict();
     cw = OrderedDict();
     # allkeys = sorted(compared2best.keys());
     allkeys = list(compared2best.keys());
     print(f"All keys sorted = {allkeys}\n\n")
     
     for kk in allkeys:
          cb[kk] = compared2best[kk];
          cw[kk] = compared2worst[kk];
          
     print(f"cb = {cb} \ncw = {cw} \n\n")
     
     colSize = np.size(allkeys);
     rowSize = 4*colSize-5;
     mat = np.zeros((rowSize-1, colSize+1), dtype=np.double);
     
     print(f'ColSize = {colSize},  rowSize = {rowSize},\n mat = \n{mat}\n\n')
     
     bloc = 0; bkey='';
     wloc = 0; wkey='';
     #     get the best criteria location
     bkey =  min(compared2best, key=compared2best.get);
     print(f"{compared2best}\n get = {compared2best.get}\n\n")
     bloc = allkeys.index(bkey);
     
     print (f'bkey = {bkey}, bloc = {bloc}\n\n')
     
     # get the worst criteria location
     wkey = min(compared2worst, key=compared2worst.get);
     wloc = allkeys.index(wkey);
     
     
     print (f'wkey = {wkey}, wloc = {wloc}\n\n')
     
     cb_copy = cb.copy();
     
     print (f'cb_copy = {cb_copy}\n\n')
     '''delete the key corresponding to best critreia.
     The TWO equations corresponding to the best criterion
     do not appear in the system of equations when comparing all
     criteria against the best '''
     cb_copy.pop(bkey, None);
     
     print (f'cb_copy now = {cb_copy}\n\n')
     tmpmat = np.zeros((len(cb_copy.keys()), colSize+1), dtype=np.double);
     tmpmat1 = np.zeros((len(cb_copy.keys()), colSize+1), dtype=np.double);
     
     
     print (f'tmpmat = {tmpmat},\ntmpmat1 = {tmpmat1},\n\n')
     for idx in np.arange(len(cb_copy.keys())):
          itmp = allkeys.index(list(cb_copy.keys())[idx]);
          tmpmat[idx, bloc] = 1.0;
          tmpmat[idx, itmp] = -cb_copy[list(cb_copy.keys())[idx]];
          tmpmat[idx, colSize] = -1.0;
     # tmpmat1 = tmpmat.copy()
     for idx in np.arange(len(cb_copy.keys())):
          itmp = allkeys.index(list(cb_copy.keys())[idx]);
          tmpmat1[idx, bloc] = -1.0;
          tmpmat1[idx, itmp] = cb_copy[list(cb_copy.keys())[idx]];
          tmpmat1[idx, colSize] = -1.0;
     
     print (f'AFTER\ntmpmat = {tmpmat},\ntmpmat1 = {tmpmat1},\n\n')
     mat[0:2*colSize-2,:] = np.concatenate((tmpmat, tmpmat1), axis=0);
     print(f'After mat= {mat}')
     
     #----------------------------------------------------------------------------------------
     cw_copy = cw.copy();
     
     print (f'cw_copy = {cw_copy}\n\n')
     '''delete the two keys corresponding to best critreia and worst criteria.
     The FOUR equations corresponding to the best and worst criteria
     do not appear in the system of equations when comparing all
     criteria against the worst '''
     cw_copy.pop(bkey, None);
     cw_copy.pop(wkey, None);
     
     print (f'cw_copy now = {cw_copy}\n\n')
     
     tmpmat  = np.zeros((len(cw_copy.keys()), colSize+1), dtype=np.double);
     tmpmat1 = np.zeros((len(cw_copy.keys()), colSize+1), dtype=np.double);
     for idx in np.arange(len(cw_copy.keys())):  
          # find the location of the key of cw_copy in the keylist list
          itmp = allkeys.index(list(cw_copy.keys())[idx]);
          tmpmat[idx, itmp] = 1;
          tmpmat[idx, wloc] = -cw_copy[list(cw_copy.keys())[idx]];
          tmpmat[idx, colSize] = -1.0;
     for idx in np.arange(len(cw_copy.keys())):  
          # find the location of the key of cw_copy in the keylist list
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
          # outp[x] = np.asscalar(sol1[ii]);    
          outp[x] = sol1[ii].item();    
          ii += 1
     return((outp, sol1[ii].item()))



#==========================================================================================
#==========================================================================================
# compared2best  = dict({'quality':2, 'price':1, 'comfort':4,  'safety':3, 'style':8});
# compared2worst = dict({'quality':4, 'price':8, 'comfort':2,  'safety':3, 'style':1});


# compared2best  = dict({'price':1, 'mp':2, 'fps':7,  'iso':4, 'video':8, 'lensesco':2, 'conn':5})
# compared2worst = dict({'price':9, 'mp':5, 'fps':8,  'iso':3, 'video':1, 'lensesco':4, 'conn':5})

# compared2best  = dict({'quality':100, 'price':2, 'comfort':1})
# compared2worst = dict({'quality':1, 'price':5, 'comfort':100})

compared2best  = dict({'KB':1, 'DTB':2, 'JPB':4, 'JVB':8, 'HP':6, 'K':7})
compared2worst = dict({'KB':8, 'DTB':7, 'JPB':6, 'JVB':1, 'HP':4, 'K':2})


w, zeta = calc_weight(compared2best, compared2worst)
print(f"Weights: {w}\n")
print(f"sum(Weights): {np.sum(list(w.values()))}\n")
print('Consistency: {0}'.format(zeta))


