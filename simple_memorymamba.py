import torch
import torch.nn as nn
from VMamba.classification.models_qa import build_vssm_models_ as our_model
import torch.nn.functional as F

classes = 10
model = our_model(cfg="vssm_tiny")
model.classifier.head = nn.Linear(model.classifier.head.in_features, classes)
model.cuda()
    
images = torch.randn(10, 3, 224, 224).cuda()
output, attn, loss_ce = model(images)
print(output.size())
