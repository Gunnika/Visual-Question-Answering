# Visual-Question-Answering

## Integrated model: 
Requires annotations file from: https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Train_mscoco.zip

Other files are contained in Files folder of repo.

## Bert.pkl
https://drive.google.com/file/d/1rStLsUbgAC1uU7Mai5X_-c0qJPxnJk63/view?usp=sharing

## Dataset we are using:

### VQA v2.0 
(https://github.com/GT-Vision-Lab/VQA/blob/master/README.md)
It consists of : 

- Real
  - 82,783 MS COCO training images, 40,504 MS COCO validation images and 81,434 MS COCO testing images (images are obtained from [MS COCO website] (http://mscoco.org/dataset/#download))
  - 443,757 questions for training, 214,354 questions for validation and 447,793 questions for testing
  - 4,437,570 answers for training and 2,143,540 answers for validation (10 per question)
  
- There is only one type of task - 
Open-ended task


## Research paper we are referring to: 
https://arxiv.org/abs/1704.03162

PDF : https://arxiv.org/pdf/1704.03162.pdf

## Base Code:

https://github.com/iamaaditya/VQA_Demo

https://github.com/iamaaditya/VQA_Keras


## Other Datasets : 
https://visualqa.org/download.html,

https://arxiv.org/abs/1905.13648,

https://tryolabs.com/blog/2018/03/01/introduction-to-visual-question-answering/

https://iamaaditya.github.io/2016/04/visual_question_answering_demo_notebook

https://paperswithcode.com/task/visual-question-answering

https://vqa.cloudcv.org/


## Useful Resources:
https://keras.io/getting-started/functional-api-guide/

https://github.com/Cyanogenoid/pytorch-vqa

https://github.com/nithinraok/VisualQuestion_VQA

Improvements over this code : 

https://github.com/Cyanogenoid/vqa-counting/tree/master/vqa-v2

https://github.com/KaihuaTang/VQA2.0-Recent-Approachs-2018.pytorch

## Models
https://github.com/KaihuaTang/VQA2.0-Recent-Approachs-2018.pytorch has reimplemented several approaches using the following models: 

1. Bottom up and Top Down Attention
https://arxiv.org/abs/1707.07998
Uses a combined top-down and bottom-up attention mechanism to calculate attention at object level and over other notable regions of the image. The bottom-up mechanism is based on Faster R-CNN and proposes image regions, each with an associated feature vector while the top-down mechanism determines feature weightings. 

2. Bilinear Attention Networks
https://arxiv.org/abs/1805.07932
This paper proposes bilinear attention networks (BAN) that find bilinear attention distributions to utilize given vision-language information seamlessly, along with a variant of multimodal residual networks to exploit eight-attention maps of the BAN efficiently. 

3. Intra- and Inter-modality Attention
https://arxiv.org/abs/1812.05252
Proposes a novel method of dynamically fusing multi-modal features with intra- and inter-modality information flow that passes dynamic information between and across the visual and language modalities to robustly capture high-level interactions between language and vision domains, significantly improving VQA performance. 

4. Learning to count
https://arxiv.org/abs/1802.05766
VQA models thus far have struggled with counting objects in natural images.This paper identifies a fundamental problem due to soft attention in the models as a cause and proposes a neural network component that allows robust counting from object proposals.

5. Learning Conditioned Graph Structures
https://arxiv.org/abs/1806.07243
Very few VQA models rely on higher level image representations capable of capturing semantic and spatial relationships. This paper proposes a graph-based approach that combines a graph learner module, which learns a question specific graph representation of the input image, with the recent concept of graph convolutions, aiming to learn image representations that capture question specific interactions. It uses VQA v2 dataset using a simple baseline architecture enhanced by the proposed graph learner module. 
