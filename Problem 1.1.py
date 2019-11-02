import numpy as np
import matplotlib.pyplot as plt



def UnifPDF(a,b,x):     
    f=(1/abs(b-a))*np.ones(np.size(x))     
    return f 


a=2.0  
b=5.0 
n=10000

x= np.random.uniform(a,b,n) 

#Create bins and histogram 
nbins=30 # Number of bins 
edgecolor='w'  # Color separating bars in the bargraph
bins=[float(x) for x in np.linspace(a, b,nbins+1)] 
h1, bin_edges = np.histogram(x,bins,density=True) # Define points on the horizontal axis 
be1=bin_edges[0:np.size(bin_edges)-1] 
be2=bin_edges[1:np.size(bin_edges)] 
b1=(be1+be2)/2 
barwidth=b1[1]-b1[0] # Width of bars in the bargraph 
plt.close('all')

# PLOT THE BAR GRAPH 
plt.title('Uniform Random Variable - PDF')
plt.xlabel('Uniform distribution between 2 and 5',fontsize=14)
plt.ylabel('Probability',fontsize=14,)

fig1=plt.figure(1) 
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor) 

#PLOT THE UNIFORM PDF 
f=UnifPDF(a,b,b1) 
plt.plot(b1,f,'r') 

#CALCULATE THE MEAN AND STANDARD DEVIATION 
mu_x=np.mean(x) 
sig_x=np.std(x) 


print("Mu_x: = ", mu_x)

print("Sig_x: = ", sig_x)