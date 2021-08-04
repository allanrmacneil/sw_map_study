This is the semi-organised version of the code for computing mapping longitude offsets using HCS crossings at 1 au and PFSS models

The environment .yml file is the exact env I am running so that is a bit of a mess. Probably the key thing is to have the correct versions of pandas, xarray, scipy, numpy, pfsspy, and sunpy installed. Otherwise chances of running drastic go down.

Run HCS_mapping.ipynb to get the mapping offsets 

Then run mapping_paperplots to make most of the plots that went in the paper.

The code options should work in order to download all the data, but that is very large and goes slowly. There are intermediate data products with code to download from my google drive included in these scripts.

Allan Macneil 04/08/21