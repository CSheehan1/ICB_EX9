#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 01:23:36 2018

@author: ColinSheehan
"""

import numpy
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm
from plotnine import *
vote=pd.read_csv("votingdata.csv")
data=vote.iloc[:,1:3]
data
population_size_million=data.iloc[:,0]
population_size_million
PDEM=data.iloc[:,1]
scatter=ggplot(mpg)+aes(x='population_size_million', y='PDEM')+geom_point()+ggtitle("American city population density and Democratic Votes during Midterm Election")+xlab("population size in millions")+ylab("Percentage Democratic Votes")
scatter
scatter+scale_x_log10()
scatter2=scatter+scale_x_log10()+geom_smooth(method = "lm")
ggsave(filename="Scatterplot01.png", plot=scatter2)