import numpy as np
import matplotlib.pyplot as plt

# Exemplo do cálculo da tangente de perdas
e0 = 8.85e-12  # Permissividade no espaço livre
sigCu = 5.8e7  # Condutividade do cobre
erCu1 = 1      # er' do cobre
erCu2 = 0      # er" do cobre
sigAM = 5
erAM1 = 81
erAM2 = 12     # sig, er', er" água do mar
sigVi = 10e-12
erVi1 = 10
erVi2 = 0.01   # sig, er', er" Vidro

# Definindo a faixa de frequências
n = np.arange(2, 13, 1)
f = 10.0**n
w = 2 * np.pi * f  # Frequência angular

# Cálculos para o cobre
e1Cu = e0 * erCu1
e2Cu = e0 * erCu2
tanCu = (sigCu + w * e2Cu) / (w * e1Cu)

# Cálculos para o vidro
e1Vi = e0 * erVi1
e2Vi = e0 * erVi2
tanVi = (sigVi + w * e2Vi) / (w * e1Vi)

# Cálculos para a água do mar
e1AM = e0 * erAM1
e2AM = e0 * erAM2
tanAM = (sigAM + w * e2AM) / (w * e1AM)

# Plotagem em escala logarítmica
plt.loglog(f, tanCu, '+', label='Cobre')
plt.loglog(f, tanAM, '*', label='Água do mar')
plt.loglog(f, tanVi, 'o', label='Vidro')

# Legendas e rótulos
plt.legend()
plt.xlabel('Frequência (Hz)')
plt.ylabel('Tangente de Perdas')
plt.grid(True, which="both", ls="--")
plt.show()