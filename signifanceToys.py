from utils.plot import plot, text
import matplotlib.pyplot as plt


# PbPbv23
ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
significance = [0, 0, 0, 3.090232, 3.719016, 3.598547, 3.540084]
yerr = [0, 0, 0, 0.296844, 0.252610, 0.091958, 0.059006]
asymptotic = 3.434812
fig, ax = plot(x=ntoys, y=significance, yerr=yerr, xlim=[10**0, 2*10**5], xlog=True, ylim=[0, 4.5], xlabel="Number of Toys", ylabel="Significance", label=f"v23 ({asymptotic:.2f})", color="red")
plt.hlines(asymptotic, 10**0, 2*10**5, color="red", ls="--", alpha=0.5)
#text(0.075, 0.81, f"Asymptotics = {asymptotic:.2f}", fontsize=12, color="red")

# PbPbv25
ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
# expected with data
significance = [0, 0, 0, 0, 3.290527, 3.258507, 3.301994]
yerr = [0, 0, 0, 0, 0.125789, 0.053607, 0.040476]
asymptotic = 3.269032
# asimov
significance = [0, 0, 0, 0, 3.290527, 3.258507, 3.301994]
yerr = [0, 0, 0, 0, 0.125789, 0.053607, 0.040476]
asymptotic = 3.269032
# plot
color = "purple"
plt.errorbar(ntoys, significance, xerr=None, yerr=yerr, fmt='-o', color=color, label=f"v25 ({asymptotic:.2f})")
plt.hlines(asymptotic, 10**0, 2*10**5, color=color, ls="--", alpha=0.5)
#text(0.075, 0.88, f"Asymptotics = {asymptotic:.2f}", fontsize=12, color=color)

# PbPbv27
ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
# expected with data
significance = [0, 0, 0, 0, 3.540084, 3.598547, 3.633134]
yerr = [0, 0, 0, 0, 0.186592, 0.091958, 0.068928]
asymptotic = 3.629660
# asimov
significance = [0, 0, 0, 0, 3.540084, 3.598547, 3.633134]
yerr = [0, 0, 0, 0, 0.186592, 0.091958, 0.068928]
asymptotic = 3.629660
# plots
color = "green"
plt.errorbar(ntoys, significance, xerr=None, yerr=yerr, fmt='-o', color=color, label=f"v27 ({asymptotic:.2f})")
plt.hlines(asymptotic, 10**0, 2*10**5, color=color, ls="--", alpha=0.5)
#text(0.075, 0.88, f"Asymptotics = {asymptotic:.2f}", fontsize=12, color=color)

# PbPbv28
ntoys = [10**0, 10**1, 10**2, 10**3, 10**4, 5*10**4, 10**5]
significance = [0, 0, 0, 0, 3.719016, 3.846126, 3.846126]
yerr = [0, 0, 0, 0, 0.252610, 0.141533, 0.100079]
asymptotic = 3.740695
color = "black"
plt.errorbar(ntoys, significance, xerr=None, yerr=yerr, fmt='-o', color=color, label=f"v28 ({asymptotic:.2f})")
plt.hlines(asymptotic, 10**0, 2*10**5, color=color, ls="--", alpha=0.5)
#text(0.075, 0.88, f"Asymptotics = {asymptotic:.2f}", fontsize=12, color=color)

plt.legend(title="Sample (Asymptotic)", loc="lower left", fontsize=14, title_fontsize=14)
text(0.04, 0.96, text="Expected significance using data", fontsize=15, color="black")
text(0.04, 0.91, text="Significance roughly when using asimov dataset", fontsize=12, color="black")
plt.savefig("ttPbPbToys.pdf", bbox_inches="tight")
