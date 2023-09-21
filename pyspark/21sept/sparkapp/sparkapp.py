

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()

df = spark.read.csv('input_data.csv', header = True, inferSchema = True)

# place to perform operations
df = df.filter((df['variety']=="Versicolor") | (df["variety"] == "Setosa"))

df.write.csv('output_data.csv', header = True)

spark.stop()



