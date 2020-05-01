# FinalExam

## Overview
This repository hosts the two projects related to the CIS 4517 Final Exam, a MapReduce program to count Bigrams on an AWS EC2 instance, and an investigation into the [COVID-19 data I scraped](https://github.com/bri-davis/Scrapers-for-Government-COVID-19-Measures) using Pandas. Implementation and design details are located in the FinalExamReport.pdf

## Requirements
The MapReduce BigramCount program requires access to an AWS EC2 instance (large node), Java 8, and Hadoop 2.7.3. The BigramCount deliverables Python script additionally requires Python 3. 

The Pandas program requires Python 3 and Pandas.

## How to Run
### Running MapReduce
Run the MapReduce BigramCount program by setting up Hadoop on an AWS EC2 Ubuntu instance in the same manner that I thoroughly documented in the FinalExamReport.pdf. The hadoop_config files were provided own the BigramCount directory; these are the only Hadoop XML and bash files that I edited in the /hadoop-2.7.3/etc/hadoop directory. Update the contents of the ~/.bashrc with that which is stored in the bashrc.txt file. After all of this setup is taken care of, run the following commands:

Compile the java file into binary that can be executed by the JVM:

```javac -d BigramCountClasses/ BigramCount.java```

Compile the java classes into a jar to execute on the HDFS:

```jar -cvf BigramCount.jar -C BigramCountClasses/ .```

Execute the jar on the HDFS:

```hadoop jar BigramCount.jar BigramCount /input /output```

Obtain the output from HDFS:

```hdfs dfs -get /output```


The code is set to run with 5 reducers, therefore there will be 5 outputs in the retrieved /output folder.

### MapReduce Deliverables
In order to obtain the deliverables, simply run the following in the /BigramCount directory:

```python3 BigramDeliverables.py```

And observe the terminal stdout for the deliverables.

### Pandas Deliverables
In order to obtain the deliverables, simply run the following in the /PandasDataAnalysis directory:

```python3 explore_data_using_pandas.py```

And observe the terminal stdout for the deliverables.