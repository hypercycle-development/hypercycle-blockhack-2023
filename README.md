# HyperCycle BlockHack 2023 Repo

This contains resources related to the HyperCycle challenges at BlockHack 2023.


# Writing AI Machines

An AI Machine (AIM) is a packaged AI model that lets other machines run your model in
a compatable way that includes cost logic, so other machines can know how to charge
for using your model. The `hackathon_aim_examples` includes examples of how to create
such a service, and DockerDiles for creating the corresponding docker images.

Examples given are:

## Greeting AIM

This is a simple "Hello World!" AIM, using the pyhypercycle-aim library

## Queue AIM

This is an example AIM that uses a builtin queue system to better manager GPU memory
usage. See app/main.py for more information

## ZTranslate AIM

This is a self-contained exaple AIM that doesn't use the pyhypercycle-aim library, and 
includes all the needed header and body information needed to get a custom aim to run.


## The pyhypercycle-aim Package

The pyhypercycle-aim package is available at https://github.com/hypercycle-development/pyhypercycle-aim
and includes the helper classes being used to create AIMs. To install it, include the following in your
requirements.txt file:  

`git+https://github.com/hypercycle-development/pyhypercycle-aim.git#egg=pyhypercycle_aim`







