# from setuptools import setup
#
# setup(name='Hello',
#       version='1.0',
#       description='A simple example',
#       author='zjx',
#       py_modules=['hello'])


from setuptools import setup, Extension

setup(name='palindrome',
      version='1.0',
      ext_modules=[
          Extension('palindrome', ['palindrome2.c',
                                   'palindrome2.i'])
      ])
