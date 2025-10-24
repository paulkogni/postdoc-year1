# Broad Structure
## Topic-introductory part
- (optional) Introduction of myself
- the need and challenges of ML in medicine
- Introduction: origins of uncertainty in medicine
- The special case: diagnostic pipelines (away from isolated tasks)
- Uncertainty for clinical decisions (and the necessary ingredients: uncertainty estimation, propagationm, calibration, decision)

## My contributions to these problems
- The contribution of this thesis: Estimation + Propagation, Leveraging (decision), Calibration
- Takeaway of this thesis: ML (and UQ) is not just an application in medicine, it requires 

## Main Methods: Papers 
- Paper 1: Uncertainty estimation and propagation for accelerated MRI
- Paper 2: UQ for clinical decision
- Paper 3: Used uncertainties should be useful
- Paper 4: Bringing all together: propagation, calibration, action

## Conclusion + future work
- Why pipelines
- Model performance and uncertainty
- Interacting uncertainties
- personal: future work (ML for pediatrics) and thanks

# Potential Backup slides
- Differences Conformal and RCPS (and why we chose which when)
- math conformal 
- math rcps
- MRI Physics
- why "old" methods
- Radiation therapy physics / background
- fundus stuff background
- mathematical formulation of PHiRec


# Introduction slides

## The need + challenges for ML in medicine
- what I want to say with this slide
    - why ML in medicine is relevant and what challenges we have when using it

- content
    - more need for computational tools (aging population, shortage of specialists)
    - more and more ML tools are fda-approved. In order to actually use them: trust
    - high-risk domain and need to address issues of trustworthiness, reliability, interpretability etc.
- figures
    - FDA approvals 


## Origins of uncertainty in medicine
- what I want to say with this slide
    - medical diagnosis is by its nature full of uncertainty

- content
    - uncertainty in acquisition (motion during scan)
    - varying/ambiguous human physiology (fuzzy tumor boundaries)
    - uncertainty from different levels of expertise 
    - lot's of research has been done on that already
- figures
    - something that visualizes origins of uncertainty


## The special case: diagnostic pipelines (away from isolated tasks)
- what I want to say with this slide
    - how uncertainty affects the whole diagnostic pipeline and not only isolated tasks

- content
    - example of an actual pipeline (MICCAI 23)
    - show how uncertainties are embedded within pipeline 
    - affect eventually decisions

- figures
    - dinggeng screenshot


## Uncertainty for clinical decisions
- what I want to say with this slide
    - how we have to treat uncertainty such that it can be used to form decisions in diagnostic pipelines

- content
    - need to know how to pass on uncertainty, ensure that it is meaningful and eventually know what to do with it

- figures
    - not sure yet, maybe combine this slide with previous one


## Contribution of this thesis
- what I want to say with this slide
    - establish the research gap and how I plan to fill it 

- content
    - my contributions are propagation + importance of evaluation
    - how to effectively laverage propagated uncertainty
    - calibrate with statistical guarantees  
    - how to bring everything together to make clinical decisions

- figures
    - overview of maybe propagation, calibration and decision


# Paper contribution slides 




# Conclusion and outlook slides