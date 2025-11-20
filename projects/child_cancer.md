# 18.11.2025
## General
- challenges of pediatric cancer 
    - data scarcity + childchood cancer rare in general
    - imaging evolves fast -> little data from one domain/modality
    - not enough data to train DL models 
    - small market size (market size drives innovation)

- possible stages of where ML in the whole process of cancer treatment could be used (or already is used) for pediatrics
    - from this paper: Applications of Artificial Intelligence for Pediatric Cancer Imaging (sergios gaditis)
    - image acquisition
    - processing
    - reconstruction
    - segmentation
    - diagnosis 
    - staging 
    - treatment response monitoring

- the gap: basically no work on treatment planning for childhood cancer



- Current applications of ML in radiation therapy for pediatrics
    - transfer learning from adults

- Brachytherapy in pediatric cancer treatment
    - often used for rhabdomyosarcoma, soft tissue sarcoma
    - from paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC5095266/): "For sites relevant for brachytherapy, the anatomy and topography in tumours of children are comparable to those in adults."
    - but: dimensions are much smaller -> important for relationship between target volume and radiosensetive critical organs around volume
    - main cancer types for treatment
        - head and neck regions
        - gynaecological, urological
        - anus-rectum 
        - extremeties
        - eye orbit
        - all "reachable"
    - Brachytherapy as second treatment round (normal radiation therapy was first round)

- ML in brachytherapy
    - multiple stages possible to use: 
        - imaging, preplanning, treatment planning. applicator reconstruction, quality assurance, outcome prediction, real-time monitoring
        - imaging
            - registration (gyn cancer) 
            - segmentation (gyn -> mri, prostate -> CT, pet, trus, mri)
        - preplanning 
            - so far only done on gyn and prostate
            - gyn: 
                - selecting appropriate applicators (intra-cavity or interstitial)
                - can train ML models to select the optimal needle based on anatomy
            - in prostate
                - seed distribution and dose distribution; number of seeds
        - treatment planning 
            - prostate
                - dose calculation (like we did in the other project)
                - predict catheter locations
            - gyn
                - similar to prostate
        - Applicator reconstruction
    


- Potential projects
    - multi-institutional data sharing 
    - privacy for children with rare cancer types 
    - live cancer segmentation in children with ultrasound imaging to guide needle/catheter insertion


## TODOs 
- [ ] make presentation for Daniela