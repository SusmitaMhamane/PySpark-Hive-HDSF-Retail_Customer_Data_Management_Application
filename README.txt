Retail Customer Data Management Application

This application is designed to manage retail customer data using Apache Hive and Apache Spark. Below are the components and steps involved in the application:

------------------------------------------------------------------------------------------------------------------------------------------------

Problem Statement:

The primary goal of this application is to process and store retail customer data into Hive tables with specific requirements:
------------------------------------------------------------------------------------------------------------------------------------------------

Initial Data Ingestion and Preparation:

The retail customer data is initially stored as CSV files on HDFS (/user/futurexskill/retailcust/).
These files contain customer information such as customerid, age, salary, gender, and country.
Data Processing with Apache Spark:

retail_PySpark.py script is used to read the CSV data into a DataFrame using Spark SQL.
The data is cleaned by dropping any rows with null values.
A cleaned DataFrame (clean_df) is created, which includes selected columns (customerid, age, salary, country, gender).

Storing Data in Hive:

Initially, the cleaned data (clean_df) is stored in a non-partitioned Hive table named clean_retail.

------------------------------------------------------------------------------------------------------------------------------------------------

Partitioning and Bucketing Requirements:

The requirement to partition the data by country and gender, and bucket it by salary into 4 buckets, poses a challenge due to limitations in the Spark version (2.4.5).

------------------------------------------------------------------------------------------------------------------------------------------------

Solution Approach:

To overcome the limitations, a Hive script retailCustomer_PartitionBucketed.hive is used:
Sets necessary Hive properties.
Defines an external table (clean_retail_data) with partitions (country, gender) and buckets (salary).
Inserts data into this partitioned and bucketed table from the initial non-partitioned table (clean_retail).
Execution Flow:
------------------------------------------------------------------------------------------------------------------------------------------------

Execution Flow:
retail.sh script orchestrates the execution:

Checks for existing data files on HDFS and manages file operations.

Executes Hive scripts (retailCustomer.hive and retailCustomer_PartitionBucketed.hive) and PySpark script (retail_PySpark.py) sequentially.

------------------------------------------------------------------------------------------------------------------------------------------------

Unset Jupyter Configurations:

The unset_jupyter.sh script is sourced to unset specific environment variables (PYSPARK_DRIVER_PYTHON and PYSPARK_DRIVER_PYTHON_OPTS) related to the PySpark driver's Python configuration. This ensures a clean environment for Spark execution.

------------------------------------------------------------------------------------------------------------------------------------------------

Conclusion:

This approach allows efficient data management using Hive's partitioning and bucketing features, leveraging the strengths of Spark for data processing and Hive for structured storage. This hybrid approach ensures scalability and performance, meeting the requirements for organized storage and retrieval of retail customer data.