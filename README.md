# pyspark-dataframe-example 

## Example using PySpark:

### 1) Creating a virtual environment:

I used ```conda``` as a virtual environment:

-----
        
    conda create -n env
    conda activate env
### Official manual installing:

[Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

-----

### 2) Install requirements packages:

    conda install conda-forge::pyspark
    conda install openjdk
    conda install -c conda-forge findspark

### 3) Download archive [spark-hadoop](https://spark.apache.org/downloads.html) and unpack to dir ``C:\apps``

P.S Create dir

----

### 4) Setting system environment variables

### Windows:

1) Go to the 'Environment Variables' section
2) Create three variables ``HADOOP_HOME``, ``SPARK_HOME``, ``JAVA_HOME`` 
and set the path where unpack ``spark-hadoop`` is stored, for ``JAVA_HOME``, indicate the path to jdk(
Usually this ``C:\\Program Fiiles\Java\jdk_x``)
3) Finding the ``Path`` variable
4) Adding variables

        %JAVA_HOME%\bin
        %SPARK_HOME%\bin
        %HADOOP_HOME%\bin

More details in the [official documentation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

Our environment for PySpark is ready

-----

### 5) Import requirements modules

    from pyspark.sql import SparkSession, Row
    from pyspark.sql.functions import col, count

    import findspark

    findspark.init()
    findspark.find() # Exports required system environment variables

    ....