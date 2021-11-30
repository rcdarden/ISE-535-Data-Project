ISE 535 Fall 2021 Class Project - Casey Darden

Injection Molding Data Analysis

video link - https://youtu.be/fTrcnje9LQ4
gitHub link - https://github.com/rcdarden/ISE-535-Data-Project


• Explain the problem and/or Dataset
	There is (was) no method to analyze machine yield issues. Having a breakdown of exactly
	what machine errors are occuring over long runs aids in predictive maintenance to the machines, and shows which issues
	are having the greatest impact on machine performance.
	Secondly, the method in which our company reporting systems capture machine yield is sometimes erroneous, due to cavity
	count and/or cycle time information being innaccuratly recorded. Being able to quickly determine true machine yield from
	a production run based on actual machine data is very helpful when troubleshooting these types of issues. 
• What you want the program to do
	The program should parse a large .csv file exported directly from a KM injection molding machine and display a dashboard
	of all the key metrics from the production run, including yield issues, with minimal input from the user.
• Explain any unique features that you incorporated.
	The program searches for the correct file based on the part number and overwrites all files that are no longer needed
	An easy to read bar chart showing the occurances of machine errors is saved to the assets folder, then displayed in the
	dashboard, along with static displays of other key metrics (and our company logo)  


Requirements Met

1. Involves reading in CSV files

2. Involves Pandas and NumPy

3. Displays data visualization via matplotlib and Dash (html)

4. Learning component - went pretty deep into Pandas with my code - as expected I often had
	to try several methods until I found the one that worked. Also used some lines from base64.
   	Explored wepage / html development with Dash, CSS Styling, etc. Built dashboard from scratch 
	with no pre-existing css stylesheets. Got pretty good at debugging in Spyder. Also my data 
	visualization component analyzes large data sets (thousands of machine cycles) almost instantly.

Working journal of project progress is included in the comments section at the beginning of the code.

files:
	assets - contains objects for dashboard, defectChart is generated (overwriting) each time the code is ran.
	Dashboard Skeleton - design plan for my dashboard
	headerRow.csv - used in the construction of dataframe
	machineData118XXXX0001.csv - original .csv files exported directly from Krauss Maffei injection molding 
		machines (various models)
	machineDataFormatted.csv - used in the construction of dataframe
	parameterDB.csv - contains the acceptable range values of the various part numbers that we produce. This makes 
		the project scalable as more part numbers are added.
