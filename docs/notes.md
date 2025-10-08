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
- [ ] read into masked autoencoders 
- [ ] make project for regensburg clinicians
- [ ] make presentation defense