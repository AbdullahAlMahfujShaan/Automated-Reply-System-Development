<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p align="center"><strong><img src="https://media.dhakatribune.com/uploads/2016/11/nsulogo.jpg" alt="" width="307" height="172" /></strong></p>
<p align="center"><strong>North South University</strong></p>
<p align="center">Department of Electrical &amp; Computer Engineering</p>
<p align="center"><strong>Project Description</strong></p>
<p align="center"><strong>Spring 2021</strong></p>
<p align="center"><strong>Project Name</strong>: NSU Chatbot</p>
<p align="center"><strong>Course No</strong>: CSE 498R <strong>Sec</strong><strong>:</strong> 8</p>
<p align="center"><strong>Faculty</strong>: Shaikh Shawon Arefin Shimon (SAS3)</p>
<p align="center"><strong><u>Member Detail</u></strong></p>
<p align="center"><strong>Name</strong><strong>:</strong> Abdullah Al Mahfuj Shaan</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1721275042</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:abdullah.mahfuj@northsouth.edu">abdullah.mahfuj@northsouth.edu</a></p>
<p align="center"><strong>Name</strong><strong>:</strong> Monsur Hillas</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1721911042</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:monsur.hillas@northsouth.edu">monsur.hillas@northsouth.edu</a></p>
<p align="center"><strong>Name</strong><strong>:</strong> Md. Jubaer Khan</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1721616042</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:jubaer.khan@northsouth.edu">jubaer.khan@northsouth.edu</a></p>
<p align="center"><strong>Git Repository</strong><strong>: </strong><a href="https://github.com/AbdullahAlMahfujShaan/Automated-Reply-System-Development">https://github.com/AbdullahAlMahfujShaan/Automated-Reply-System-Development</a></p>
<p align="center"><strong>Date Prepared</strong><strong>: </strong>05/05/2021</p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>

## Getting Started (Windows)

## Required Softwares
- [PyCharm IDE] - for Python based projects or any other equivalent
- [Anaconda Navigator] - the open-source Individual Edition (Distribution) is the easiest way to perform Python/R data science and machine learning on a single machine. 

## Installation

Create virtual environment using Anaconda Prompt for developing the project. 

```
conda create --name YOURENVNAME python=3.8 anaconda
```
After we create the virtual environment we must activate it:

```
conda activate YOURENVNAME
```

Install Tensorflow CPU

Note: If you have a CUDA Enabled environment you can install Tensorflow GPU, but in that case this code will not work, as this is developed using CPU.

```
pip install tensorflow-cpu
```

Install NLTK

```
pip install nltk
```


## Getting Started (Linux)

## Required Softwares
- [PyCharm IDE] - for Python based projects or any other equivalent
- [Anaconda Navigator Linux] - the open-source Individual Edition (Distribution) is the easiest way to perform Python/R data science and machine learning on a single machine. 

## Installation
### Anaconda Installation
Download Anaconda (Check Latest Version before downloading)

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
```
Run Anaconda3 Installation Script on Ubuntu or CentOS
If you have downloaded it using the browser, then the installation script will automatically go to Downloads folder thus switch to that. Or to the folder where you have saved it.

```
cd Downloads
```

```
ls
```
Now, use the following syntax

```
./filename
```
or

```
bash filename
```

The filename is the name of the Anaconda Linux installation script. In our case it was Anaconda3-2020.07-Linux-x86_64.sh, thus the command will be:

```
./Anaconda3-2020.07-Linux-x86_64.sh
```

or

```
bash Anaconda3-2020.07-Linux-x86_64.sh
```

Accept the terms and conditions
The installer will ask you to accept the terms and conditions, that would be a long list. So, if you don’t want to go through it, simply press Ctrl+C and then press Y to accept that.

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
```

Create virtual environment using Anaconda Prompt for developing the project. 

```
conda create --name YOURENVNAME python=3.8 anaconda
```
After we create the virtual environment we must activate it:

```
conda activate YOURENVNAME
```

Install Tensorflow CPU

Note: If you have a CUDA Enabled environment you can install Tensorflow GPU, but in that case this code will not work, as this is developed using CPU.

```
pip install tensorflow-cpu
```

Install NLTK

```
pip install nltk
```

At the beginning the project will give an error to download 'punkt' to resolve this error go to chatbot.py and comment out 'nltk.download('punkt')'
Run this for once and comment it again.

## Getting the repository

This repository can be downloaded and also cloned by the following steps, you can try either.
[git](https://git-scm.com/) repository:

    git clone https://github.com/AbdullahAlMahfujShaan/Automated-Reply-System-Development

or [download a zip archive](https://github.com/AbdullahAlMahfujShaan/Automated-Reply-System-Development).


## Folder Tree
- static : this folder contains the css and js scripting files
- templates : this folder contains the HTML scripts for the frontend
- chatbot.py : this is the code for the model
- intents.json : dataset for training the model
- main.py : main file for running the whole project, it contains the flask api code.
- model.h5 : output created by running chatbot.py which is then used by main.py to use it for the project.

**Goodluck!!!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.)

 
   [PyCharm IDE]: <https://www.jetbrains.com/pycharm/>
   [Anaconda Navigator]: <https://www.anaconda.com/products/individual>
   [Anaconda Navigator Linux]: https://docs.anaconda.com/anaconda/install/linux/
