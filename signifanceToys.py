from utils.plot import plot, text
import matplotlib.pyplot as plt

ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
significance = [0, 0, 0, 3.090232, 3.719016, 3.598547, 3.540084]
yerr = [0, 0, 0, 0.296844, 0.252610, 0.091958, 0.059006]
fig, ax = plot(x=ntoys, y=significance, yerr=yerr, xlim=[10**0, 2*10**5], xlog=True, ylim=[0, 4.5], xlabel="Number of Toys", ylabel="Significance")
plt.hlines(3.434812, 10**0, 2*10**5, color="blue")
text(0.075, 0.85, f"Asymptotics = {3.434812:.2f}", fontsize=20, color="blue")
plt.savefig("ttPbPbToys.pdf", bbox_inches="tight")
