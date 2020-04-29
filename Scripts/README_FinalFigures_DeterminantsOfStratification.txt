READ ME: Final Figure Analysis.py (OCEAN 220)
Updated:4/18/2020
By: Dylan Vecchione

Data processing for figure production from publication in OCEAN 220:
"Determinants of stratification in Whidbey Basin and influence on water biogeochemistry"

===================================================================================================

PYTHON PACKAGES REQUIRED:
	1) Numpy
	2) Matplotlib and matplotlib.pyplot
	3) Gibbs Seawater (GSW)


NOTE: SECTION BREAKS ARE DENOTED BY COMMENTS OF SECTION NAMES IN THE PYTHON FILE


___________________________________________________________________________________________________
SECTION 1

Inputs: read from cnv text files from a subsampling of CTD stations (3, 5, 7, 9, 10), 
	and two Niskin Bottles (stations 3, 7, 10).
	Numpy.genfromtxt converts columns:
		1: Depth [salt water, m]
		3: Potential Temperature [ITS-90, deg C]
		6: Oxygen [umol/Kg]
		4: Salinity [PSU]
		5: Density [sigma-theta, Kg/m^3)
		8: Fluorescence (mg/m^3)
		0: Pressure [db]
	to data lists for further processing.
	NOTE: cnv files msut be in same directory as .py file, and
	names must be specified in the genfromtxt statement.

Outputs: Graphical figures showing relationship between various physical and 
	biogeochemical features with the Brunt Vaisala Frequency (Buoyancy Frequency, N^2)


___________________________________________________________________________________________________
SECTION 2

Empty lists are created an named to house all of the mid-point data from nearest-neighbor
mid-point interpolations for N^2 compariosn. 

	This is required because N^2 is a claculated value based on midpoints
	between datapoints. So the N^2 output is n-1 long. Because of the difference
	in data length, it cannot be plotted using matplotlib.pyplot, and so each 
	input data will be analyzed using nearest neighbor interpolations to calculate 
	the mid-point values along the profile, creating a new data-itermediary of n-1 
	length, compatible with the N^2 output for plotting.


___________________________________________________________________________________________________
SECTION 3

Here midpoints are calculated, and the above lists (SECTION 2) are populated. 


___________________________________________________________________________________________________
SECTION 4

Here N^2 values are calcualted and populate new lists named n[station number]


___________________________________________________________________________________________________
SECTION 5

Midpoint values are calculated for Niskin Bottle Data (Depth, pH, PAR, PO4, etc.) at Station 3.


___________________________________________________________________________________________________
SECTION 6

Midpoint values are calculated for Niskin Bottle Data (Depth, pH, PAR, PO4, etc.) at Station 7.


___________________________________________________________________________________________________
SECTION 7

Midpoint values are calculated for Niskin Bottle Data (Depth, pH, PAR, PO4, etc.) at Station 10.


___________________________________________________________________________________________________
SECTION 8

A matplotlib figure is created with 5 subplots showing profiles of various variables and N^2.
Subplot 1: Temperature
Subplot 2: Dissolved Oxygen
Subplot 3: Chlorophyll
Subplot 4: Salinity
Subplot 5: Buoyancy Frequency

Figure is saved as a png to parent directory with input name.


A second matplotlib figure is created with two subplots comparing variables/stations to N^2
Subplot 1: Station 3 and 10 N^2 vs. fluorescence
Subplot 2: Station 3 and 20 N^2 vs. dissolved oxygen

Figure is saved as png to parent directory with input name.


A third matplotlib figure is created with four subplots comparing niskin N^2 to biogeochemical factors.
Subplot 1: Station 3 and 10 N^2 vs. pH
Subplot 2: Station 3 and 10 N^2 vs. NO3
Subplot 3: Station 3 and 10 N^2 vs. SiOH
Subplot 4: Station 3 and 10 N^2 vs. NH4

Figure is saved as png to parent directory with input name.


_______________________________________________________________________________________________________
REST OF DOCUMENT

The rest of the python script repeates the above steps but only for the upper 50m of the Water Column
to resolve more interesting data behaviors that are not visible by viewing larger profiles.

This analysis only produces one figure with 6 subplots showing profiles of:
1: N^2
2: Temperature
3: Salinity
4: Fluorescence
5: Oxygen
6: Nitrate

Lines are drawn onto all subplots plot at two depths consistent with the highest startification features 
(changes in N^2), and visual correlations are present with some biogeochemical factors in other subplots.


Also saved as a png to parent directory with input filename.



==========================================================================================================

END