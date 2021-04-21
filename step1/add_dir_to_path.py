# Databricks notebook source
import sys
import os

sys.path.append(os.path.abspath('..'))

# COMMAND ----------

import common.params
print(common.params.get_params())

# COMMAND ----------

from common import params
print(params.get_params())
