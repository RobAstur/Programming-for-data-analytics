# Evolution of property prices, employment and Homelesness in Ireland 

## Overview

This repository contains an analysis of the evolution of the price property in Ireland, the unemployment and the homelessness rate.
All the data is pulled from two official websites. Central statistical office (price property index and unemployment rate) and data.gov.ie (homelessness dataset).
The first part of the project gets information and provide graphs for each single dataset. The second part of the project combine different datasets to analyse how the different variables influence each other. It also provided basic statistics.

## Getting started

In order to work with this repository, the author recommends the installations of below packages/programs.

*	Install the latest version of Python and Pandas, Matplotlib and NumPy modules. All of it include in  [Anaconda ]( https://www.anaconda.com/download/). 
*   To start using the notebooks, I recommend to install [Visual studio](https://visualstudio.microsoft.com/downloads/). 

## Source of tables and summary.

**Price property index** was downloaded from [CSO](“ https://data.cso.ie/”). Name of the table is Residential _Property Price Index HPM09_. Filters applied:
•	Statistic: Residential property price index (base 2005=100)
•	Month: Select all.
•	Type of residential property: Dublin – all residential properties, Midland houses, West houses, Mid-East, Mid-west, South East and South West 

The **property price index** contains the evolution of the property prices compared with the base value which was stablish in 2015. One thing to highlight is that data from Dublin is available from 2005 and it includes all the type of property. For the rest of the regions, there are only information about houses and it only is available and only from 2010. To have the correct format of the table two different actions were applied. Firstly, column Month was formatted to datetime, then rows with NAN was removed. ( Reference 1,3,4)

**Unemployment rate in Ireland** was download from [CSO](“ https://data.cso.ie/”). Name of the table is _MUM01 - Seasonally Adjusted Monthly Unemployment_. Filters applied.
•	Statistics: seasonal adjusted Monthly unemployment rate %
•	Month: Select all.
•	Age group: Select all.
•	Sex: Male and Female. Initially I selected all but It was changed to Male and Female.

**Homelessness rate**: Table were built from multiple tables. It was opened directly from the cloud. All the links  can be found in the project. Details about how to combine the tables can be found in the project.

Data is available from 1998. It contains information about unemployment rate by age groups and sex.(Reference 1)
It contains the number of homelessness people in the country by region, sex, group age and type of accommodation provided. To create the table all the data was opened directly from the website month by month. Information cover from 2019 to October 2024. All the tables were combined to create a single table. In 2022 there was a change in the table, thus, few columns needed to be removed to create the final table. A new column was added to the tables to ensure dates were tracker and review the evolution. Finally, all the number were converted to integers. There were issues with numbers with comma (References 6,7,8).


## Analysis: Statistics and Plots

### Plots from individual tables.

The plots pulling from single tables are covered in this section. Each of the plots are coming from one of the different tables. 

1)  _Evolution of Residential Property Price Index by Year_: The plot shows the evolution of the price property index across all the regions in Ireland. The base year was set up in 2015. Since then, we can see a constant growth across all the regions in Ireland. More information that we can extract from the plot is that Dublin has overcome the prices of the Celtic tiger era. In the rest of the region the price property index is growing at much faster pace than in Dublin. The regression line has a positive trend, and we can predict that the value of property price index will continue to growth in the next years.

2)  _Evolution of yearly unemployment rate in Ireland_: This section starts with a table with statistics where we can see the mean, standard deviation, min, max or median by age of group and sex and it helps to understand the plot. Unemployment is more prevalent in the age group of 15-14. Across all the series we can see that the value is considerable higher than the rest of the age groups. The levels of unemployment have a positive evolution and nowadays both are at the same level. Since the financial crash the levels of employment have reduced across all the age groups. 

3)  _Evolution of Homelessness in Dublin by Gender_: For this section 3 different plots were create. Line and bar plots to see the evolution of homelessness in Dublin in the last years. The combination of both plots gives a clear picture of the issue. We can clearly see that homelessness in Dublin have constantly growth across genders. Finally there is other bar plot to see the evolution across all the regions. Although homelessness is not growing at the same pace as in Dublin. The trend is showing an increase across all the regions.

### Plots from table combination

This section start the merge of the tables and creation of the plots. Then calculation of correlation by differente parameters.

1)  _Evolution of property index and unemployment rate over the years_: This plot is a combination of tables property index and unemployment rate and focus on Dublin. We can clearly see that when unemployment goes down, price property index increase. However, there is a point where unemployment has stabilize at low levels , but property price index is still raising. The calculation of the correlation shows a negative correlation of -0.49 which suggest that there is a moderate negative correlation between them. **Reference 14**

2) _Evolution of property index and homelessness in Ireland over the years_: The last table show the evolution of the price property index and the homelessness in Dublin. For rest of the region can be seen replacing the filters. Visually we can see that both patrons evolve similarly. If we calculate the correlation between homelessness in Dublin and price index the results show a strong positive relation between the two variables with a positive value of 0.73. 



## References

- **Reference 1**: [CSO Data](https://data.cso.ie/)
- **Reference 2**: [Data.gov](https://data.gov.ie/)
- **Reference 3**: [GeeksforGeeks - Convert String to Datetime in Pandas](https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/)
- **Reference 4**: [W3Schools - Python Datetime](https://www.w3schools.com/python/python_datetime.asp)
- **Reference 5**: [StackOverflow - Drop Rows with NaN Values in a Specific Column](https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan)
- **Reference 6**: [Pandas - concat Function](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
- **Reference 7**: [Pandas - DataFrame drop Function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
- **Reference 8**: [Spark by Examples - Convert String to Integer in Pandas](https://sparkbyexamples.com/pandas/pandas-convert-string-to-integer/)
- **Reference 9**: [Datacamp-Seaborn](https://www.datacamp.com/tutorial/python-seaborn-line-plot-tutorial)
- **Reference 10**: [Pandas-Melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)
- **Reference 11**: [Datacamp-Errors](https://www.datacamp.com/tutorial/settingwithcopywarning-pandas)
- **Reference 12**: [Pandas_statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
- **Reference 13** [Pandas_Correlation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html)
- **Reference 14** [Correlation_ranges](https://link.springer.com/article/10.1057/jt.2009.5)

-----
END