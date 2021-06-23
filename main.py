# 待预测图片列表
image_list = ["./1.jpg", "./2.jpg", "./3.jpg", "./4.jpg", "./5.jpg","./6.jpg"]


import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

plt.figure(figsize=(15,15))

#显示图片
for i in range(6):
    img1 = mpimg.imread(image_list[i]) 
    plt.imshow(img1) 
    plt.axis('off') 
    plt.show()
    
with open('test.txt', 'r') as f:
    test_img_path=[]
    for line in f:
        test_img_path.append(line.strip())
print(test_img_path)

#加载预训练模型
import paddlehub as hub
#resnet50_vd_animals动物识别模型
module = hub.Module(name="resnet50_vd_animals")

#预测
import cv2
np_images =[cv2.imread(image_path) for image_path in test_img_path]

results = module.classification(images=np_images)

for result in results:
    print(result)
