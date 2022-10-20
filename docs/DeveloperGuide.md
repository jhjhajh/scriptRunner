# Developer Guide

## Table of Contents
1. [Introduction](#1-introduction)
2. [About this Guide](#2-about-this-guide)
3. [Installation](#3-installation)

   3.1 [System Requirements](#31-system-requirements)

   3.2 [Installation Instructions](#32-installation-instructions)

4. [Implementation](#4-implementation)

   4.1 [Tech Stack](#41-tech-stack)

   4.2 [General Architecture](#42-general-architecture)

   4.3 [Configuration File](#43-configuration-file)

   4.4 [Generate Config](#44-generate-config)

   4.5 [Start Instances](#45-start-instances)


## 1. Introduction

This application seeks to help in managing and streamlining adversary emulation. 

## 2. About this Guide

This guide would explain how the application is implemented and some limitations of this application. You can refer to the [userguide](userguide.md) for more information about how you can use the application.

## 3. Installation

### 3.1 System Requirements

This application requires Python 3.10 or later to work. You can either install the latest version of python on your system directly or install it in a virtual environment.

Prefered Operating System: Linux or MacOS

You can run the application on Windows system by running the `main.py` file directly in the `/app` folder. You would need to change the `start_instances.sh` to a script that is compatible with Windows OS for starting of instances, or do it outside of the app.

### 3.2 Installation Instructions

1. Install tkinter using the command below.

    `sudo apt install python3-tk -y`

2. Install the rest of the depenencies using the requirements.txt file using the command below.

    `pip install -r requirements.txt`

## 4. Implementation


### 4.1 Tech Stack

Tkinter package is used to build this application and custom_tkinter is used to improve on the interface of the application. In order to use the tkinter package, Python3.10 is required. You can refer to the links below to find out more about the packages and libraries.

tkinter: https://docs.python.org/3/library/tkinter.html 

custom_tkinter: https://github.com/TomSchimansky/CustomTkinter 

### 4.2 General Architecture

The python code that is used to build the application resides in the `app` folder. `data.txt` is where data is stored, and `run.sh` allows users to run the application without having to open the `app` folder.

`main.py` builds the general homepage or landing page of the application. 

The popup windows are in `pop.py`.

