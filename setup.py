from setuptools import setup, find_packages

setup(name='screenshot2latex',
      version=0.1,
      description='takes a screenshot, converts it to latex, pastes latex to clipboard',
      url='https://github.com/rmst/screenshot2latex',
      author='Simon Ramstedt',
      author_email='',
      license='MIT',
      zip_safe=False,      
      install_requires=[
          'pyperclip',
      ],
      scripts=['scripts/screenshot2latex'],
      extras_require={},
      packages=find_packages(),	
)
