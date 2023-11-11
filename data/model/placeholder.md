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


# Alternative way of getting py310 (instead of doing conda py310 activate)
## WARNING: This is untested and may not work

https://www.python.org/downloads/windows/

Go here
"""
 Python 3.10.11 - April 5, 2023

Note that Python 3.10.11 cannot be used on Windows 7 or earlier.

    Download Windows embeddable package (32-bit)
    Download Windows embeddable package (64-bit)
    Download Windows help file
    Download Windows installer (32 -bit)
    Download Windows installer (64-bit) <<<<<<<<<<<<<<<<<<<<<<<<<INSTALL
"""

On the installation screen, do 'custom' 
don't touch default settings/checkboxes except for one.
that 'one' is make sure check yung box na nagasabi ng 'add to system environment variables / path / somewhere along these lines'

Open "Edit the system environment variables" app in windows
Click Environment Variables
Under "user variables for user", open Path
Copy address of the python310 folder/directory (looks like C:\Users\user\AppData\Local\Programs\Python\Python310\) and open mo sa folder app, para makapunta ka
sa directory na yun

rename python.exe to python310.exe

open terminal
input python310 -- version to check if python 3.10.11 ang nainstall
if successful, good job

MAKE SURE you only call python310 from now on
setup your virtual environment
python310 -m pip install "tensorflow<2.11"

then follow the vid for the cuda /cudnn tutorial