from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      license = "MIT License",
      description='Python implementation of quine mccluskey algorithm',
      author='Kumbong Hermann',
      author_email='kumbonghermann@gmail.com',
      url='',
      packages=['gui','qm' ,'tests'],
      long_description=open('README.md').read(),
     )

