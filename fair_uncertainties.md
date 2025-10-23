# General 
- General question: provide good uncertainties for adults and children in dataset
- approach: treat them as covariate shifts (like in the paper)
- also make OOD detection for either children or subgroups of children etc. 
- compare calibration between this approach and maybe my own one
- in general leads to more trustworthy uncertainties and predictions
- use this method to adjust phiseg such that it captures ood distribution
- 

- story
    - ML methods have arrived in medicine + perform already very well 
    - not much application of ML methods for pediatrics because of poor performance 
    - bad performance due to
        - less data available 
        - more restrictions on data
        - more physiological variety 
    - moreover, ML models do not only need to be better, also should indicate whether they make good predictions (improves )

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


# New method


# Methods to compare against


# Experiments
- metrics to evaluate


# Datasets
- [x] AMOS 
- [ ] oediatric CT seg
- [x] echonet
- [x] echonet pediatrics