#spacenoise

This is a set of simple python scripts that test a method for generating spatially correlated noise. 

This will generate an (n * m) pixels intensity image (i.e. between 0 and 1) with an underlying noise structure.

## Usage

Run the scripts in your console using

    > python spacenoise.py
    
    > python spacenoise_reduced.py

## How it Works

### Algorithm

For the original implementation, 

  - Generate an image with a specific initial condition (e.g. random or uniform(0.5) )
  - Define an underlying coupling structure using pixel position information, to return a "similarity measure"
  - Normalize the similarity measure to get coupling weights
  - Iteratively sample a random pixel from the image
    - Use the coupling weights to sample another pixel to which it couples strongly
    - Sample the new pixel intensity from some distribution based on sampled pixel intensities, similarity and other params.
  
Note that this is very slow, since coupling is calculated for all pixels to all pixels, and we sample accordingly.
To make this faster, another version was written (spacenoise_reduced) that only samples from the strongest coupling pixels.

### Sample Functions

We require a definition of:

  - Initial Condition
  - Similarity Measure
  - Sampling Distribution
  
for the algorithm to work. A few examples have been implemented!

#### Initial Condition

  - Uniformly Random
  - Uniform 0.5
      
#### Similarity Measure

    - Exponentiated euclidean pixel distance squared
    - Exponentiated euclidean pixel distance non-squared
    - Sine squared of euclidean pixel distance

#### Sampling Distribution

    - Gaussian centered around neighbor with fixed variance
    - Gaussian centered around average of neighbor and sampled pixel with fixed variance
    - Gaussian centered around neighbor with variance determined by coupling strength

## Results

Coming in a second.
