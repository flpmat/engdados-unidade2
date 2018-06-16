from pyspark.sql import SparkSession

if __name__ == "__main__":


    df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", "mongodb://192.168.0.4/movielens.movies").load()

    df.printSchema()

    