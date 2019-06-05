from distutils.core import setup

long_description = '''
This package is an add on library on top of keras or tensorflow.
The aim of this package is to provide privacy of images by enabling the model to be trained on encrypted images.

Read the documentation at: https://github.com/akshaybahadur21/keras-secure-image

For a detailed code overview on colab, see:
https://colab.research.google.com/drive/1D7ziODKrzL0QK-GuI7BH9f9Fk7U3tfUW

keras-secure-image is compatible with Python 2.7-3.6
and is distributed under the MIT license.

'''

setup(
  name = 'keras-secure-image',         
  version = '0.3.1',      
  license='MIT',       
  long_description = long_description,
  description='Add on library for deep learning on encrypted images'
  author = 'Akshay Bahadur',                   
  author_email = 'akshaybahadur21@gmail.com',      
  url = 'https://github.com/akshaybahadur21',   
  download_url = 'https://github.com/akshaybahadur21/keras-secure-image/archive/v0.3.tar.gz',
  keywords = ['KERAS', 'SECURITY', 'PRIVACY', 'DEEP LEARNING'],   
  install_requires=[            
          'numpy',
          'Pillow',
	  'scikit-image'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      	

    'Intended Audience :: Developers',      	
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   

    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
