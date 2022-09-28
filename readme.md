#  General
A software that helps to extract insights from raw csv data. <br>
The input is expected to be a csv file as follows:<br>
 Capacity- positive number.<br>
 Monthly Price - positive number.<br>
 Start Day - YYYY-MM-DD format.<br>
 End Day -  YYYY-MM-DD format.<br>
The program is able to answer the following questions:<br>
given a month (YYYY-MM), what would be:<br>
count of reserved offices for the month<br>
capacity  offices not reserved for the month<br>
profit for the month<br>
average profit per office in the month.<br>

#  structure
The project is divided into 2 major classes:
Researcher and CSVDataSource.<br>
The CSVDataSource parses the raw csv file, and creates a data object.<br>
The data object must comply to the abstraction that the Researcher expects:<br>
A list of dicts, each with the keys:<br>
"Capacity" - int,<br>
"Monthly Price" int,<br>
"Start Day" - date object,<br>
"End Day"- date object.<br>
Thus, an abstraction is created, and the data can come from any other source<br>
as long as it complies to that format.<br>

The Researcher class is capable of performing the needed quieres.<br>
To do so, a helper class is involved- the Research utils.<br>
The methods of this class are doing only one-line quirees.<br>
The Researcher uses these methods to create the needed aggregate results.<br>

#  files

CsvDataSource - creates a data object from a csv file
 
Researcher - given a data object from the data source, it is able to explore and answer questions
 
ResearchUtils -  helper funcs for the researcher
 
test - runs the test cases
 
cli_server - runs a CLI server that prompts for csv file and year-month input,
               and prints the result of running the queries.
               
 Go - directory, another version of the same software, in Golang. Not finished yet.
               
