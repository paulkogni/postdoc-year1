# Paper

## Abstract


## Introduction + Related work (roughly 1.5 pages)


## Methods (roughly 2.5 pages)
- our method is an extension of the VIDS framework 
    - the extension: adapt the architecture for segmentation
- general idea of this framework: uncertainty quantification under distribution shifts
- we decided to adopt this framework because it allows us to model uncerainties that essentially come from a change in distribution (children vs. adults)
- the mathematical formulation
    - usually we don't have the property by default that for OOD data we observe high uncertainty 
    - in standard NNs, the distribution over params theta is usually treated independently of covariates x
    - this means: label y_i is independent of other pairs (x_j, y_j) given x_i and theta
    - same goes for new test points x* -> therefore no change of posterior distribution
    - the framework tackles this problem by introducing an adaptive prior for input covariates (not only parameters theta)
    - new test points are treated as independent of all other dataset pairs (x_i, y_i)


- what are individual network parts
    - have a predictive network f parameterized by theta
    - have pre-trained embedding network g
    - prediction network h that estimates parameters for variational distribution


- how the training procedure works 
    - test covariates are not available 
    - for this, VIDS uses synthetic environments / inverse bootstrapping
    - want to create environments that are different to standard training distribution (simulates covariate shift)
    - drawing enough subsamples makes it very likely that we approximate true unknown distribution

- how uncertainty estimation works
    - by getting parameters from inference network for variational distribution, we can draw samples for theta 
    - use these samples then to make multiple forward passes -> gives us uncertainty estimates on the output

- what we adapted in order to make it compatible with segmentations
    - we took a U-Net for segmentation as a basis
    - the encoder is basically all of the U-Net except the last layer 
    - the decoder is the last layer as a 1x1 convolution layer 
    - we do this because 


## Experiments & Results (roughly 4 pages)


## Discussion and Conclusion (roughly 0.5 pages)






# Story
- ML can help in medical settings to reduce workload
- must be reliable though and ideally free of bias such that downstream decisions are fair for all subgroups i.e. all get equal treatment
- one critical subgroup: children
- underperformance for children when using ML is a problem
    - children are not small adults
    - high variation in anatomy
    - when using ML models on children, usually bad performance
- it is not always possible to mitigate underperformance 
    - usually requires more information on data side
- but: we would ideally like to know WHEN we are underperforming 
- one possible way of indicating underperformance: quantifying uncertainty
- But: uncertainties must be expressive and useful in order to help making good/safe/trustworthy decisions based on these
- problems with common UQ methods 
    - problem of calibration: usually no guarantee that high uncertainties correspond to high error probability and vice versa (usually plain uncertainties over-confident)
    - there are frequentist methods to turn notions of uncertainty into ones that come with statistical guarantees (e.g. conformal prediction)
    - problem with these methods: when dataset is so heterogeneous (such as children) these methods can be misleading with the guarantees 
        - e.g. when there is underrepresented group: guarantees can still hold globally but unc. can be completely uncalibrated for underrepresented group (such as children etc.)
        - also these methods only make statements across a dataset (statistical statements) and not necessarily per individuum
    - even a subgroup-calibration is not always possible because in some cases (such as children) it is very hard to define those

- our contributions
    - we show the problematics with uncertainties in the setting of performance on children and how these would lead to unfair downstream decisions
    - we further show that plain frequentist methods don't fully get rid of this problem
    - to tackle this problem, we introduce an extension of VIDS for segmentation
        - tricky to use amortized variational inference because for segmentation models we usually have a huge amount of parameters
        - we deal with this problem by only applying VI on a prediction head 
        - to model uncertainties for different distributions, the model uses inverse bootstrapping
    - this model allows us to model uncertainties for different subgroups and OOD subgroups by artificially creating OOD subsets 
    - we treat children as it's own distribution which allows us to explicitly model the uncertainty inherent to the subgroups without explicitly knowing the subgroups



# Figure plan 
## F1: Methods
- show several input images from training distribution; are devided into smaller batches which visualizes inverse bootstrapping
- show input also as OOD (children image)
- show how they are being jointly embedded
- show how the parameter estimation based on this joint embedding changes when inputs are further away from each other in embedding space
- leads to higher uncertainty in prediction

## F2: Under-performance


## F3: Uncertainties (performance)


## F4: Uncertainties (Qualitative)


## F5: (Downstream decisions)


# Experiment plan
## Exp 1: Under-performance for children and age-groups
- three different models for UQ 
- domain: 
    - segmentations (error: dice)
    - ejection fraction (error: squared error?)
- experimental settings
    1. Trained on children/adults/both
    2. Performance within the different age groups

- message with this figure
    - bad transfer of knowledge from adults to kids
    - dice might be not suited to asses/compare performance since big structures
    - high performance variations between age groups


## Exp 2: Uncertainty Analysis 
- domain
    - EF
- metrics
    - coverage
    - interval size
    - correlation error and interval size 

- experimental settings
    - three models 
    - coverage with vs. without calibration 
    - correlation for interval sizes and 

- message
    - the coverage by default is not there
    - after calibration it is but interval size and correlation show that uncertainty is more than coverage
    - our model has coverage but also best uncertainty interval sizes + correlation


## Exp 3: Downstream Decision Analysis
- make artificial labelling of cardiac dysfunction (< 50%)
- if dysfunction is inside the unc. interval -> refer
- check auc, sens, spec
- see which model in that case would be better
- only prediction vs. unc.-informed (and then all different models)





# Code plan
