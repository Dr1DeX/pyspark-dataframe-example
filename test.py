from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import col, count

import findspark

findspark.init()
findspark.find()


def get_product_category_pairs(df):
    product_categories_pairs = df.select('product_name', 'category_name')

    product_without_category = df.groupBy('product_name').agg(count('category_name')) \
        .filter(col('count(category_name)') == 0) \
        .select('product_name')

    return product_categories_pairs, product_without_category


spark = SparkSession.builder.appName('ProdCat').getOrCreate()

data = [
    Row(product_name='Product 1', category_name='Category 1'),
    Row(product_name='Product 1', category_name='Category 2'),
    Row(product_name='Product 3', category_name='Category 2'),
    Row(product_name='Product 4', category_name=None),
]

df = spark.createDataFrame(data)

prod_cat_pairs, prod_without_cat = get_product_category_pairs(df)

print('Пара Продукт-Категория: ')
prod_cat_pairs.show()

print('Продукты без категории: ')
prod_without_cat.show()

spark.stop()
