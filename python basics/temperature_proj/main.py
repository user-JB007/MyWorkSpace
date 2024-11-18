import pyspark.sql
from pyspark.sql.connect.session import SparkSession

spark = SparkSession.builder \
    .appName("Temp_cnvrtr") \
    .master("local[4]") \
    .getOrCreate()

file_path="Data/MOCK_DATA.csv"
#reading the file temp
temp_df = spark.read\
    .csv(file_path) \
    .option("header", "true") \
    .option("inferSchema","true")

temp_df.show()