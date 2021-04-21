# Databricks notebook source
# This does not work
from ..common import params

# COMMAND ----------

# MAGIC %sh 
# MAGIC # We will run this python from now on and explore things
# MAGIC cat rel_import.py

# COMMAND ----------

# MAGIC %sh python -m rel_import

# COMMAND ----------

# MAGIC %sh 
# MAGIC cd ..
# MAGIC python -m step2.rel_import

# COMMAND ----------

# DBTITLE 1,This works
# MAGIC %sh 
# MAGIC cd ../..
# MAGIC python -m python_rel_imports.step2.rel_import

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Any python source file when executed will have an associated \_\_package\_\_ and \_\_name\_\_ variables. We printed these variables in rel_import.py
# MAGIC 
# MAGIC **You can do relative imports only with respect to the "package" name**
# MAGIC 
# MAGIC As you can see in the above commands `..` works if package has 2 levels
# MAGIC ```
# MAGIC If package_name = 'a.b.c' 
# MAGIC package . = a.b.c
# MAGIC package .. = a.b
# MAGIC package ... = a
# MAGIC package .... = error
# MAGIC ```
# MAGIC 
# MAGIC https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time has some nice comments about this subject
