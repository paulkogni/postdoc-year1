# General information
- switch edu-id recovery code: 2420 2287 6426 4041

# 01.10.2025
## General 
- group meeting information
    - Data manager: Sergio
    - have group github for publications
    - finances: there is an excel sheet in confluence 
    - for bigger things like travels: separate reimbursment tool
    - group meeting structure
        - one hour, weekly, Wednesday at 10
        - my meeting with Ece: Wednesday at 1, every other week

- meeting Ece
    - first little project: calprotein
    - other project: MAEs for ultrasound in frequency domain
    - bigger project idea: multi-modal learning for pediatrics


- general info calprotectin
    - calprotectin as new biomarker
        - calprotectin = protein from white blood cells; in poop; says how much inflammation is in the colon
        - usually taken biomarkers: 
            - Interleukin-6 (IL6): inflammation marker, comes from macrophages (is setting up acute phase, activates T and B immune cells)
            - C-reactive protein (CRP): blood protein, comes from liver during inflammation (during acute phase)

    - approaches
        - ML with vs. without cal (i.e. only IL6 and CRP) 
            - remove one subject with missing IL1 
            - select only the first time measures for markers due to incompleteness
            - put only biomarkers into a dataframe 
            - make label dataset as diagnosis infection
            - create training, testing and validation splits from them
        - take features of mum etc. into account
    
    - general notes on the dataset: 
        - no missing values for cal1
        - 1 missing value for IL1
        - no missing value for CRP

## TODOs 
- [x] check onboarding from Sergio
- [x] activate account DBE


# 03.10.2025
## Work 
- todat 
    - [x] train models 
    - [x] account scicore (maybe re-check with Anna's documentary)



## Next steps
- [x] check out data from Ece
- [x] check out lecture
    - https://docs.google.com/document/d/164_yrXwbHt-Ek4yFR-g1iKvQkpN2bRDQHG5IWGP--eM/edit?pli=1&tab=t.0



# 05.10.2025
## Work 
- notes on classification
    - labels: diagnosis sepsis
    - class imbalance: ca. 31.4% diagnosis 
    - split for train/test/val: 0.8/0.1/0.1
    - data was scaled (standard scaling)
    - model: logistic regression (compared a few, this is most simple and all equally performing)
    - scores without calprotectin (only crp and IL6)
        - AUC: 0.7982
    - scores only calprotectin
        - AUC: 0.7273
    - scores all together: 
        - AUC: 0.8291
        - most predictive: IL6 > CRP > Cal

    - looked into more potential predictive features: fever_sub_partu, b_streptococcus, breath_aid
        - AUC: 0.7418
        - breath_aid more predictive than cal_value (but not sure about causal relation)

## Next steps
- [x] prepare some slides
- [x] ask Ece about scicore 
- [x] read BiomedIT training


# 07.10.2025
## Work
- meeting 
- fighting with scicore 
- neonates project

## Next steps
- [x] read into masked autoencoders 
- [x] make project for regensburg clinicians


# 08.10.2025
## Work 
- read into transformers and MAEs


- forming projects: 
    - [x] read into hot topics from neurips
    - [x] try to see trends 
        - UQ, medical imaging etc.
- project ideas
    1. Fairness of uncertainties between adults and children in CT organ segmentation
        - maybe even more like "unfair uncertainties in ML"
    2. Global ranking-based evaluation of medical models
    3. Training models from pairwise-ranked feedback (metric-free)
        - Kaggle Diabetic Retinopathy / EyePACS (DR detection)



## Next steps


# 09.10.2025
## Work
- reading into MAEs for vision
- meeting radio oncology with Daniela THorwarth
- neurips topic analysis
    - look into 
        - [ ] https://torch-uncertainty.github.io/
        - [ ] https://arxiv.org/pdf/2502.06067 (Lipschitz)
        - [ ] https://arxiv.org/pdf/2506.18283 (UQ for distribution shifts)
        - [ ] https://arxiv.org/abs/2507.06645 (UQ in error consistency)
        - [ ] https://neurips.cc/virtual/2025/poster/119528 (error propagation; not public yet)
        - [ ] https://neurips.cc/virtual/2025/poster/119522 (multi-domain segmentation for medical images; not public yet)
        - [ ] https://hidivelab.org/publications/lange-2025-dqvis/ interactive biomedical data visualization dataset
        - [ ] https://arxiv.org/abs/2505.18636 new way of UQ for large language models (with sidekick models)
        - [ ] https://arxiv.org/pdf/2506.19083 decisions under uncertainty

- Potential project ideas
    - Project 1: Fair uncertainties for children
    - Project 2: Ranking-based learning (with comparisons)
    - Project 3: Spotting (predictive performance for) children as distribution shift using uncertainty
    - Project 4: adult-children sidekick predictions 
    - Project 5: Decisions for children under uncertainty

- What I need to find out to formulate specific projects still
    - which domains are most often used for children?
    - what is the machine learning challenge between children and adults?
    - what is the current state of the art and what is being used in practice?
    - really what is the difference between children and adults? 

## Next steps



# 10.10.2025
## Work
- Important conference dates for 2026
    - MICCAI: February 2026 (Abu Dhabi)
    - MIDL: 01.12.2025 (paper registration) / 05.12.2025 (paper submission) (Taipei)
    - NeurIPS: probably May 2026 
    - ICML: probably End of January (Seoul, Korea)
    - ECCV: 6 March 2026 (Malmoe)
    - CVPR: 06/12. November 2025 (Denver)

- Idea for Sergio
    - 

## Next steps



# 13.10.2025
## Work
- check out dataset from Ece 
    - 
- clean up my computer 
    - 

- challenges for ML in pediatric settings
    - limited data
        - solutions to overcome: fine tuning, transfer learning
    - biased models (age-related)
        - when trained on adults -> ML can perform poorly on different children populations 
        - children's anatomy changes rapidly 
            - models in general need to see more data I guess 
        - possible solutions
            - pre-trained foundational models (other problem: quite big)
            - age-aware models
    - lack of explainability
        - no transparency -> important for even more sensitive outcomes
    
    - my: economic perspective (even more costs / impact for future)
        - the more we miss, the more expensive it is later on for healthcare system
        - potential ideas: would ML have a positive cost/benefit effect and if no, how can we improve it? 


## Next steps
- [x] project ideas




# 15.10.2025
## Work 
- neonates project
    - implementing EOS calculator in python

- specific project collection


- defense making

- grouop meeting 
    - read entry on how to supervise from WIKI
    - Think about workshop ideas
    - @Paul: organize research updates
    - Lab social next wednesday

- Scientific talk Simon
    - [x] look up what CLS is 
    - [x] look into MAEs 



- TODOs today
    - [x] meeting slides Neonates
    - [x] meeting slides MSc project

## Next steps
- [x] neonates implement other 



# 16.10.2025
## Work 
- meeting Sabrina 
- meering MSc student Hareeswara
- cleaning up neonates project 
- collecting project ideas
- making some more slides for my defense 

## Next steps



# 17.10.2025
## Work 
- read paper on uncertainty for distribution shifts

- neonates project

- download data

### Paper: Yuli / Blei: Quantifying uncertainty in the presence of distribution shifts
- key idea: learn adaptive prior that is dependent on new, unseen input

- to look up
    - [x] amortized variational inference
    - [x] check papers on age bias from related work

- related work
    - https://arxiv.org/pdf/2510.10947

### My project idea
- General question: provide good uncertainties for adults and children in dataset
- approach: treat them as covariate shifts (like in the paper)
- also make OOD detection for either children or subgroups of children etc. 
- compare calibration between this approach and maybe my own one
- in general leads to more trustworthy uncertainties and predictions
- use this method to adjust phiseg such that it captures ood distribution
- 

- ML task: 
    - segmentation 
- potential datasets
    - 

- steps to do in this project
    1. replicate the paper
    2. adjust our method (phiseg) for this
    3. evaluate on segmentations for adults and children (and it's uncertainty)

- download datasets (echonet adults and pediatrics)
    - for echonet pediatric: https://aimistanforddatasets01.blob.core.windows.net/echonetpediatric?sv=2019-02-02&sr=c&sig=Foschl55%2FyC87Qtc%2BfootulPXGxzqXKVMOG2mArLNno%3D&st=2025-10-17T12%3A51%3A12Z&se=2025-11-16T12%3A56%3A12Z&sp=rl
- other dataset: AMOS and pediatric CT-seg


## Next steps



# 20.10.2025
## Work 
- read into OOD detection (maybe relevant for subgroups such as children)\

- EchoNet
    - goal: automatic estimation of cardiac function (i.e. lvef)
    - contents: videos, EF information, segmentations


## Next steps




# 21.10.2025
## Work 
- downloading datasets

- echonet exploration

### text for website
Paul is a Postdoctoral Researcher in Prof. Ece Özkan Elsen's AICH group. His research focuses on quantifying and propagating uncertainty in machine learning models along the entire diagnostic pipeline. His work aims to guide clinical decisions and ultimately improve the trustworthiness and transparency of AI applications in pediatric medicine. He completed his PhD in Machine Learning as part of the International Max Planck Research School for Intelligent Systems (IMPRS-IS) at Christian Baumgartner's Machine Learning in Medical Image Analysis Group at the University of Tübingen and the University of Lucerne.

## Next steps



- datasets to download
    - [x] amos
    - [x] pediatric CT SEG
    - [x] echonet
        -  https://echonet.github.io/dynamic/
        - https://echonet.github.io/pediatric/




# 23.10.2025
## Work

### Appeal for paper mail 
Of course. It's best to separate this into two parts:

1.  **The Email Body:** This will serve as your cover letter for the appeal. It should be concise and professional, summarizing the key issues.
2.  **The Attached Response Document:** This will be the plain text version of your detailed, point-by-point rebuttal. You should save this as a separate file (e.g., a `.txt` or `.pdf`) and attach it to your email.

Here is the formatted text for both.

---

### Part 1: The Email Body (Your Cover Letter)

Copy and paste this text into your email client.

**Subject:** Appeal of Decision for Manuscript ID: MEDIA-D-25-0214

**To:** [Email of the Associate Editor or Editor-in-Chief]

Dear Editor in Chief, Associate Editor, and Managing Editor,

On behalf of all co-authors, we are writing to appeal the rejection of our manuscript. We believe it was based on a limited and, in one case, critically flawed assessment of our work. Upon careful review of the two reports, we find that only one provides substantive feedback. The second review, however, contains several demonstrably false claims and appears to be a generic critique that does not engage with the specific contributions or details of our manuscript. It raises points that are directly contradicted by the text and by the state of the art in our field. We maintain that our work presents a significant and novel contribution to the field, well-aligned with MedIA’s scope and standards. We respectfully suggest that for a manuscript to be fairly judged against the high standards of MedIA, it must first be subject to a review process of according quality. Therefore, we kindly request that the manuscript be reconsidered and sent for a new round of review by experts who can provide a thorough and accurate evaluation of its contributions.

Below, you can find our appeal as text. Additionally, we attached the appeal as a PDF document along with the decision letter from the 23rd of September. 


Sincerely,

Paul Fischer
---

23rd October, 2025

Subject: Appeal for Manuscript MEDIA-D-25-02145: ``CUTE-MRI: Conformalized Uncertainty-based framework for Time-adaptivE
MRI''


Dear Prof. Duncan, dear Associate Editor,


We thank you for your time and efforts handling our submitted manuscript. We are writing to appeal the decision to reject our manuscript "CUTE-MRI: Conformalized Uncertainty-based framework for Time-adaptivE MRI" (MEDIA-D-25-0214). 

We believe that the provided reviews fall far below the high quality standards of Medical Image Analysis. It appears the reviewers have only given the paper a cursory reading making numerous claims that are incorrect, not backed up by facts, and that are directly contradicted by information that is already in our manuscript. Examples include the claim by Reviewer 1 (R1.3) that we did not analyze patient specific adaptation (which we do in Fig. 3 of the manuscript), and all claims by Reviewer 2, such as the unbacked claim that uncertainty-guided MR acquisition stopping is decades old (R2.1 and R2.2). 

Most of the remaining comments seem to stem from misunderstandings of our method, likely due to an inattentive reading. However, these could easily be clarified through minor textual revisions.

We have addressed all concerns raised by the reviewers point-by-point with detailed explanations and evidence why the raised points are unjustified or even incorrect.

Based on the serious deficiencies in the review process, we kindly request that you grant our manuscript a de novo review by a new set of qualified experts who can provide a fair and accurate assessment of its scientific merits. 

We thank you for your time and consideration, and look forward to your response and the opportunity to improve our manuscript.



Sincerely,

Paul Fischer

On behalf of all co-authors: Paul Fischer, Prof. Dr. Thomas Küstner, Prof. Dr. Christian Baumgartner


---
### **Reviewer 1**
---

**Reviewer Point 1.1:**
*Reviewer's Comment: "This paper proposes a dynamic, uncertainty-aware acquisition framework... The idea is innovative, but method is too simple, and lot of content is meaningless to the method, experiments are insufficient. In my opinion, the paper does not meet the requirements of this journal."*

**Our Reply:**
We thank the reviewer for judging our work to be innovative. However, we disagree with the assessment that the method is 'too simple'. We propose the first method to automatically terminate MR acquisitions based on a real-time uncertainty computation. As detailed in the manuscript, the choice of models was deliberate, prioritizing essential real-world requirements such as sampling speed for real-time application and the quality of uncertainty estimates (Section 2.1). We believe the paper clearly outlines the necessary components for our method (e.g., calibrated uncertainties, rapid reconstruction, clinically relevant metrics; Section 1) and demonstrates how our proposed framework successfully integrates and meets them.

---
**Reviewer Point 1.2:**
*Reviewer's Comment: "In section 2.1, the content is the reconstruction and segmentation model used in this paper, so this section is not related to the method and meaningful."*

**Our Reply:**
We believe that a clear definition and explanation of the underlying reconstruction and segmentation models are crucial for understanding the integrated CUTE-MRI framework. This section provides necessary context on the building blocks of our pipeline and is essential for the reproducibility of our work.

---
**Reviewer Point 1.3:**
*Reviewer's Comment: "The proposed method is to create a patient-specific adaptive stopping rule for k-space acquisition, so, I think it is a good for motivation to analysis the difference of accelerated rate between different patient."*

**Our Reply:**
This patient-specific adaptation is a core motivation of our work and **has been indeed analyzed**. Figure 3 in our manuscript explicitly shows the distribution of stopping acceleration rates across all subjects for both datasets, comparing the calibrated and uncalibrated approaches. This figure directly demonstrates the patient-specific nature of our method and the variability in optimal scan times.

---
**Reviewer Point 1.4:**
*Reviewer's Comment: "Whether to train a reconstruction model for each acceleration rate."*

**Our Reply:**
Based on the findings from the original PHiRec paper, training a single model to handle multiple acceleration rates can lead to degraded reconstruction performance. To ensure the highest quality at each step, we opted to train a separate model for each acceleration rate. This is a design choice and our CUTE-MRI framework is agnostic to it. The fundamental principle of our adaptive acquisition approach remains unchanged. However, we would be happy to include an ablation study in the paper where we compare a single model for all accelerations versus acceleration-specific models.

---
**Reviewer Point 1.5:**
*Reviewer's Comment: "According to Fig.1., the basic pipeline is to iteratively sample k-space... what are the advantages compared to a multi-task model (same as reconstruction + segmentation)..."*

**Our Reply:**
Our modular, pipeline-based approach was intentionally designed to mirror clinical decision-making processes, where a reconstruction is often assessed before subsequent analysis. This design allows us to explicitly model and calibrate the uncertainty arising from the reconstruction process itself. Furthermore, the modularity ensures that the high-quality reconstructions can be repurposed for other downstream tasks beyond segmentation. An end-to-end model would lose this flexibility and interpretability, which we believe are critical for clinical translation. We will clarify this in our manuscript.

---
**Reviewer Point 1.6:**
*Reviewer's Comment: "Section 2.3 is the core of this article, but it is not detailed enough, such as how to make conformal calibration. There is only basic conformal prediction content."*

**Our Reply:**
Section 2.3 provides a comprehensive explanation of how conformal prediction is integrated into our framework. We detail the algorithm and its specific application within our pipeline, providing sufficient information for implementation. To further aid reproducibility, all hyperparameters and specific settings used in our experiments are explicitly listed in Section 3.4 (Experimental Details). While we believe that the combined information in these sections is sufficient for others to replicate our method, we can address this point in a revision by adding more details as requested by the reviewer. In addition, we have released our code at https://github.com/paulkogni/CUTE-MRI, which will allow others to exactly replicate our work.

---
**Reviewer Point 1.7:**
*Reviewer's Comment: "What is the goal of Sec.4.1 and Fig.2.? It is a basic cognition that the more measurements you sample, the better the image quality. Thus, Sec.4.1 is meaningless."*

**Our Reply:**
The purpose of Sections 4.1 and Figure 2 was to validate the performance of the individual modules of our pipeline (reconstruction and segmentation). While it is intuitive that more measurements yield better quality, it is crucial to empirically demonstrate that our chosen models perform as expected before evaluating the entire adaptive framework. This foundational analysis confirms the integrity of each component, which is essential for trusting the results of the full pipeline. We will clarify this point in a potential revision.

---
**Reviewer Point 1.8:**
*Reviewer's Comment: "From Fig.3., it can be seen that the scan stops at high acceleration factor when there is no conformal calibration. In my opinion, the goal of conformal calibration is to more precisely terminate the scan, so it should need less scan duration..."*

**Our Reply:**
**The reviewer has misunderstood the purpose of calibration** and the interpretation of Figure 3. The goal of conformal prediction is not to produce *tighter* confidence intervals (and thus shorter scans), but to produce statistically *correct* or *valid* intervals. Our results show that without calibration, the model is overconfident, leading to erroneously stopping too early. Conformal calibration corrects this overconfidence. This is not a flaw but a crucial finding of our study: uncalibrated uncertainty can be dangerously misleading. This point is further elaborated in our discussion in Section 5.2.

---
**Reviewer Point 1.9:**
*Reviewer's Comment: "How many slices does every dataset have in every dataset."*

**Our Reply:**
This information is provided in detail in Section 3.2.2 for our internal dataset. For the public SKM-TEA dataset, this information is available in the original publication, to which we refer. We will include this information directly in our paper in a potential revision.

---
**Reviewer Point 1.10:**
*Reviewer's Comment: "According to the experiment, the final goal is similar to salient object recognition, so it would be nice to have some metrics related to salient object recognition."*

**Our Reply:**
While there may be conceptual similarities, our tasks are grounded in clinical medical image analysis. We have therefore reported metrics that are **standard and widely accepted for evaluating MRI reconstruction (e.g., SSIM, PSNR) and segmentation (e.g., Dice score)**, as well as clinically relevant downstream measurements (e.g., ejection fraction).

---
**Reviewer Point 1.11:**
*Reviewer's Comment: "According to the limitations, there is no data consistency. This is a simple operation—why wasn't it considered in the original design?"*

**Our Reply:**
We agree that incorporating a data consistency step can be beneficial. However, for this study, we chose to adhere to the original, validated PHiRec framework. Introducing data consistency adds complexity to the probabilistic formulation and would represent a deviation from the established baseline model whose uncertainty properties we aimed to leverage. This is a design choice and does not detract from our main contribution: the first uncertainty-guided dynamic MRI acquisition approach.

---
### **Reviewer 2**
---

**Concern 2.1:**
*Reviewer's Comment: "The central contributions of the manuscript... are... not conceptually new... Using these estimates to define a threshold for early stopping is a straightforward and decades-old strategy in adaptive acquisition."*

**Our Reply:**
**We strongly disagree with the reviewer's assessment of our work's novelty.** The reviewer's claims are factually incorrect and demonstrate a significant misunderstanding of the literature. The claim that uncertainty-based adaptive acquisition for MRI is a 'decades-old strategy' is incorrect, and **is not backed up by any evidence by the reviewer**. To our knowledge, no prior work has proposed or implemented such a framework for dynamic, patient-specific MRI acquisition driven by downstream task uncertainty.

---
**Concern 2.2:**
*Reviewer's Comment: "The models selected... are outdated... Furthermore, the experimental setup lacks critical comparisons. No alternative adaptive acquisition strategies or uncertainty-driven baselines are included..."*

**Our Reply:**
The reviewer ignores explicit justifications provided in the manuscript and makes false claims regarding baselines. In Section 2.1, we provided explicit justifications for selecting the PHiRec model, prioritizing its rapid sampling speed and its well-characterized uncertainty quantification capabilities. Furthermore, the claim that our work lacks comparison to 'alternative adaptive acquisition strategies or uncertainty-driven baselines' is misleading because, as stated previously, **such baselines for our specific application do not exist** in the literature. Our work aims to establish the first such baseline.

---
**Concern 2.3:**
*Reviewer's Comment: "Key components... are not individually analyzed. The absence of ablation studies... there is no robustness evaluation across different datasets..."*

**Our Reply:**
**The reviewer's claim that we performed no ablation or robustness evaluation is incorrect**, and is directly contradicted by the evidence in our manuscript.
- **Ablation of Conformalization:** We explicitly analyzed the contribution of conformal calibration by comparing results with and without it (Section 4.2, Figure 3).
- **Robustness across Datasets:** Our evaluation was performed on two distinct datasets (one public, one internal) with different characteristics.
- **Patient-Specific Adaptability:** Figures 3, 4, and 5 are dedicated to analyzing the patient-specific adaptability and variability in stopping times.
The review dismisses a substantial portion of our results section, which is dedicated to exactly these types of analyses.

---
**Concern 2.4:**
*Reviewer's Comment: "The manuscript... does not convincingly demonstrate added value... There is no formal complexity analysis, no runtime benchmarking..."*

**Our Reply:**
**These points raised by Reviewer 2 are also incorrect.** We explicitly report runtime benchmarks in Section 4.2, stating the time per pipeline iteration and the hardware used. The chosen downstream tasks (cartilage volume and ejection fraction computation) are of high diagnostic relevance, as motivated in Sections 3.4.1 and 3.4.2. Our framework's value is in achieving a user-defined, clinically acceptable precision for these metrics in the shortest possible time for each individual patient.


#### other potential journals to send it to
- https://www.sciencedirect.com/journal/computerized-medical-imaging-and-graphics
- https://onlinelibrary.wiley.com/journal/15222594
- https://www.sciencedirect.com/journal/computers-in-biology-and-medicine
- https://www.embs.org/tbme/
- https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=42


## Next steps



# 24.10.2025
## Work 
- finish reviews
- make slides for defense
- make slides for research update
- look into neonates project

## Next steps
- [x] write Xin-Yi for contract change


# 27.10.2025
## Work 
- read into self-supervision and attention

- slides for research update

### Project idea: growing neural networks (self-supervision)
- general idea: 
    - create small network (transformer, with attention head)
    - train it for a few epochs, let architecture grow (first only a few neurons, then bigger; have a fixed rate)
    - can even think about establishing a final architecture or something
    - see how it behaves when learning representations

- toy data for experiments
    - ask chatti for this 

- real-world data 
    - maybe cifar 10 or something
    - check what is commonly used for self-supervised pre-training
    - also check how this works with clinical data

- topics to read into
    - [ ] self-supervised learning 
    - [ ] evolutionary algorithms
    - [ ] transformers 
    - [ ] attention
    - [ ] growing networks in pytorch 

- related work
    - https://ieeexplore.ieee.org/document/592393
    - https://arxiv.org/html/2406.04607v2
    - https://arxiv.org/abs/2201.05125

## Next steps
- [x] look into self-supervised learning
- [ ] make presentation defense

- stuff to look up
    - [x] self-attention
    - [x] transformer for segmentation


- look into (neurips)
    - [ ] https://torch-uncertainty.github.io/
    - [ ] https://arxiv.org/pdf/2502.06067 (Lipschitz)
    - [x] https://arxiv.org/pdf/2506.18283 (UQ for distribution shifts)
    - [ ] https://arxiv.org/abs/2507.06645 (UQ in error consistency)
    - [ ] https://neurips.cc/virtual/2025/poster/119528 (error propagation; not public yet)
    - [ ] https://neurips.cc/virtual/2025/poster/119522 (multi-domain segmentation for medical images; not public yet)
    - [ ] https://hidivelab.org/publications/lange-2025-dqvis/ interactive biomedical data visualization dataset
    - [ ] https://arxiv.org/abs/2505.18636 new way of UQ for large language models (with sidekick models)
    - [ ] https://arxiv.org/pdf/2506.19083 decisions under uncertainty

- [ ] Project idea: hierarchical MAEs