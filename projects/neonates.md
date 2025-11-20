# 07.10.2025
## Meeting 
- Core ideas for my project
    - P1: predictive tool for infection_diagnosis based on clinical features and not biomarkers
    - P2: prediction after 24 or 48 hours (still a bit unclear)


## Work 
- clinical features removal
    - features to exclude due to missingness
        - antibiotic_therapy_duration
        - result_blood_culture
        - membrane_rupture_hours
        - crp_max_prepartal
        - leukocyte_max_prepartal
        - all biomarkers > value 2
    - excluding antibiotic_therapy due to leakage
    - birth model (for now because of complexity, i.e. categorical variable)
    - capillary time
    - after cleaning the features: 324 

- TSNE experiment
    - didn't show any nice separation from features itself but maybe I need to normalize the features first
    - even after scaling no success
    - PCA didn't invent the wheel new either


## TODOs
- [x] make classification with stuff except biomarkers
    - classification with the other features is improving when considering the biomarkers as well 
    - but when only taking clinical features, the classification is not improving
- [ ] make classification with stuff + biomarkers (with and without calprotectin)
- [ ] make API or replicate Neonatal Early-Onset Sepsis Calculator
    - https://neonatalsepsiscalculator.kaiserpermanente.org/
    - resources
        - https://www.jointcommissionjournal.com/action/showPdf?pii=S1553-7250%2816%2942030-1
        - https://watermark02.silverchair.com/zpe011110e1155.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAzswggM3BgkqhkiG9w0BBwagggMoMIIDJAIBADCCAx0GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMBsy7A8J31Me2FyJ5AgEQgIIC7ku1jyyPhXO5HEMjRbxTxsTobF4fPwz6s-rtk38N5ZQURfBvVCSDZ71lrYoTjreO2oX-jz4dcmhR2d99WFhKyRax0i15fY74fzV4nHoGolON3ZhKCcidK_8U8bLaybsnoswAbz0kX3qyM-mJnhaQqIVPwbP4t2gBGUGFMM_UJc3rUma096zpD4YhR-SHPptyfruWSmbECRCzNrQ-Oj03gWEuRZMxXXk6qpTVJ5T8dbmJ9F61OzTCVEhzamD5FCaGEBt6SSiQm7lH2Cdb1AqXqcl9MvnICr31gIxYX9EptGIY33gdyTM2e6Ce1oPkq8FK4iRhcpz7SgWp1ii7iS_s0J0_4j6jiAdTd-voyivIJlQlC2rnH0yGHEAFsOTnzfDOnLqoEVThin3D5pXUfxNb-cT3HfCAKRIc9ix74IJkf3RGcQEb1_WVz-2nDO8BolCLQrfxvsD4Nzwzc2jPdGEoDXDmiKnIQ7hm00ge67KwrHPrnTmz3IISg0W15YBxuvItqazxfMiVVpK7T9udtAqT-Tynv_V8aeeKQ_jblbINMCYLBbEjVc-fCxCqP7_Q0H412MiNowcjQIDbA_Ie3vv8iOhBlcr_aWSgHHVXqmYMY7kp-9B43OEbSDb_B03tDzRMOPUw38mhZ1pEtPYs-XoSKzLsig1oXf1c9J8lIFw9-UzlGO2xLTffs73IaOiyGhmfMpncEhu5RYlO-PtFvrwFLLXqtkrolLuWdKicrUGVIGLnXs53E788L9XHXTLuAP0nTY_zg2q2Hcb7hivGG0mcRCDflt1mgVecn_0rqVtt4y_iyq2GtZZ9pkPI1kTSWvH176C1-RDfvt-aScl5ojumUQsqnqzwhzQW7AZhSbPfT9HjkNAEkQXHLdKXBIDOsU7tmrZ0DGQsfB9zgYW9Fst4cqIJBoIAfoTGrj8hmvqJeCic3Jwf8FcJ17qAdyfHRzhQsT_DaJiFpAW3S5b83Uo8NZi-wedON3XX9PdL8meRug
    - source code: see email Ece
- [x] make TSNE visualization for data

# 14.10.2025
## Work 
- implementing EOS calculator
    - variables we need 
        - gest_weeks
        - gest_days
        - membrane_rupture_hours
        - incidence_rate 
        - maternal_temp
        - abx_type
        - gbs_status
        - clinical_status
    - what we are missing
        - incidence_rate (probably known for our region)
        - maternal_temp (have only fever_sub_party)
        - abx_type (have only antibiotics_prepartal)
        - gbs_status (don't have "Unknown" as category; not sure how to treat this)
        - clinical_status (have only indicators, maybe even more fine-grained)

- What I can do
    - compare pre_risk only 
    - only thing I am missing here then: highest maternal temperature and type of antibiotics (if any)


## My topics for next meeting
- classification performance for ML approach in general 
- cannot compare EOS calculator directly with our approach because of missing / different features


# 15.10.2025
## Work 
- features selected for classification: 
    - birth_weight
    - gest_weeks + gest_days (-> made to one gest_time)
    - age_mother
    - gravidity
    - parity
    - birth_mode (one-hot encoding)
    - umbilical_cord_ph
    - capillary_time
    - o2_demand
    - breath_aid
    - heart_rate
    - respiration_rate
    - rr_systolic
    - rr_diastolic
    - base_excess
    - ph_value
    - diabetes_type_1_2
    - adiposity
    - early_membrane_rupture
    - membrane_rupture_hours (put 0 in case missing)
    - early_labor_pain
    - green_amniotic_liquor
    - b_streptococcus
    - crp_max_prepartal
    - leukocyte_max_prepartal
    - fever_sub_partu
    - antibiotics_prepartal
    - prepartal_antibiotics_count
    - biomarkers: only from time 1


- label: diagnosis_infection

# 16.10.2025
## Meeting Sabrina

### General 
- the previous dataset was not correct with the calprotectin (some values have been mixed up regarding the time point)
- there are two/three goals that we might need to do with machine learning 
    1. Infection right after birth -> yes/no? 
        - for this we mainly look at time stamps at time zero
        - look at all clinical parameters that we have and maybe also calprotectin
    2. If antibiotics were given, test after 24 or 48 hours based on clinical parameters (and calprotectin) whether we can predict even better
        - important to stop as soon as possible with treatment

    3. Detect ideal window for calprotectin to be predictive



### New TODOs until next time
- [x] include WBC in analysis as biomarker
- [x] maybe look at infants from only > 34 weeks (this is roughly the cutoff for when immune system works differently)
- [x] include SHAP for XGBoost in analysis for explainability 


# 17.10.2025
## Work
- clean new dataset 
    - the features I have selected: ['birth_weight', 'gest_weeks', 'gest_days',
       'age_mother', 'gravidity', 'parity', 'umbilical_cord_ph',
       'capillary_time', 'o2_demand', 'breath_aid', 'heart_rate',
       'respiration_rate', 'rr_systolic', 'rr_diastolic', 'base_excess', 'diagnosis_infection', 'gestation_diabetes',
       'diabetes_type_1_2', 'adiposity', 'early_membrane_rupture',
       'membrane_rupture_hours', 'early_labor_pain', 'green_amniotic_liquor',
       'b_streptococcus', 'fever_sub_partu', 'antibiotics_prepartal', 'SCP1', 'CRP1', 'IL61', 'WBC1']

- preprocessing:
    - select only relevant features 
    - impute membrane rupture hours (lots of null values)
    - drop null values
    - compute total gest time

- new amount of data I have left after cleaning: 273

- tsne visualization

- save into train, test, eval split

- new classification results (AUC)
    1. all features
        - LR: 0.7869
        - XGBoost: 0.9391
    2. Only clinical
        - LR: 0.6971
        - XGBoost: 0.7123
    3. Only biomarkers
        - LR: 0.7500
        - XGBoost: 0.8173
    4. Clinical + calprotectin
        - LR: 0.7019
        - XGBoost: 0.7147

- feature importance see notebook exp011


# 28.10.2025
## Work 
- make grid search on parameters for XGBoost

- include SHAP for XGBoost (take individual example patients)

- looked at data distributions (after filtering out)

- my questions about features
    - respiration_rate: one with 175
        - typo?
    - membrane_rupture_hours: 1848 hours (77 days), 1176
        - maybe minutes and not converted? 
    - CRP1: 
        - what's with all the 0.99980003? 
        - one is 60, normal? 
    - IL61: 
        - what's with 9.999800?
        - extremely high values, e.g. 37000?

- Subject IDs for extremely high values
    - respiration rate 180: CAL-329
    - high membrane rupture hours: 
        -   CAL-094	(1176.0)
        - 	CAL-169	(1848.0)
        - 	CAL-227	(3192.0)
        - 	CAL-317	(1008.0)
    - high IL6 values
        - CAL-112 (37000.0)
        - CAL-119 (3690.0)
        - CAL-126 (16410.0)
        - CAL-169 (25765.0)
        - CAL-176 (6520.0)


# 30.10.2025
## Meeting Sabrina 





# 04,11.2025
## Work 
- next steps to do in the project
    - [x] convert membrane rupture to binary variable 
        - < 18h normal, >= 18h problematic (it will mean early rupture)
        - already in dataset
    - [x] IL6: leave for now, if doesn't work then do cutoff; maybe do log scale but then values could be too close together
    - [x] group by dates
        - first window: 0-18h, group the values together
        - second window: 18-60h 


## New TODOs 

- [x] exclude newborns < 34 weeks 
    - they could corrupt the data analysis because their immune system works completely different 
    - biomarkers don't tell anything about infections
    - should be around 60 kids 
    - maybe we could do even two different models (one for < 34 and one for > 34 weeks) if enough data
    - in worst case we have to restrict our model to > 34 hours





# 05.11.2025
## Work 
- fit classifier for algorithm V1
    - all features
    - all features without SCP
    - all biomarkers 
    - biomarkers without scp
    - clinical with scp
    - only clinical

- fit classifier for algorithm V2
    - fit classifiers again like on top for second phase 
    - in test set, look at only the ones that received antibiotics 
    - check how many of them are incorrect by labels 
    - check how many of those we would prevent from over-treatment

## Next steps
- [x] try out to add additional binary variable early born or not 
- [x] for AUC experiment: check additionally for biomarkers with and without calprotectin
- [x] make new distinction for classification: 
    - merge datapoints within 24h together and then 24h-48h
    - this will create two new datasets and two new classifiers 
    - for merging double datapoints of biomarkers: take the first measured one 


# 20.11.2025, Meeting 
## General 
- the current results should be taken with a grain of salt since the division of the two algorithms based on time is not necessarily correct
- what we should do instead is to treat the time of the first measurement as t_0 instead of the birth

## Next steps
- [ ] compute the hours of measurement not after brith but after the first measurement (first measurement is t_0)
- [ ] visualize the features I have taken out of all the available features, probably with a Venn-diagram
- [ ] find a way of how to compare against Kaiser-permanente 