Application of Generative Adversarial Networks (GANs) for Medical Training
Christopher Myau (Team Leader), Andrew Moore, Jae Lee, Dauren Karatayev

Project Idea
This project will explore the application of generative adversarial networks (GANs) by utilizing artificial medical images as a training tool for medical students, residents, and radiologists. In the recent years, the application deep learning in radiology have gain rapid popularity, especially with GANs utility for medical image classification, segmentation, artifact and noise reduction, and data augmentation (1). However, GANs have been heavily concentrated in clinical research in improving image quality or pathology detection. This project proposes to utilize GANs to synthesize radiology images feeding normal and pathology X-ray images for training purposes. Radiology images are central to train radiologists and reviewing many images will provide the experience to properly detect anomalies and diagnose diseases. Still, medical data has been inaccessible due to patient health information protection law. Synthetic images will increase the collection and diversity of pathology images without breaking any patient confidentiality. 
Dataset Description
A collection of 5,856 chest X-ray images will be used for the proposed project. The chest X-ray images collected by Kermany et al. and cohorts were retrospectively selected of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center. From the total of 5,856 labeled images included 1583 normal, 2780 bacterial pneumonia, and 1493 viral pneumonia (2).
Project Plan
Technologies: GANs models using PyTorch and Pandas for data processing
Workflow: A data pipeline will be set up for the training data to input into GANs. The pipeline should split the data into training efficiently, test and validation data as well as double cross-validate the model by using nested validation. Following the output GANs artificial X-ray images with sufficient fidelity and variety as measured by Fréchet Inception Distance (FID) and Kernel Inception Distance (KID) and input the images into the application (3). For demonstration purposes, a game-like application will be created to correctly identify the normal, bacterial pneumonia, viral pneumonia, or a synthetic chest X-ray image being displayed. Lastly, an attempt to implement an ingestion engine to process new future data with the goal to retrain, evolve and improve out GANs model, by potentially utilizing a computer vision library, such as, OpenCV to convert arbitrary images into standardized matrix.
 
Work Division and Timeline
Timeline
Function
10/03-10/17
Data processing (Jae, Dauren, Andrew), pipeline architecture (Christopher)
10/20-10/23
Progress report (All)
10/17-11/10
Training (Andrew), validation (Jae, Dauren) and hyperparameter tuning (Christopher). 
11/10-11/25
Application development (Jae, Dauren), ingestion engine, iterative retraining (Christopher, Andrew)
11/25-12/06
Final Report (All)

References
Wolterink JM, Mukhopadhyay A, Leiner T, Vogl TJ, Bucher AM, Išgum I. Generative Adversarial Networks: A Primer for Radiologists. Radiographics. 2021 May-Jun;41(3):840-857. doi: 10.1148/rg.2021200151. Epub 2021 Apr 23. PMID: 33891522.
Kermany DS, Goldbaum M, Cai W, Valentim CCS, Liang H, Baxter SL, McKeown A, Yang G, Wu X, Yan F, Dong J, Prasadha MK, Pei J, Ting MYL, Zhu J, Li C, Hewett S, Dong J, Ziyar I, Shi A, Zhang R, Zheng L, Hou R, Shi W, Fu X, Duan Y, Huu VAN, Wen C, Zhang ED, Zhang CL, Li O, Wang X, Singer MA, Sun X, Xu J, Tafreshi A, Lewis MA, Xia H, Zhang K. Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning. Cell. 2018 Feb 22;172(5):1122-1131.e9. doi: 10.1016/j.cell.2018.02.010. PMID: 29474911.
Carrasco, S. and Majchrowska, S., 2022. On the evaluation of Generative Adversarial Networks. Medium. Available at: <https://medium.com/towards-data-science/on-the-evaluation-of-generative-adversarial-networks-b056ddcdfd3a> [Accessed 5 October 2022]
