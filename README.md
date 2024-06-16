# time-to-event

## Time to event (Survival Analysis) 

### Introduction to Survival Analysis

The aim of survival analysis, also known as reliability analysis in engineering, is to link covariates with the timing of an event. This field derives its name from clinical research, where the primary goal is often to predict the time until death, or survival. Survival analysis is a specialized form of regression problem, where the goal is to predict a continuous outcome. However, it stands out from conventional regression because some training data is only partially observed, or **censored**.

In simple terms, it predicts the probability of an event happening after a period of time has passed. For example, the probability of a patient to survive a stage IV Cancer after their diagnosis. 

It's one of the fundamental model families in clinical research and drug discovery as usually, researchers use these type of analyses to evaluate a treatment's efficacy and/or superiority. 

Let's look at this image. 

![survival analysis](docs/censoring.png?raw=true "Survival Analysis")

Patient A was lost to follow-up after three months without a recorded cardiovascular event, patient B experienced an event four and a half months after enrollment, patient D withdrew from the study two months after joining, and patient E did not have any event before the study concluded. Thus, the exact time of a cardiovascular event is only known for patients B and C, whose records are uncensored. For the other patients, it remains unknown whether they experienced an event after the study ended. The only available information for patients A, D, and E is that they were event-free up to their last follow-up, resulting in their records being censored.

This repo has some tutorials and examples on how to apply these type of models in a clinical context.

### Installation

**NOTE**: Using a Bash terminal is recommended for the set up. 

It is assumed Python and Conda have been installed. 

Make sure you have the latest version of pip install: `python -m pip install --upgrade pip`

I highly recommend building a new virtual environment. You can use conda for example (replace <ENVNAME> by your desired v-env name): 

`conda create -n <ENVNAME> python==3.12`

activate your virtual environment after you created it.

`conda activate <ENVNAME>`

Build the module. This will allow to import methods and classes from the package seamlessly.


### Build the module

First, install the build package. This will allow you to build the Python Module and install its dependencies. 

`python -m pip install build`

or

`pip install --upgrade build`

then, Build the `time_to_event` module using: 

`python -m build`

Finally, install all dependencies that are in the `setup.py` file with 

`pip install -e .`

## Tutorials and assigments

In the analysis folder you have the [Introduction](./analysis/introduction.ipynb) and [RandomForest](./analysis/RandomForest.ipynb) notebooks. I recommend studying them in that order. 
The class assigment introduction is in [assigment](./analysis/assignment.ipynb)