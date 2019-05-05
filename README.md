# Keras Secure Image
[![](https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg?colorB=ff0000)](https://github.com/akshaybahadur21/Emojinator/blob/master/LICENSE.md)
[![](https://img.shields.io/badge/Akshay-Bahadur-brightgreen.svg?colorB=ff0000)](https://akshaybahadur.com)

This is an add-on library for Keras. The main functionality is to encrypt the images in the dataset so they are secure.
You can write your own generator and call the decrypt functionality at runtime. The decrypted images are not stored, they are stored in tuple by the generator ensuring the safety of your images.

## [Link to the colab notebook](https://colab.research.google.com/drive/1D7ziODKrzL0QK-GuI7BH9f9Fk7U3tfUW)

### Installation

`pip install keras_secure_image`

### Usage

#### Encrypting the images

```python
from keras_secure_image import encrypt_directory
encrypt_directory(src_dir="/path/to/src",
                                   dest_dir="/path/to/dest", image_x=100, image_y=100,
                                   password="<PASSWORD>)
												  
```
#### Training on encrypted images

```python
def generator_from_encrypted_data(path_to_features, labels, batch_size):
 batch_features = np.zeros((batch_size, 64, 64, 3))
 batch_labels = np.zeros((batch_size,1))
 while True:
   for i in range(batch_size):
     # choose random index in path_to_features
     index= random.choice(len(path_to_features),1)
     img = decrypt_data(path_to_img=path_to_features[index], password="<PASSWORD>", image_x=100, image_y=100)
     batch_features[i] = img
     batch_labels[i] = labels[index]
   yield batch_features, batch_labels
   
```

***Note*** : Check the line
```python
img = decrypt_data(path_to_img=path_to_features[index], password="<PASSWORD>", image_x=100, image_y=100)
```
This `decrypt_data` function takes the path to the image and decrypts it.
Make sure that the `<PASSWORD>` is the same for encryption.

Calling the fit_generator in Keras

```python
model.fit_generator(generator_from_encrypted_data(path_to_features,labels, 32),
                    samples_per_epoch=20, nb_epoch=10,
                    validation_data=generator_from_encrypted_data(features,labels, 16),
                    validation_steps=5, callbacks=callbacks_list, shuffle=True,use_multiprocessing=True)
```  
