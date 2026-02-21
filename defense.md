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




# Introduction slides (5.5 Minutes)
## Slide 1: Title
- say title 

## Slide 2: Motivation (1.5m)
- slide goal: why we need uncertainty ML applications for medicine
- what to say
    - increasing FDA approvals
    - medicine high-risk application
    - doctors handle uncertainty implicitly (important!)
    - for ML applications we need to do it explicitly
    - if want to use ML in medicine, we need to use uncertainty somehow
- figures
    - FDA figure
    - different segmentations

## Slide 3: Challenges + diagnostic pipelines (1.5)
- slide goal: unclear how to integrate uncertainties in clinical workflow + how it integrates in diagnostic pipeline
- what to say
    - what notion of uncertainty is useful for a task? 
    - what are the properties of uncertainty that need to be fulfilled? 
    - clinical workflows are not isolated tasks -> how do we model uncertainty in a stream of dependent tasks? 
    - need to know: how to pass uncertainty to downstream task, how to ensure expressiveness / reliability  and eventually how to make use of it
- figures
    - uncertaity maps for segm
    - MICCAI pipeline

## Slide 4: Diagnostic pipelines (1.5)
- maybe merge with the one from above


## Slide 5: Contributions (1)
- slide goal: point out contributions to problems mentioned above
- what to say
    - how to propagate -> paper 1
    - how to leverage -> paper 2
    - how to calibrate -> paper 3
    - how to combine full workflow -> paper 4
- figures
    - none



# Project 1: Acc. MRI (5 Mins)
## Slide 6: Motivation (1 mins)
- slide goal: acc. MRI inherently uncertain and usually not isolated -> want to do something with these images (e.g. compute segemntations, make clinical decisions; like quantifying tumor size )
- what to say
    - acc. MRI = make scans faster through making incomplete measurements (in frequency space)
    - leads to artifacts in image space
    - operator: inverse FT 
    - this process inherently uncertain (infinitely many images possible) -> some are more likely than the others
    - more important: uncertainty not isolated but propagates to subsequent tasks
    - question to answer: how can we pass uncertainty on efficiently and what does it mean for it to be good? 
- figures
    - undersampling process
    - image with artifacts + maybe multiple reconstructions with uncertainty

## Slide 7: Method (2 mins)
- slide goal: two contributions: 1. a new model that produces good reconstructions and best uncertainties + 2. show how this uncertainty affects a downstream task (segmentation)
- what to say
    - don't only want to get any uncertainty but we want to get *good* uncertainty (i.e. uncertainty should correlate with error)
    - for this: introduce recon model based on hier. cVAEs 
    - we model local and global structure of artifacts (from missingness in high and low freq measurements)
    - model residuals and not reconstruction directly
    - for uncertainty propagation: used monte-carlo sampling, i.e. sample reconstructions 
- figures
    - phirec figure 
    - sampling figure 

## Slide 8: Results + Impact (2 mins) 
- slide goal: can reconstruct well, uncertainty best, can propagate usefully
- what to say
    - to ensure recon quality + segm quality: we evaluated ssim/psnr and dice 
    - compared different settings to asses ID and OOD model and uncertainty performance 
    - takeaway: our model has similar recon performance but way better 
    - have now a mdoel + way of propagating uncertainty in medical pipelines
- figures
    - quantitiative results 
    - qualitative results 



# Project 2: Glaucoma (5 Minutes)
## Slide 9: Motivation (1)
- slide goal: what do we do with uncertainty once we have it? 
- what to say
    - many tasks in medicine are uncertain and doctors handle this uncertainty implicitly in their decisions
    - example uncertain task: glaucoma diagnosis based on fundus images 
    - glaucoma: disease related to optical nerve -> main cause for blindness
    - look at cup to disk ratio; if certain ratio -> test for glaucoma
    - in previous paper we have seen that there are ways to model uncertainty and even propagate it
    - but what do we do with it in the end? How do we make decisions based on that? 
- figures
    - CDR, Fundus, Uncertainty of fundus 

## Slide 10: Method (2)
- slide goal: a method for improving diagnosis -> making better decisions with uncertainty
- what to say
    - 
- figures
    - 

## Slide 11: Results + Impact (2)
- slide goal: 
- what to say
    - 
- figures
    - 



# Project 3: UQ in Radiation Therapy (5 Mins)
## Slide 12: Motivation / Context / Failure (1)
- slide goal: 
- what to say
    - 
- figures
    - 

## Slide 13: Method (Subgroup fix) (2)
- slide goal: 
- what to say
    - 
- figures
    - 

## Slide 14: Results + Impact (2)
- slide goal: 
- what to say
    - 
- figures
    - 


# Project 4: Uncertainty-guided MRI acquisition (5 Mins)
## Slide 15: Motivation (1)
- slide goal: 
- what to say
    - 
- figures
    - 

## Slide 16: Method (2)
- slide goal: 
- what to say
    - 
- figures
    - 

## Slide 17: Results + Impact (2)
- slide goal: 
- what to say
    - 
- figures
    - 


# Conclusion (4 Mins)
## Slide 18: Summary / Impact (2)
- slide goal: 
- what to say
    - 
- figures
    - 

## Slide 19: Future Work / Limitations (2)
- slide goal: 
- what to say
    - 
- figures
    - 

## Slide 20: Thanks
- slide goal: 
- what to say
    - 
- figures
    - 




















# General questions and things to look up
- [ ] current SOTA UQ in ML + in medicine
- [ ] realted propagation methods + how they work 
    - feiner
    - raghav
    - the old methods (fitting gaussians etc.)
- [ ] diffusion models 
- [ ] 2d vs 3d predictions







# remaining TODOs slides

- S2
    - not so nice up to now
    - maybe motivation of segmentation
    - ask chatti
- S3
    - align spacing for decision items
- S4
    - re-position texts
    - make math formulas
- S5 
    - make difference between brains bigger
    - math formulas 
    - last arrow spacing 
- s6
    - re-position text
- s7 
    - animations
- s8
    - animations
    - include segmentation example
- s9
    - adjust figure sizes
    - text position
- s10
    - write core idea
    - maybe include methods used
- s11
    - make higher-res screenshot of results table
    - include main takeaway 
- s12
    - re-position figures and text
- s13
    - write info on rcps (motiv + how it works)
    - math formulas
- s14
    - adjust animations
    - make figures a bit bigger
    
- s15
    - little text: how our approach differs from original one
- s16
    - text under images
    - animations
- s17 
    - math formula
    - knee volume images
- s18
    - text on methods used
- s19
    - re-position texts
    - highlight key takeaways
- s20
    - write key takeaways
    - maybe split figure into two
- s21
    - image of group