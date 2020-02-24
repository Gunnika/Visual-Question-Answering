Questions picked up from the file v2_OpenEnded_mscoco_train2014_questions.json were converted to a dataframe in vocab_new.ipynb. The first 10k rows of this df are contained in the questionsdf.csv file. It contains questions for 1919 images.  
Of these 1919 images, 6 were greyscale (ids contained in excluded_image_ids.npy). These were excluded from the sample dataset. 
Image vectors for images in the sample dataset were then generated. Thus:  
  
1. excluded image_ids.py: IDs of 6 greyscale images (out of initial 1919) that were excluded from sample dataset  
2. image_IDs.npy: image IDs corresponding to image vectors generated  
3. image_vectors_with_ids.csv.zip: csv of image IDs (same as image_IDs.npy) with their corresponding vectors  
4. img_vectors_sample.npy: image vectors of images in sample set (in same order as IDs in file #2)  
5. questionsdf.csv file: image_id,question,question_id from first 10k rows of df from questions json  
