# Evolution of property prices, employment and Homelesness in Ireland 

## Overview

This repository contains an analysis of the evolution of the price property in Ireland, the unemployment rate and the homelessness rate.
All the data is pulled from two official websites. Central statistical office (price property index and unemployment rate) and data.gov.ie (homelessness dataset).
The first part of the project gets information and provide graphs for each single dataset. The second part of the project combine different datasets to analyse how the different variables influence each other.

## Getting started

In order to work with this repository, the author recommends the installations of below packages/programs.

*	Install the latest version of Python and Pandas, Matplotlib and NumPy modules. All of it include in  [Anaconda ]( https://www.anaconda.com/download/). 
*   To start using the notebooks, I recommend to install [Visual studio](https://visualstudio.microsoft.com/downloads/). 

## Source tables details

1) **Price property index** was downloaded from [Data_CSO]
(https://data.cso.ie/). The property price index contains the evolution of the property prices compared with the base value which was stablish in 2015. One thing to highlight is that data from Dublin is available from 2005 and it includes all the type of property. For the rest of the regions only information about houses is available and only from 2010. To have the correct format of the table two different actions were applied. Firstly, column Month was formatted to datetime, then rows with NAN was removed. ( Reference 1,2,3)

2) ** Unemployment rate** was downloaded from [Data_CSO]
(https://data.cso.ie/).

## Analysis

## references

**Reference 1**: https://data.cso.ie/
**Reference 2**: https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/
**Reference 3**: https://www.w3schools.com/python/python_datetime.asp
**Reference 4**: https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan



