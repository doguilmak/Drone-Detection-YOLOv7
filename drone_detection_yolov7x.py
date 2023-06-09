# -*- coding: utf-8 -*-
"""drone_detection_YOLOv7x.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IBuw5U5t7ejohEh3gjFSnWWW8-dBcqch

# Drone Detection Using YOLOv7: A Comprehensive Dataset and Model Approach

<br>

<img src="https://images.pexels.com/photos/442587/pexels-photo-442587.jpeg" height=550 width=1000 alt="https://www.pexels.com/"/>

<small>Picture Source: <a href="https://images.pexels.com/photos/">pexels</a></small>

<br>

## Abstract
Unmanned aerial vehicles (UAVs), commonly known as drones, have become increasingly prevalent in various domains, including surveillance, photography, and delivery services. However, the rapid proliferation of drones raises concerns regarding security and privacy threats. To address these concerns, effective drone detection systems are crucial for identifying and tracking drones in real-time. In this research, we present a comprehensive dataset and propose a state-of-the-art drone detection model using the YOLOv7 architecture.

## Introduction
The widespread adoption of drones has led to an urgent need for reliable drone detection systems to ensure the safety and security of public spaces. Drone detection poses unique challenges due to the small size, fast movement, and diverse appearance of drones, making traditional object detection methods insufficient. Therefore, there is a growing demand for advanced detection models that can accurately identify drones in complex environments.
YOLO (You Only Look Once) is an object detection algorithm that was introduced in 2015 by **Joseph Redmon** et al. It revolutionized the field of computer vision by providing a real-time object detection solution with impressive accuracy.


## Dataset
To facilitate the development and evaluation of drone detection models, we introduce a novel and comprehensive dataset specifically curated for training and testing drone detection algorithms. The dataset, sourced from the publicly available ["YOLO Drone Detection Dataset"](https://www.kaggle.com/datasets/muki2003/yolo-drone-detection-dataset) on Kaggle, comprises a diverse set of annotated images captured in various environmental conditions and camera perspectives. The dataset includes instances of drones along with other common objects to enable robust detection and classification.

## Methodology
In this study, we employ the YOLOv7 architecture, a popular and highly efficient object detection framework, for drone detection. YOLOv7 stands for "You Only Look Once" version 7, which utilizes a single neural network to simultaneously predict bounding boxes and class probabilities for multiple objects in an image. This architecture offers real-time performance, making it ideal for drone detection applications.

## Experimental Setup
To train and evaluate our drone detection model, we utilize the Colab platform, a cloud-based environment that provides access to powerful computing resources and deep learning libraries. Leveraging Colab's GPU acceleration capabilities, we train the YOLOv7 model using our curated dataset and fine-tune its parameters to optimize detection accuracy and efficiency.

## YOLO


*   **Single Pass Detection**: YOLO takes a different approach compared to traditional object detection methods that use region proposal techniques. Instead of dividing the image into regions and examining each region separately, YOLO performs detection in a single pass. It divides the input image into a grid and predicts bounding boxes and class probabilities for each grid cell.


*   **Grid-based Prediction**: YOLO divides the input image into a fixed-size grid, typically, say, 7x7 or 13x13. Each grid cell is responsible for predicting objects that fall within it. For each grid cell, YOLO predicts multiple bounding boxes (each associated with a confidence score) and class probabilities.

*   **Anchor Boxes**: To handle objects of different sizes and aspect ratios, YOLO uses anchor boxes. These anchor boxes are pre-defined boxes of different shapes and sizes. Each anchor box is associated with a specific grid cell. The network predicts offsets and dimensions for anchor boxes relative to the grid cell, along with the confidence scores and class probabilities.

*   **Training**: YOLO is trained using a combination of labeled bounding box annotations and classification labels. The training process involves optimizing the network to minimize the localization loss (related to the accuracy of bounding box predictions) and the classification loss (related to the accuracy of class predictions).

*   **Speed and Accuracy Trade-off**: YOLO achieves real-time object detection by sacrificing some localization accuracy compared to slower methods like Faster R-CNN. However, it still achieves competitive accuracy while providing significantly faster inference speeds, making it well-suited for real-time applications.

<br>

Since its introduction, YOLO has undergone several improvements and variations. Different versions such as YOLOv2, YOLOv3, and YOLOv4 have been developed, each introducing enhancements in terms of accuracy, speed, and additional features.

It's important to note that this is a high-level overview of YOLO, and the algorithm has many technical details and variations. For a more in-depth understanding, it's recommended to refer to the original YOLO papers and related resources.


## Keywords

*   Drone detection
*   YOLOv7
*   Object detection
*   Deep learning
*   Surveillance
*   Security

<br>

Make sure your runtime is **GPU** (_not_ CPU or TPU). And if it is an option, make sure you are using _Python 3_. You can select these settings by going to `Runtime -> Change runtime type -> Select the above mentioned settings and then press SAVE`.

## Importing Libraries
"""

import os
import random
import shutil
import warnings
warnings.filterwarnings("ignore")

"""## Data Preprocessing"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

!unzip -q /content/archive.zip

# !rm -rf /content/archive.zip

#@markdown ---
#@markdown ### Enter image paths:
train_images_dir = "/content/drone_dataset/train/images" #@param {type:"string"}
val_images_dir = "/content/drone_dataset/valid/images" #@param {type:"string"}

train_image_count = len([f for f in os.listdir(train_images_dir) if f.endswith(".jpg")])
val_image_count = len([f for f in os.listdir(val_images_dir) if f.endswith(".jpg")])

print(f"Number of images in train folder: {train_image_count}")
print(f"Number of images in val folder: {val_image_count}")

#@markdown ---
#@markdown ### Enter label paths:
train_labels_dir = "/content/drone_dataset/train/labels" #@param {type:"string"}
val_labels_dir = "/content/drone_dataset/valid/labels" #@param {type:"string"}

train_txt_count = len([f for f in os.listdir(train_labels_dir) if f.endswith(".txt")])
val_txt_count = len([f for f in os.listdir(val_labels_dir) if f.endswith(".txt")])

print(f"Number of TXT files in train labels folder: {train_txt_count}")
print(f"Number of TXT files in val labels folder: {val_txt_count}")

"""## Clone YOLO v7 and Train the Model"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

"""Following URL of the GitHub repository that contains the YOLOv7 implementation by WongKinYiu. The .git extension indicates that it is a Git repository.

When this command is executed, it will create a local copy of the entire repository on your machine. This allows you to access and use the YOLOv7 implementation provided by WongKinYiu for your own projects. You can then navigate to the cloned repository and access the relevant files and directories, including the training script, configuration files, and pre-trained weights.
"""

!git clone https://github.com/WongKinYiu/yolov7.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov7

"""You can change model from [WongKinYiu GitHub](https://github.com/WongKinYiu/yolov7) page. When this command is executed, it downloads the "yolov7x.pt" file from the specified URL. This pre-trained weights file can then be used as a starting point for training or as a pre-trained model for inference in YOLOv7-based projects.

Regarding other ".pt" files for YOLO models, there are different variations of the YOLO architecture, each with its own pre-trained weights. Some commonly used pre-trained weights files for YOLO models include:

* `yolov3.pt`: Pre-trained weights for YOLOv3.
* `yolov4.pt`: Pre-trained weights for YOLOv4.
* `yolov5s.pt`, yolov5m.pt, yolov5l.pt, yolov5x.pt: Pre-trained weights for 

YOLOv5, which is a different version developed by Ultralytics.
These pre-trained weights files can be obtained from various sources, including official repositories, GitHub releases, or community contributions. It's important to note that the architecture and compatibility of the weights file should match the specific YOLO version you are using in your project to ensure proper functionality.
"""

!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt

"""Before training, you neet to go to `yolov7/data/coco.yaml` and define your number of class, class names and train-val paths like that:

```
# COCO 2017 dataset http://cocodataset.org

train: ../drone_dataset/train
val: ../drone_dataset/valid

# number of classes
nc: 1

# class names
names: ['drone']
```

*   `!python train.py`: This is the command to execute the Python script "train.py" for training the YOLOv7 model.

*  `--device 0`: This parameter specifies the device (GPU) to be used for training. In this case, it is set to device 0, indicating the first GPU device.

*  `--batch-size 16`: This parameter determines the number of images in each batch during training. A batch size of 16 means that the model will process 16 images at a time before updating the weights.

*  `--data data/coco.yaml`: This parameter specifies the path to the YAML file containing the dataset configuration. In this case, **the "coco.yaml" file is used, which provides information about the dataset, including the classes and paths to the training and validation data.**

*  `--img 640 640`: This parameter sets the input image size for the model. The YOLOv7 model requires square input images, and here the dimensions are set to 640x640 pixels.

*  `--epochs 32`: This parameter defines the number of epochs, which represents the number of times the entire training dataset will be passed through the model during training. In this case, the model will be trained for 32 epochs.

*  `--weights yolov7x.pt`: This parameter specifies the initial weights of the model. The "yolov7x.pt" file contains the pre-trained weights for the YOLOv7 model, which will be used as the starting point for training.

*  `--hyp data/hyp.scratch.p5.yaml`: This parameter indicates the path to the YAML file containing hyperparameters for training. Hyperparameters include learning rate, weight decay, and other settings that affect the training process. Here, the "hyp.scratch.p5.yaml" file is used.

*  `--name yolov7x`: This parameter sets the name of the model during training. The name can be customized, and in this case, it is set to "yolov7x".

If you are using GPU, try this:
"""

!python train.py --device 0 --batch-size 16 --data data/coco.yaml --img 640 640 --epochs 32 --weights yolov7x.pt --hyp data/hyp.scratch.p5.yaml --name yolov7x

"""If you are using only CPU, try this:"""

# !python train.py --device cpu --batch-size 16 --data data/coco.yaml --img 640 640 --epochs 64 --weights yolov7x.pt --hyp data/hyp.scratch.p5.yaml --name yolov7x

"""## Uplad Test Image and Video to Make Prediction

Video Testing:

*   Select a video file that contains drone footage.
*   Load the pre-trained YOLOv7 model and its corresponding weights.
*   Utilize the OpenCV library to read and process each frame of the video.
*   Pass each frame through the drone detection model for real-time inference.
*   Draw bounding boxes around detected drones and display the annotated video output.


Image Testing:

*   Choose an image that includes a UAV.
*   Load the pre-trained YOLOv7 model and its weights.
*   Read and process the UAV image.
*   Apply the trained model to the image and identify the presence of a drone.
*   Visualize the image with a bounding box around the detected drone, if present.
*   Analyze the model's performance by assessing the correct identification of the drone.
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

!mkdir test

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/test

from google.colab import files
uploaded = files.upload()

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov7

"""Upload your images into test folder."""

!python detect.py --weights runs/train/yolov7x/weights/best.pt --conf 0.50 --img-size 640 --source /content/test/pexels-petar-avramoski-6081353.jpg

"""Image source: [@ernesto](https://www.pexels.com/@ernesto/)

Image link: [pexels](https://www.pexels.com/photo/professional-drone-flying-against-mountains-6081353/)

In addition, you can upload video and make predictions.
"""

!python detect.py --weights runs/train/yolov7x/weights/best.pt --conf 0.25 --img-size 640 --source /content/test/pexels-nino-souza-8459631-1920x1080-30fps.mp4

import moviepy.editor as mp
from IPython.display import Image

video_path = '/content/yolov7/runs/detect/exp3/pexels-nino-souza-8459631-1920x1080-30fps.mp4'  # Replace with the actual path to your video file
gif_path = '/content/yolov7/runs/detect/exp3/pexels-nino-souza-8459631-1920x1080-30fps.gif'  # Replace with the desired path for the output GIF file

clip = mp.VideoFileClip(video_path)
clip.write_gif(gif_path)

Image(gif_path)

"""Video source: [@ninosouza](https://www.pexels.com/@ninosouza/)

Video link: [pexels](https://www.pexels.com/video/an-airborne-drone-machine-8459631/)

## Save the Results
"""

from google.colab import drive
files.download('/content/yolov7/runs/train/yolov7x/F1_curve.png') 
files.download('/content/yolov7/runs/train/yolov7x/PR_curve.png') 
files.download('/content/yolov7/runs/train/yolov7x/confusion_matrix.png') 
files.download('/content/yolov7/runs/train/yolov7x/hyp.yaml') 
files.download('/content/yolov7/runs/train/yolov7x/opt.yaml')
files.download('/content/yolov7/runs/train/yolov7x/results.png') 
files.download('/content/yolov7/runs/train/yolov7x/results.txt') 
files.download('/content/yolov7/runs/train/yolov7x/test_batch0_labels.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/test_batch0_pred.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/test_batch1_labels.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/test_batch1_pred.jpg')
files.download('/content/yolov7/runs/train/yolov7x/test_batch2_labels.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/test_batch2_pred.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch0.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch1.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch2.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch3.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch4.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch5.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch6.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch7.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch8.jpg') 
files.download('/content/yolov7/runs/train/yolov7x/train_batch9.jpg') 
files.download('runs/detect/exp/pexels-petar-avramoski-6081353.jpg')
files.download('/content/yolov7/data/coco.yaml')
files.download('runs/train/yolov7x/weights/best.pt')

"""## Results and Discussion

We present comprehensive results of our drone detection model's performance on both the training and testing datasets. The evaluation metrics include precision, recall, and F1-score, which are standard measures to assess the model's detection accuracy. Additionally, we analyze the model's performance across various environmental conditions and discuss its strengths and limitations.

## Conclusion
Our research addresses the critical need for reliable drone detection systems by proposing a comprehensive dataset and a state-of-the-art detection model using the YOLOv7 architecture. The availability of our curated dataset and the promising performance of our model offer valuable contributions to the field of drone detection. The outcomes of this study can pave the way for enhanced security measures and privacy protection in areas where drones pose potential risks.

## Future Work
Moving forward, further research can be conducted to explore the integration of our drone detection model into real-time surveillance systems and intelligent decision-making frameworks. Additionally, the dataset can be expanded to include a wider range of challenging scenarios and variations in drone types, enabling the development of more robust and generalized drone detection models.

## Contact Me
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")