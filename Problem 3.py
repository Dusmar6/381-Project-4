import numpy as np
import matplotlib.pyplot as plt


beta =50 #days
n=30 #batteries
Y1=3 #yrs
Y2=2 #yrs
Y3=4 #yrs;
N=10000


# Generate the values of the RV X 
X=np.zeros((N,1)) 

for k in range(0,N):     
    x=np.random.exponential(beta,n)         
    X[k]= np.sum(x) /365
    
# Create bins and histogram 
nbins=30        # Number of bins 
edgecolor='w'       # Color separating bars in the bargraph # 



bins=[float(y) for y in np.linspace(1,7,nbins+1)] 
h1, bin_edges = np.histogram(X,bins,density=True) 


# Define points on the horizontal axis  
be1=bin_edges[0:np.size(bin_edges)-1] 
be2=bin_edges[1:np.size(bin_edges)] 
b1=(be1+be2)/2 
barwidth=b1[1]-b1[0] # Width of bars in the bargraph 

# PLOT THE BAR GRAPH 

plt.close('all') 
fig1=plt.figure(1) 
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor) 
plt.title('Sum of Exponential RVs Distribution')
plt.xlabel('Battery Cart Life (yrs)',fontsize=14)
plt.ylabel('PDF',fontsize=14,)


mu_x=np.mean(X) 
sig_x=np.std(X) 

#PLOT THE GAUSSIAN FUNCTION 
def gaussian(mu,sig,z):   
    f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))   
    return f 

f = gaussian(mu_x, sig_x, b1)
plt.plot(b1, f, 'r')
plt.show()

print("Mu_x: = ", mu_x)

print("Sig_x: = ", sig_x)

CDF = np.cumsum(h1 * barwidth)
plt.bar(b1, CDF, width = barwidth, edgecolor = edgecolor)
plt.title('CDF of Carton Life')
plt.xlabel('Lifetime of one carton',fontsize=14)
plt.ylabel('Prob. Density',fontsize=14,)
#plt.grid(True, color='#dfdfdf', dashes=(1,2))
#plt.yticks(np.arange(0,1.1,step=.1))


plt.plot (b1, CDF, 'r')
plt.show()
