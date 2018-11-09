#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 02:02:38 2018

@author: ColinSheehan
"""

ls
import numpy
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm
from plotnine import *
new=pd.read_csv("data.txt")
bar1=ggplot(new)+theme_classic()+xlab("regional area")+ylab("number of observations")
bar2=bar1+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=numpy.mean)
ggsave(filename="Barplot01.png", plot=bar2)
scatter2=ggplot(new)+aes(x="factor(region)", y="observations")+geom_point()+geom_jitter()
scatter2
ggsave(filename="scatterplot02.png", plot=scatter2)

#the two plots suggest different things. While the means of the regional data are all
#relatively similar, the scatterplot of individual points reveals that they in fact
#are very different populations. Some are highly variant and others are not. 