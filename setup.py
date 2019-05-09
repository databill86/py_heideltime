from setuptools import setup, find_packages
files = ["py_heideltime/*"]
setup(name='py_heideltime',
      version='1.0',
      description='module in python using java standalone Heideltime from https://github.com/HeidelTime/heideltime',
      author='Jorge Alexandre Rocha Mendes',
      author_email='mendesjorge49@gmail.com',
      url='https://github.com/JMendes1995/py_heideltime.git',
      packages=find_packages(include=['py_heideltime', 'package']),
      package_data = {'package' : files},
      py_modules=['py_heideltime']
)



