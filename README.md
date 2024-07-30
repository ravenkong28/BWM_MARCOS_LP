# Project Explanation: BWM-MARCOS Application for Decision-Making Systems and Linear Programming

## Introduction

The BWM-MARCOS application is a web-based platform designed to support decision-making and optimization by integrating the Best Worst Method (BWM) and Measurement of Alternatives and Ranking According to Compromise Solution (MARCOS) methods. This application aims to provide efficient solutions for complex decision-making and resource planning.

## Key Features

### 1. Decision-Making System with BWM-MARCOS

#### BWM-MARCOS Method

BWM-MARCOS is a combination of two methods: Best Worst Method (BWM) and Measurement of Alternatives and Ranking According to Compromise Solution (MARCOS). This method operates in the realm of Multi-Criteria Decision Making (MCDM) with the goal of evaluating a set of alternatives based on a set of decision criteria. BWM involves systematic pairwise comparisons of decision criteria, while MARCOS focuses on defining relationships between alternatives and reference values (ideal and anti-ideal alternatives).

By combining the BWM and MARCOS concepts, this method generates utility values for the considered alternatives, calculated based on these relationships. A compromise ranking is formulated concerning the ideal utility function.

MARCOS is a relatively new and straightforward MCDM technique that can be applied in various fields, such as supplier selection in the healthcare industry.

#### Best Worst Method (BWM)

The Best Worst Method (BWM), introduced by Dr. Jafar Rezaei in 2015, addresses limitations found in commonly used MCDM methods such as the Analytic Hierarchy Process (AHP), which may produce inconsistent pairwise comparison matrices.

BWM overcomes these challenges by comparing criteria systematically using a different approach. Dr. Jafar Rezaei's approach involves several stages:

1. **Identify Criteria**: The decision-maker initially identifies the relevant criteria for the problem at hand, forming a set of criteria \(\{c_1, c_2, \ldots, c_n\}\) that affect the decision.
2. **Select Best and Worst Criteria**: The decision-maker then selects two criteria labeled as the best and worst criteria from the identified criteria. The best criterion is the most important in the decision-making process, while the worst criterion is the least important.
3. **Compare Other Criteria with the Best and Worst Criteria**: The decision-maker then provides preferences in the form of pairwise comparison values between the best criterion and other criteria, as well as between all criteria and the worst criterion. These comparisons use a numeric scale from 1 to 9.

   The results of these pairwise comparison values are formalized into equations, where \( A_{Bn} \) represents the preference value of the best criterion for criterion \( n \), and \( A_{nW} \) represents the preference value of criterion \( n \) for the worst criterion. The preference comparison stages are formalized into equations and optimization models to determine the optimal weights for each criterion.

### 2. Measurement of Alternatives and Ranking According to Compromise Solution (MARCOS)

MARCOS is a method used to evaluate a set of alternatives concerning a set of decision criteria. This method is based on defining relationships between alternatives and reference values (ideal and anti-ideal alternatives).

Based on these relationships, the utility function of the considered alternatives is computed, and the compromise ranking is formulated concerning the ideal utility function. MARCOS is a relatively new and straightforward MCDM technique that can be applied in various fields, such as supplier selection in the healthcare industry.

#### Steps in MARCOS Calculation:

1. **Form Initial Decision Matrix**: Create an initial decision matrix consisting of several alternatives and criteria.
2. **Form Extended Decision Matrix**: Expand the initial matrix by defining the ideal (AI) and anti-ideal (AAI) solutions.

   The anti-ideal solution (AAI) represents the worst alternative, while the ideal solution (AI) is the best alternative. Based on the type of criteria, AAI and AI are calculated using the relevant equations.

3. **Normalize the Matrix (\(N\))**: The normalized matrix \(N = [n_{ij}]_{m \times n}\) elements are produced using normalization equations based on the type of criteria.

4. **Form Weighted Decision Matrix (\(V\))**: Calculate the weighted matrix \(V\) by multiplying the normalized matrix with weight coefficients \(w_j\).

5. **Compute Alternative Utility Values (\(K_i\))**: Compute the utility values of alternatives concerning the anti-ideal and ideal solutions using specific equations.

6. **Determine Utility Function for Alternatives (\(f(K_i)\))**: The utility function is the compromise of the observed alternatives concerning the ideal and anti-ideal solutions. The utility function for alternative \(f(K_i)\) is defined based on computed values.

7. **Rank Alternatives**: Rank alternatives based on the utility function values; higher values indicate higher rankings.

## Linear Programming

### Integer Linear Programming

Integer Linear Programming (ILP) is a type of optimization program where some or all variables are constrained to be integers. It is used to find optimal solutions for specific problems such as production planning, capital budgeting, crew scheduling, and Sudoku puzzles. ILP differs from Linear Programming (LP) in that it uses integer constraints rather than real number constraints.

ILP can be divided into three types:

1. **Pure Integer Linear Programming**: Expects all basic variables to be integer values (positive integers or zero).
2. **Mixed Integer Linear Programming**: Expects only some specific variables to be integer values.
3. **Zero-One Integer Linear Programming (1/0 IP)**: Expects variables to take values of either zero or one.

Several methods are commonly used to solve ILP problems, including:

- Gomory Cut Method / Cutting Plane Method
- Branch and Bound (B&B) Method
- Round Off Method

### Gomory Cut / Cutting Plane Method

The Gomory Cut / Cutting Plane Method is used to solve large-scale integer programming problems to obtain values close to optimal. It involves three steps:

1. **Solve the Integer Programming Problem**: Use the ordinary simplex method to solve the problem.
2. **Observe the Optimum Solution**: If all basic variables have integer values, the solution is optimal. If not, proceed to step 3.
3. **Create a Gomory Constraint**: Create a Gomory constraint and find the optimal solution through elementary row operations, then return to step 2.

The Gomory constraint is determined by separating the fractional parts of the variables and forming constraints to eliminate non-integer solutions. The process involves iterating until all solutions are integers or determining that no feasible integer solution exists.

This combined explanation integrates the BWM-MARCOS decision-making system with an overview of Integer Linear Programming and the Gomory Cut method, providing a comprehensive overview of both methodologies.

## Disclaimer

**Note:** The equations and formulas provided in this document are formatted using LaTeX. To view these equations correctly, ensure that you are running the server in an environment that supports LaTeX rendering for markdown.

### User Accounts

To access and test the application, use the following credentials:

**Account 1:**
- **Username:** admin
- **Password:** admin

**Account 2:**
- **Username:** test1
- **Password:** test1234567890

**Account 3:**
- **Username:** test3
- **Password:** test1234567890

Make sure to log in using the appropriate account to check the functionality of the application and view the formatted equations.
