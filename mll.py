from utils.plot import plot, text
from utils.histograms import extended_hist
import matplotlib.pyplot as plt
import uproot
import numpy as np 

import mplhep as hep
hep.style.use("ATLAS")

# load data
inFileName = "/Users/anthonybadea/Downloads/PbPbv30/hists.root"
f = uproot.open(inFileName)
samples = {
	"data" : ["data", "black"],
	"ttbar" : ["$t\\bar{t}$", "red"],
	"Wt" : ["tW", "orange"],
	"WW" : ["WW", "green"],
	"Zee" : ["Z$\\rightarrow ee$", "blue"],
	"Zmumu": ["Z$\\rightarrow \\mu \\mu$", "blue"],
	"Ztautau": ["Z$\\rightarrow \\tau \\tau$", "blue"],
	"fake" : ["fake", "purple"]
}



# create plot
fig, ax = plot(xlim=[0, 300], ylim=[0, 0.1], xlabel="Dilepton invariant mass m$_{ll}$", ylabel="Fraction of Events")

# histogram
trees = [i for i in f.keys() if "nominal" in i and "emu" in i]
bins = np.linspace(0,300,31)
for t in trees:
	# load
	label, color = samples[t.split("-nominal")[0].split("emu-")[1]]
	mll = np.array(f[t]['mll'].array()).flatten()
	w = np.array(f[t]['weight'].array()).flatten()
	# histogram and normalize

	# need to normalize. there should be a histogram script somewhere to do this properly with weights
	plt.hist(mll, weights=w, bins=bins, histtype="step", label=label, lw=1.3, color=color, density=True) 
	


# text
hep.atlas.text("Internal")
text(0.04, 0.88, text="1.9 nb$^{-1}$", fontsize=15, color="black")
text(0.04, 0.82, text="$e\\mu$ SR", fontsize=15, color="black")
text(0.04, 0.76, text="$p_{T}^{ll} > 40$ GeV, $\\geq 2$ jets", fontsize=15, color="black")

# save
plt.legend(title="", loc="upper right", fontsize=13, title_fontsize=12)
plt.savefig("mll.pdf", bbox_inches="tight")