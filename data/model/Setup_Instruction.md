Model is found at our gdrive. it is too large to be placed here in GitHub

For Setup Purposes, here are some instructions on model training (do ask me and jan first before following them):

These are best read through a text editor

# Installation of Tensorflow GPU
## Will most likely work

A. CREATING CONDA ENVIRONMENT (https://www.youtube.com/watch?v=QUjtDIalh0k&t=138s)

** TensorFlow 2 Setup Link **
https://www.tensorflow.org/install/pip#windows-native


** INSTALL **
1. conda create -n py310 python=3.10

2. conda activate py310

3. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

4. python -m pip install "tensorflow=2.10"

** Test GPU **

conda activate py310 

python

import tensorflow as tf

tf.config.list_physical_devices('GPU')

tf.test.is_gpu_available()


B. CONNECTING TO JUPYTER LAB

1. Make sure your conda environment is activated 

conda activate py310 

2. Install Environemnt to Jupyter 

conda install -n your_environment_name jupyterlab

3. Install Other Dependencies

conda install -n py310 scikit-learn

conda install -n py310 pillow

3. Open Jupyter Lab

jupyter lab