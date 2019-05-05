from distutils.core import setup

long_description = '''
This package is an add on library on top of keras or tensorflow.
The aim of this package is to provide security for encrypting images.
The model is trained on the encrypted data
'''

setup(
  name = 'keras_secure_image',         
  packages = ['keras_secure_image'],   
  version = '0.1',      
  license='MIT',       
  long_description = long_description,   
  author = 'Akshay Bahadur',                   
  author_email = 'akshaybahadur21@gmail.com',      
  url = 'https://github.com/akshaybahadur21',   
  download_url = 'https://github.com/akshaybahadur21/keras-secure-image/archive/v_01.tar.gz',
  keywords = ['KERAS', 'SECURITY', 'DEEP LEARNING'],   
  install_requires=[            
          'numpy',
          'PIL',
		  'skimage'
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