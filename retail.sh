#!/bin/bash



# Source script to unset Jupyter configurations if any
source ./unset_jupyter.sh

# Check if the retail data CSV file exists on HDFS and delete if present
hdfs dfs -test -e /user/futurexskill/retailcust/retailstore_large.csv
if [ $? -eq 0 ]; then
    echo "File is There"
    hdfs dfs -rm /user/futurexskill/retailcust/retailstore_large.csv
    echo "File Deleted Successfully"
fi

echo "-------------------------------------------------------------------------------------"

# Put the retail data CSV file onto HDFS
echo "Putting file on HDFS"
hdfs dfs -put retailstore_large.csv /user/futurexskill/retailcust
echo "File copied successfully."

# Execute Hive script to create initial tables and process data
hive -f retailCustomer.hive

echo "---------------------------Executing PySpark Script----------------------------------"

# Execute the PySpark script for data processing and cleaning
spark-submit retail_PySpark.py

echo "---------------------------Hive Script-----------------------------------------------"

# Execute Hive script to create partitioned and bucketed table and insert data
hive -f retailCustomer_PartitionBucketed.hive

