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
- [ ] include WBC in analysis as biomarker
- [ ] maybe look at infants from only > 34 weeks (this is roughly the cutoff for when immune system works differently)
- [ ] include SHAP for XGBoost in analysis for explainability 