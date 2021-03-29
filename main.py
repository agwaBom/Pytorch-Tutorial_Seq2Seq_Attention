# It's basically the equivalent of "I guess you're not ready for this, but your kids are gonna love it". 
from __future__ import unicode_literals, print_function, division

import preprocessing

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as f


#device = torch.device("cuda" if torch.cuda.is_avaliable() else "cpu")

input, output, pairList = preprocessing.prepareData('eng', 'fra')
print("input : ", input)
print('output : ', output)
print('pairlist : ', pairList)

