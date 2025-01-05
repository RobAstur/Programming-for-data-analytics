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
(https://data.cso.ie/). The property price index contains the evolution of the property prices compared with the base value which was stablish in 2015. One thing to highlight is that data from Dublin is available from 2005 and it includes all the type of property. For the rest of the regions only information about houses is available and only from 2010. To have the correct format of the table two different actions were applied. Firstly, column Month was formatted to datetime, then rows with NAN was removed. ( Reference 1,3,4)

2) **Unemployment rate** was downloaded from [Data_CSO]
(https://data.cso.ie/). Data is available from 1998. It contains information about unemployment rate by age groups and sex.(Reference 1)

3) **Homelessness in Ireland** was downloaded from [Data_Gov] (https://data.gov.ie/).
It contains the number of homeless people in the country by region, sex, group age and type of accommodation provided. To create the table all the data was opened directly from the website month by month. Information cover from 2019 to October 2024. All the tables were combined to create a single table. In 2022 there was a change in the table, thus, few columns needed to be removed to create the final table. A new column was added to the tables to ensure dates were tracker and review the evolution. Finally, all the number were converted to integers. There were issues with numbers with comma (References 6,7,8).

## Analysis

## References

- **Reference 1**: [CSO Data](https://data.cso.ie/)
- **Reference 2**: [Data.gov](https://data.gov.ie/)
- **Reference 3**: [GeeksforGeeks - Convert String to Datetime in Pandas](https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/)
- **Reference 4**: [W3Schools - Python Datetime](https://www.w3schools.com/python/python_datetime.asp)
- **Reference 5**: [StackOverflow - Drop Rows with NaN Values in a Specific Column](https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan)
- **Reference 6**: [Pandas - concat Function](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
- **Reference 7**: [Pandas - DataFrame drop Function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
- **Reference 8**: [Spark by Examples - Convert String to Integer in Pandas](https://sparkbyexamples.com/pandas/pandas-convert-string-to-integer/)

