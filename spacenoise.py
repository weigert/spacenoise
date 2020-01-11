#Spatially Correlated Noise Test

'''
This script will generated spatially correlated noise using an arbitrary similarity measure,
for an (n * m) image.

Procedure:
- Initialize the Image (arbitrary initializer)
- Compute neighbor similarity weights based on similarity measure
- Iterate over the image, sample a point and its neighbor using the weights
    - Sample the new intensity at the sampled point using a gaussian around its neighbor's intensity
- Rescale and display the image.

There are a number of parameters to play with:
    (n, m)  = Image Size
    iter    = Number of iterations to converge image
    a       = Similarity Measure Scale
    stddev  = Variance towards neighbors for sampling

Additionally, you can define the following functions freely:
 - initialize: Determines the image initial condition
 - similarity: Gives some similarity measure (non-normalized)

This would be MUCH faster if computed in something other than python.
'''

#Dependencies
import matplotlib.pyplot as plt
import numpy as np

'''
    PARAMETERS
'''
n = 30;
m = 30;
iter = 100000;
a = 0.01;
stddev = 0.05;

'''
    GOVERNING FUNCTIONS
'''

#Get Initiial Condition
def initialize( n, m ):
    #return np.random.rand(n * m);
    return np.zeros( n * m );

#Similarity Measure
def similarity( A, B, s ):
    # Euclidean Distance Squared, Exponentiated (recommended a = 0.01)
    #return np.exp(-a*(np.linalg.norm(np.asarray(np.unravel_index(B, s)) - np.asarray(np.unravel_index(A, s))))**2);

    # Euclidean Distance Non-Squared, Exponentiated (recommended a = 0.1)
    #return np.exp(-a*(np.linalg.norm(np.asarray(np.unravel_index(B, s)) - np.asarray(np.unravel_index(A, s))))**2);

    # Squared sine of euclidean distance! a scales the frequency. (recommended a = 0.1)
    return np.sin(a * np.linalg.norm(np.asarray(np.unravel_index(B, s)) - np.asarray(np.unravel_index(A, s))))**2+0.01;

#Intensity sampling function
def distribution( I, J, sim, stddev ):
    #Sample new intensity by a gaussian centered around neighbor
    #return np.random.normal( J , sim );

    #Sample new intensity by a gaussian centered around average intensity
    #return np.random.normal( (I + J)/2 , sim );

    #Sample from a gaussian centered around neighbor, with variance determined by similarity
    return np.random.normal( J , (1-sim)*0.1 );
    
'''
    COMPUTE
'''

#Initialize an Image
print('Testing Spatial Noise Correlation')

I = initialize( n, m );

#NOTE: Weight matrix is computed here because of no dependency on intensity values.
# This weight matrix becomes absolutely massive for large images.

W = np.zeros((n * m,  n * m ));
#Compute all Weights
for i in range(n * m):
    for j in range(n * m):
        #Similarity Measure
        W[i, j] = similarity(i, j, (n, m));
        W[i] /= np.sum(W[i]);

print("Computed Weight Matrix.");

for i in range(iter):
    #Sample update position and neighbor!
    x = np.random.randint(0 , n * m);
    y = np.random.choice( n * m , p = W[x] );

    #Update value by sampling gaussian
    I[x] = distribution( I[x], I[y], W[x,y], stddev );

#Rescale and show the result
I = (I - I.min())/(I.max() - I.min())
plt.imshow(I.reshape((n, m)))
plt.show()
