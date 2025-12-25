# Basic bioinformatics learning script
# Author: Putri Amalia Zukhrufa

binding_energies = [-7.2, -6.8, -7.5, -6.9]

average_energy = sum(binding_energies) / len(binding_energies)

print("Average binding energy:", round(average_energy, 2), "kcal/mol")
