# OOD segmentation
## my notes
- research gap
    -  OOD generalization of DL models
- their approach
    - lightweight DNN framework to restore degraded segmentations by refining them through geometric priors
- how they do it 
    - have an encoder-decoder-based structure that learns distributions of anatomically possible shapes 
    - framework takes degraded segmentation from model used on OOD data and produces "restored" segmentation

1. Please provide a brief summary and your overall opinion of the paper
- paper extends a conference paper by extending mathematical formulation, extended evaluation on new domains, sensitivity analysis of hyperparameters, additional baselines and extended their related work / introduction
- have encoder-decoder structure for learning anatomy distributions from ID data
- encoder projects input onto K-dimensional space representing principal modes 
- decoder for creating a possible correction based on learned distribution
- opinion
    - experiments very extensive
    - show consistent positive performance of their framework
    - introduction is an unstructured mix between background, related work and contributions
    - related work in general ok but it confuses me that there are only methods listed for segmentation and not handling OOD 
    - often at the end of a subsection in the related work part there are claims without proof/reference and relations to OOD are missing (details below)
    - the experiments should include one additional setting: when evaluating on OOD, there should be also an ID performance reported as this is what the paper is aiming for: taking corrupted segmentations that are not clinically useful and turning them into something clinically useful (as good as ID performance)
        - I am aware that - provided with the current results - there will be some significant gaps, raising the question whether the method itself is a benefit for clinical applications in OOD settings
        - it could still have a value as it often improves the ID performance already but in that case the story needs to be very different and the evaluations as well 
        - either way, it you have to justify why this method with the given results is clinically relevant
    - could it be useful to use the refining for several steps instead of only one? would this further improve segmentation? I.e. feed the output of the VarDeepPCA model again for several steps
    - the role of uncertainty here is unclear and its expressiveness is not evaluated (e.g. how do the models that provide UQ correlate to the error and does your method improve that correlation/calibration?)
    - missing related work to actual OOD segmentation
        
    - overall, the paper needs major revision but I still think it could be published 


2. What are the main strengths of the paper?
- very thorough evaluation with many baselines 

3. What are the main weaknesses of the paper?
- detailed feedback for introduction
    - in second paragraph segmentation only as binary introduced
    - in line 49/50: talk about computationally expensive sampling of VAEs without backup
    - in line 56 already talking about your contribution but in an unstructured way
    - in the whole section there is already a mix happening between your work and related work (e.g. paragraph line 100)
    - I am not fully convinced by the contributions "mathematical formulation" and "more extensive related work section" 

- feedback related work 
    - why the explicit change of U-Net to UNet when it already has a name?
    - claim in line 227-230 without any backup/reference
    - line 347 without backup
    - in section 2.3, 2.4, 2.5, 2.6 no relation to OOD 
    - in 2.7 no reference for lines 438-440
    - in 2.8 no relation to OOD and at the end no references again

- methods feedback
    - in line 498 it should be assesed what makes images OOD when they are from different hospitals or different protocols
        - i.e. different hospital doesn't automatically mean that the images are drawn from different distributions and if so, you should explain why
    - 3.3 could be improved by stating in the behinning where you are heading to with the derivation or why you are doing this (i.e. goal is to find a closed form for the distribution); this would improve reading/understanding
    - at the beginning of 3.4 it is unclear to me why segmentation errors and discretization artifacts are supposed to be filtered out with this approach

- Results and discussion feedback
    - in 4.1, line 751-753 I don't understand the rationale behind the clustering as well as the associated parameters
    - in 4.1, is the data augmentation being applied only to VarDeepPCA or to all the baseline methods?

- feedback references
    - please check your references again, for example reference S. Bernhard "Nonlinear component analysis..." is actually B. Schölkopf, i.e. the first and last name is switched




4. Please provide detailed and constructive feedback for the authors to improve their manuscript
- major changes in introduction according to points mentioned above
- aditional justification on clinical relevance for OOD settings with additional evaluation of ID performance on OOD datasets 
- maybe include iterative refining steps and compare


5. How would you rate the clarity of this submission?
- not so clear


6. How would you rate the novelty of this submission?
- okay

7. What is your general recommendation for this submission?
- reject with possibility for revision







## Introduction and Related Work

- The Introduction (Section 1) is unstructured. It mixes background information, related work, and contributions indiscriminately (e.g., the paragraph around line 100).
- The second paragraph introduces segmentation strictly as a binary problem, which may be too limiting or needs clarification.
- Unsubstantiated Claims:
    - Lines 49-50: The paper discusses the computationally expensive sampling of VAEs without providing evidence or references.
    - Lines 227-230, Line 347, and Lines 438-440: Claims are made at the end of these subsections without proof or citations.
    - Missing OOD Context: Sections 2.3, 2.4, 2.5, 2.6, and 2.8 list methods but fail to explain their relation to OOD challenges.
- The authors explicitly change "U-Net" to "UNet" which is unclear to me why as it already has its convention
- I am not fully convinced that "mathematical formulation" and "more extensive related work" stand alone as significant research contributions.


## Methodology

- The paper should assess what specifically makes images OOD when coming from different hospitals or protocols. A different hospital does not automatically imply a distribution shift; this needs to be explained and justified.
- Derivation (Section 3.3): It is unclear at the beginning of this section where the derivation is heading. Stating the goal upfront (e.g., "to find a closed form for the distribution") would improve readability.
- Section 3.4: At the beginning of this section, it is unclear why this specific approach is expected to filter out segmentation errors and discretization artifacts.
Results and Discussion:

- Section 4.1, Lines 751-753: I do not understand the rationale behind the clustering approach or the associated parameters chosen.
- Augmentation, Section 4.1: Is data augmentation applied only to the VarDeepPCA model or to all baseline methods? This impacts the fairness of the comparison.
- The paper lacks a comparison to ID performance (see detailed feedback below).
- The role of uncertainty is mentioned but its expressiveness is not evaluated. For instance, do models that provide Uncertainty Quantification show a correlation between uncertainty and error, and does this method improve that calibration?


## References

- There are errors in the bibliography. For example, the reference listed as "S. Bernhard" ("Nonlinear component analysis...") is actually authored by B. Schölkopf (first and last names are switched).