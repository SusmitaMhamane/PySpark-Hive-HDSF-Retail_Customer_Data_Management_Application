#!/usr/bin/python


# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Create a SparkSession
spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("WARN")

# Show existing tables in the 'futurex' database
print(spark.catalog.listTables())

# Get the current Spark SQL warehouse directory
print(spark.conf.get('spark.sql.warehouse.dir'))

# Print a message indicating DataFrame creation
print("Creating DataFrame--------------------------------------------------------")

# Create a DataFrame by querying the 'futurex.retailcustext_large' Hive table
df = spark.sql("select * from futurex.retailcustext_large")

# Print the schema of the DataFrame
print(df.printSchema())

# Select specific columns from the DataFrame
df = df.select("customerid", "age", "salary", "country", "gender")

# Print the schema of the modified DataFrame
print(df.printSchema())

# Show the first few rows of the DataFrame
df.show()

# Print a message indicating counting null records
print("Counting Null Records.------------------------------------------------------")

# Import necessary functions for handling null values
from pyspark.sql.functions import *

# Print a message indicating dropping null records and print the cleaned DataFrame
print("Dropping Null Records and Printing the DataFrame")
clean_df = df.na.drop()

# Show cleaned data
print("Cleaned DataFrame (after dropping null values):")
clean_df.show()

# Save cleaned DataFrame to Hive table 'futurex.clean_retail'
clean_df.write \
    .mode("overwrite") \
    .saveAsTable("futurex.clean_retail")

#below code is working in latest version of hive and not in the current version of spark(2.4.5) in sanbox.
#so work around is comment this line and uncomment the hive -f retailCustomer_PartitionBucketed.hive from retail.sh.
#clean_df.write.mode('overwrite').partitionBy("country", "gender").bucketBy(4, "salary").saveAsTable('futurex.clean_retail1')



