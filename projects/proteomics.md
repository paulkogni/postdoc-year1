# 19.11.2025, Meeting Evi 
## My notes before meeting 
- general overview
    - proteomics in general: study of proteins in the human body (i.e. the proteome)
    - measures concentration in blood sample through mass spectrometry

- data structure
    - group 1: patient data and study metadata
    - group 2: demographics and medical history
    - group 3: targets (gestation diabetes)

- my questions for the meeting 
    - [ ] general goal
    - [ ] which part of the data is relevant? 
    - [ ] what do the sheets in the excel file mean? 
    - [ ] what do the colors in the file mean? 
    - [ ] is there a meta-file for the explanation of the columns? 
    - [ ] why are there multiple ID columns in one sheet? (v1, v2, ...)
    - [ ] what is pat_id_baseline...1?
    - [ ] is the protemics sheet redundant to the one in the main sheet? 
    - [ ] what are the most important columns for me to know? 


## Meeting notes
- general: 
    - topic: gestational diabetes
    - high prevalence during pregnancy: 10-16%
    - usually based on anti-insulin hormones (14th week)
    - very related to pre-diabetes: often 10-15 years after diabetes the women get type 2 diabetes
    - one big sign: too big children (weight, disproportional); normalizes after two months usually
    - these children have high risks for almost everything 
    - the study
        - want early diagnosis of gestational diabetes
        - currenly when diagnosed it's often too late already
        - the test itself (oral glucosis test) is super variable and absolutely not reliable (this is the gold standard for us though)
        - another gold standard could be the need for insulin but this is already very late and severe stage
    - the study includes patients between 2014 and 2019 (820 women)
    - only 82 of them actually have diabetes
    - what they have done already is tested a lot of predictors for gestation diabetes
    - what they have only investigated a bit is the beta cell dysfunction which is highly relevant for gestation diabetes apparently
    - what they still would like to do is a proteomics analysis which they haven't yet
    - the core idea: there isn't just **one** type of gestational diabetes; some are worse than others
    - in a different study in Vienna, they identified three different clusters for types of diabetes based on proteoms 
    - is there a way we can do something similar for us? maybe define the clusters even better? 
    - Research questions that we could attempt to answer
        - Q1: can we predict child weight from features? 
        - Q2: Can we find a proteomics clustering? 
        - Q3: Can we predict a big belly for the new-born child? 
        - Q4: Can we forecast whether a patient needs insulin? 
        - Q5: We can colour the values of the clustered stuff by tiga/tiger/tyga score 
        - Q6: Analysis of insulin-sensitivity and beta cell dysfunction


## TODOs
- [ ] look at the feature list and divide into relevant and not relevant 
- [ ] for the feature list where I think it is relevant, check all of the features whether I understand what they are and what is the values/units 
- [ ] make a plan of what I could predict and what I would use it for 
