#!/bin/bash
## script to setup local environment and install packages
## 1) Install python-pip
##      a)check for existing pip installation
## 2) configure linux environment for pip & ansible
## 3) install & configure pipenv


export 
if [ -d "$HOME/.local/bin" ]; then
    export PATH="$PATH:$HOME/.local/bin"
fi