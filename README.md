# ncomms2022——多模态dementia诊断

## 一、任务目标

通过图像数据（核磁共振MRI影像）和非影像数据（主要是临床数据）对认知状态进行分类。

NC——正常认知

MCI——轻度认知障碍

AD——阿兹海默痴呆

nADD——非阿兹海默痴呆

ncomms2022项目主要将任务分为两块：一是COG任务（三分类），分类NC、MRI、DE；二是ADD任务（二分类），是对COG任务中的DE进行细分，AD和nADD。

## 二、环境配置

Pytorch>=1.10

Numpy>=1.19

TQDM>=4.31

Nibabel>=3.2

matplotlib>=3.3

scikit-learn>=0.23

scipy>=1.5.4

SHAP>=0.37

XGBoosh>=1.3.3

catboost>=0.24

## 三、数据集下载

### 1、ADNI

非影像数据：需要慢慢筛选。（网站上的名称和实际下载的文件名不一致，需要慢慢筛选）

![image-20231226134946769](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226134946769.png)

![image-20231226134938125](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226134938125.png)

影像数据：原论文及项目中未提及具体如何选取。在ADNI官网中随机挑选了一个共享集合进行下载。数据量大且不知道是否与非图像数据匹配。

![image-20231226134713302](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226134713302.png)

![image-20231226134718742](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226134718742.png)

### 2、NACC

非影像数据：需要向机构申请

![image-20231226135112455](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135112455.png)

影像数据：数据量大（预计25G以上）且不知道是否与非图像数据匹配。原论文及项目中未提及具体如何选取。（目前下载失败）

![image-20231226135148344](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135148344.png)

## 四、数据预处理及训练集划分

### 1、进入derived_tables文件夹，根据不同数据集生成元数据。

![image-20231226135240165](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135240165.png)

### 2、进入datasets_tables文件夹，为不同数据集准备最终的元表。

![image-20231226135255190](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135255190.png)

![image-20231226135259003](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135259003.png)

![image-20231226135306614](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135306614.png)

其中需要以图片路径作为索引，选取记录元素，并得到列名

### 3、进入CrossVaild文件夹，划分训练集、测试集、验证集。

![image-20231226135335118](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135335118.png)

combine.py将所有数据集整合到一个all.csv文件中。

split.py将all.csv划分为训练集、测试集、验证集。

appendNonImage.py将所有非图像元素加入到训练集、测试集、验证集中。（列名）

![image-20231226135351264](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135351264.png)

## 五、训练模型(NoImg)

准备好训练集、测试集、验证集后（目前仅有ADNI1中的1/10），训练CNN模型（由于没有NACC，只能COG任务）（test.ipynb）

![](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135555541.png)



nonImg_task_config.json选取合适特征，保证特征维度匹配

![image-20231226135627801](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135627801.png)

绘制ROC曲线及PR曲线

![image-20231226135732650](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135732650.png)

![image-20231226135744709](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135744709.png)

![image-20231226135752845](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135752845.png)

Shap可解释分析

![image-20231226135809749](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135809749.png)

![image-20231226135815008](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20231226135815008.png)





NC,MCI,DE,COG,AD,PD,FTD,VD,DLB,PDD,ADD,ALL,OTHER

1,      0,    0,    0,    0,   0,    0,    0,    0,      0,       ,     0,     0
