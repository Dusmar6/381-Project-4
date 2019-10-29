import math
import numpy as np
import matplotlib.pyplot as plt
    
mu=2.5    
sigma= 0.75
n=10000

def UnifPDF(mu, sigma, x):
    f=np.ones(len(x))
    for num in range(len(x)):
        f[num]=(1/(math.sqrt(2*math.pi*sigma**2)))   * math.e  **  (-((x[num]-mu)**2)/(2*sigma**2))
    return f 

x=np.random.normal(mu,sigma,n) 

#Create bins and histogram 
nbins=5# Number of bins 
edgecolor='w'  # Color separating bars in the bargraph
bins=[float(x) for x in np.linspace(0, nbins+1)] 
h1, bin_edges = np.histogram(x,bins,density=True) # Define points on the horizontal axis 
be1=bin_edges[0:np.size(bin_edges)-1] 
be2=bin_edges[1:np.size(bin_edges)] 
b1=(be1+be2)/2 
barwidth=b1[1]-b1[0] # Width of bars in the bargraph 
plt.close('all') 

# PLOT THE BAR GRAPH 
fig1=plt.figure(1) 
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor) 

#PLOT THE UNIFORM PDF 
f=UnifPDF(mu,sigma,b1) 
plt.plot(b1,f,'r') 

#CALCULATE THE MEAN AND STANDARD DEVIATION 
mu_x=np.mean(x) 
sig_x=np.std(x) 

print("Mu_x: = ", mu_x ) 

print("Sig_x: = ", sig_x ) 