# Least-Squares-Jeffery-s-Method
This code uses Jeffery's Method to perform least square on a data set which contains uncertainties in both dependent (Y) and independent (X) variables. 
Furthermore, this method also takes into account of the covariance that the independent-dependent variables have amongnst each other. The way Jeffery does 
this is that he combines both dependent and independent variable into one single variable called X (input variables) and computes the Chi-square. The cost 
function to be minimised has two terms: first is the chi-square term and the second term is the exact eqution (similar to OLS). 

A very good explanation can be found in section 14.6 of these Berkley lecture notes (http://ugastro.berkeley.edu/radio/2015/handout_links/lsfit_2008.pdf). 
I have used the same notations in the code as those used in Berkley lecture notes section 14.6. I am following the iterations mentioned in section 14.9
to derive the coefficients by updating the coefficients and the input variables at each step.

The original paper can be found here: http://adsabs.harvard.edu/full/1980AJ.....85..177J. I will be using this method to derive Star Formation Histories of
nearby Galaxies (z<0.15) by comparing their Spectral Energy Distribution (SED) with the Spectra from Models. Please keep an eye out for the upcoming repository!
