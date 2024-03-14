from utils.plot import plot, text
import matplotlib.pyplot as plt


# PbPb v23
ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
significance = [0, 0, 0, 3.090232, 3.719016, 3.598547, 3.540084]
yerr = [0, 0, 0, 0.296844, 0.252610, 0.091958, 0.059006]
asymptotic = 3.434812
fig, ax = plot(x=ntoys, y=significance, yerr=yerr, xlim=[10**0, 2*10**5], xlog=True, ylim=[0, 4.5], xlabel="Number of Toys", ylabel="Significance", label="PbPbv23", color="red")
plt.hlines(asymptotic, 10**0, 2*10**5, color="red")
text(0.075, 0.81, f"Asymptotics = {asymptotic:.2f}", fontsize=12, color="red")


# PbPb v28
ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
significance = [0, 0, 0, 0, 3.719016, 3.846126, 3.846126]
yerr = [0, 0, 0, 0, 0.252610, 0.141533, 0.100079]
asymptotic = 3.740695
plt.errorbar(ntoys, significance, xerr=None, yerr=yerr, fmt='-o', color="black", label="PbPbv28")
plt.hlines(3.740695, 10**0, 2*10**5, color="black")
text(0.075, 0.88, f"Asymptotics = {asymptotic:.2f}", fontsize=12, color="black")

plt.legend(loc="lower left", fontsize=18)
plt.savefig("ttPbPbToys.pdf", bbox_inches="tight")
