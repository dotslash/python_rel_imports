print("name=", __name__)
print("package=", __package__)
print("running 'from ..common import params'")

from ..common import params

def work():
  print(params.get_params())
  
work()