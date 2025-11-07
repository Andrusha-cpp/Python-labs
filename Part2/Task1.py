import numpy as np

t_exp = np.array([1.2, 1.45, 1.22, 1.1, 1.15, 1.33, 1.16, 1.2, 1.33, 1.18, 1.23, 1.24])

summer_exp = np.sum(t_exp[5:8]) #expenses in summer
winter_exp = np.sum(np.append(t_exp[0:2], t_exp[11])) #expenses in winter

if summer_exp > winter_exp:
    print("Expenses are higher in summer than in winter.")
elif summer_exp < winter_exp:
    print("Expenses are higher in winter than in summer.")
else:
    print("Expenses are equal.")

print(f"Month with the biggest expenses is number {np.argmax(t_exp) + 1}.")