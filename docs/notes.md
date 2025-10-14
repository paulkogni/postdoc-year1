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
    - ICLR: (Rio de Janeiro) -> already past
    - ECCV: 6 March 2026 (Malmoe)
    - CVPR: 06/12. November (Denver)

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




# 14.10.2025
## Work 
- neonates project
    - implementing EOS calculator in python

## Next steps
- [ ] neonates implement other 
- [ ] make presentation defense
- stuff to look up
    - [ ] self-attention
    - [ ] transformer for segmentation

- datasets to download
    - [ ] https://physionet.org/content/vindr-pcxr/1.0.0/ (pediatric chest xray)
    - [ ] https://physionet.org/content/vindr-cxr/1.0.0/ (normal chest xray)
    - [ ] echonet
        -  https://echonet.github.io/dynamic/
        - https://echonet.github.io/pediatric/

- look into (neurips)
    - [ ] https://torch-uncertainty.github.io/
    - [ ] https://arxiv.org/pdf/2502.06067 (Lipschitz)
    - [ ] https://arxiv.org/pdf/2506.18283 (UQ for distribution shifts)
    - [ ] https://arxiv.org/abs/2507.06645 (UQ in error consistency)
    - [ ] https://neurips.cc/virtual/2025/poster/119528 (error propagation; not public yet)
    - [ ] https://neurips.cc/virtual/2025/poster/119522 (multi-domain segmentation for medical images; not public yet)
    - [ ] https://hidivelab.org/publications/lange-2025-dqvis/ interactive biomedical data visualization dataset
    - [ ] https://arxiv.org/abs/2505.18636 new way of UQ for large language models (with sidekick models)
    - [ ] https://arxiv.org/pdf/2506.19083 decisions under uncertainty