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


## TODOs
- [ ] make classification with stuff except biomarkers
- [ ] make classification with stuff + biomarkers (with and without calprotectin)
- [ ] make API or replicate Neonatal Early-Onset Sepsis Calculator
    - https://neonatalsepsiscalculator.kaiserpermanente.org/
    - resources
        - https://www.jointcommissionjournal.com/action/showPdf?pii=S1553-7250%2816%2942030-1
        - https://watermark02.silverchair.com/zpe011110e1155.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAzswggM3BgkqhkiG9w0BBwagggMoMIIDJAIBADCCAx0GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMBsy7A8J31Me2FyJ5AgEQgIIC7ku1jyyPhXO5HEMjRbxTxsTobF4fPwz6s-rtk38N5ZQURfBvVCSDZ71lrYoTjreO2oX-jz4dcmhR2d99WFhKyRax0i15fY74fzV4nHoGolON3ZhKCcidK_8U8bLaybsnoswAbz0kX3qyM-mJnhaQqIVPwbP4t2gBGUGFMM_UJc3rUma096zpD4YhR-SHPptyfruWSmbECRCzNrQ-Oj03gWEuRZMxXXk6qpTVJ5T8dbmJ9F61OzTCVEhzamD5FCaGEBt6SSiQm7lH2Cdb1AqXqcl9MvnICr31gIxYX9EptGIY33gdyTM2e6Ce1oPkq8FK4iRhcpz7SgWp1ii7iS_s0J0_4j6jiAdTd-voyivIJlQlC2rnH0yGHEAFsOTnzfDOnLqoEVThin3D5pXUfxNb-cT3HfCAKRIc9ix74IJkf3RGcQEb1_WVz-2nDO8BolCLQrfxvsD4Nzwzc2jPdGEoDXDmiKnIQ7hm00ge67KwrHPrnTmz3IISg0W15YBxuvItqazxfMiVVpK7T9udtAqT-Tynv_V8aeeKQ_jblbINMCYLBbEjVc-fCxCqP7_Q0H412MiNowcjQIDbA_Ie3vv8iOhBlcr_aWSgHHVXqmYMY7kp-9B43OEbSDb_B03tDzRMOPUw38mhZ1pEtPYs-XoSKzLsig1oXf1c9J8lIFw9-UzlGO2xLTffs73IaOiyGhmfMpncEhu5RYlO-PtFvrwFLLXqtkrolLuWdKicrUGVIGLnXs53E788L9XHXTLuAP0nTY_zg2q2Hcb7hivGG0mcRCDflt1mgVecn_0rqVtt4y_iyq2GtZZ9pkPI1kTSWvH176C1-RDfvt-aScl5ojumUQsqnqzwhzQW7AZhSbPfT9HjkNAEkQXHLdKXBIDOsU7tmrZ0DGQsfB9zgYW9Fst4cqIJBoIAfoTGrj8hmvqJeCic3Jwf8FcJ17qAdyfHRzhQsT_DaJiFpAW3S5b83Uo8NZi-wedON3XX9PdL8meRug