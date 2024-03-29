# se-project-edr

**Software Engineering 1** (SY 2023-2024): **Eye Disease Recognition Project**

Borigas, Chris John

Loria, Jerome A.

Rayco, Jovic Francis B.

Sabal, Joanna Regina

Sy, Jan Wilhelm T.

## About

We are all new to using GitHub, even more so in handling a Software Engineering project. This README.md document is all about informing each of us what we need to setup in order to do the project.

## Notes on Environment Variables
To allow us to view the site on phone and
prevent including id addresses in commits:
Run this in cmd:
> pip install django-environ
Create a '.env' file in 'edr-django/edr-django'
Find your machine's ip address by running in cmd:
> ipconfig
It will output something like:
> Wireless LAN adapter Wi-Fi: 
> Connection-specific DNS Suffix  . :
> Link-local IPv6 Address . . . . . : (alphanumeric stuff)
> IPv4 Address. . . . . . . . . . . : 192.168.x.x
> Subnet Mask . . . . . . . . . . . : (255 numeric stuff)
> Default Gateway . . . . . . . . . : (192 168 numeric stuff)
The IPv4 Address is the address of your machine on the network
Write this line in the .env file:
> ALLOWED_HOSTS=localhost,127.0.0.1,192.168.x.x
Replace x.x with the last two numbers of your machine's ip address

Now run this in the outer edr-django directory:
> python manage.py runserver 0.0.0.0:8000

On your machine, enter 127.0.0.1:8000 in your browser.
On phone or other computers connected to the same network,
enter <IP address>:8000

## Step-by-Step

This section contains information on what to setup.

Disclaimer: most of this section is filled with YouTube video links

Disclaimer: this document is a work in progress. do inform me of concerns/conflicts

Note: On **what to do** refer to our PD8 and previous PDs. PD8 represents the requirements needed by the 3 sections (Model, FrontEnd, Backend)


### PREPARATION: Git and GitHub Desktop

**I. Follow This Tutorial**
> https://www.youtube.com/watch?v=8Dd7KRpKeaE

> Remember, Branch before doing your changes/commits to avoid merge conflicts. Do pull requests if you want me to merge your branch to main.

**I (Alternative). Ask me for demonstrations on Discord if the tutorial is hard to follow**
> Inform me through messenger if you need guidance/help

> You can also ask other members that know basic knowledge in using Git and GitHub Desktop




### DEVELOPMENT: General Setup (CNN Model Training, Coding)

**NOTE**: Jan Has a Jupyter Pipeline that will help in the tensorflow installation process.

**NOTE 2**: Backend may still want to watch **II.** for the model use instructions(?)

**I. Coding | CNN Setups:** https://www.youtube.com/watch?v=19LQRx78QVU
> This has most of the applications/tools we’ll use for the project

> Consider this as our Jupyter tutorial as well

> The GPU Section is Optional

**II. Data Gathering + CNN Training:** https://www.youtube.com/watch?v=jztwpsIzEGc
> This has instructions for our data gathering for the CNN model

> Remember to fill up our data directory




### DEVELOPMENT: KIVY/KIVYMD
NOTE: KIVY MD contains resources for a more modernized/clean UI look. While KIVY is just the normal framework.

**I. Setting up Kivy/KivyMD for VSCode**
> (Kivy) From Docs: https://kivy.org/doc/stable/gettingstarted/installation.html

> (KivyMD) From Docs: https://kivymd.readthedocs.io/en/1.1.1/getting-started/

> TLDR; just use the pip commands from the links above to install Kivy, and KivyMD

**I(Alternate). Setting up Kivy/KivyMD for PyCharm Users + Tutorials**
> Found this tutorial, uses PyCharm so unsure if applicable to others: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-&index=1

**II. DOCS (Use them in accordance to what requirements are to be addressed)**
> https://kivy.org/doc/stable/

> https://kivymd.readthedocs.io/en/1.1.1/index.html

> You can use other tutorials in youtube.




### BUILDING: BUILDOZER
**I. Installation and Use of Buildozer**

> https://www.youtube.com/watch?v=pzsvN3fuBA0

