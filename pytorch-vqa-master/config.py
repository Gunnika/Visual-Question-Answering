# paths
qa_path = '/Volumes/Seagate/VQA/vqa'
# directory containing the question and annotation jsons:
# 1. OpenEnded_mscoco_train2014_questions.json
# 2. OpenEnded_mscoco_val2014_questions.json
# 3. mscoco_train2014_annotations.json
# 4. mscoco_val2014_annotations.json

# /Users/inika/Desktop/Shortcuts/mini/Visual-Question-Answering/VQA
train_path = '/Users/inika/Desktop/Shortcuts/mini/Visual-Question-Answering/VQA/scene_img_abstract_v002_train2015'  # directory of training images
val_path = '/Users/inika/Desktop/Shortcuts/mini/Visual-Question-Answering/VQA/scene_img_abstract_v002_val2015'  # directory of validation images
test_path = '/Users/inika/Desktop/Shortcuts/mini/Visual-Question-Answering/VQA/scene_img_abstract_v002_test2015'  # directory of test images

preprocessed_path = './resnet-14x14.h5'  # path where preprocessed features are saved to and loaded from
vocabulary_path = 'vocab.json'  # path where the used vocabularies for question and answers are saved to

task = 'OpenEnded'
dataset = 'mscoco'

# preprocess config
preprocess_batch_size = 64
image_size = 448  # scale shorter end of image to this size and centre crop
output_size = image_size // 32  # size of the feature maps after processing through a network
output_features = 2048  # number of feature maps thereof
central_fraction = 0.875  # only take this much of the centre when scaling and centre cropping

# training config
epochs = 50
batch_size = 128
initial_lr = 1e-3  # default Adam lr
lr_halflife = 50000  # in iterations
data_workers = 8
max_answers = 3000
