# MAGF
## my notes
- research gap
    - early alzheimer's disease detection without neuroimaging 
- their approach
    - multi-modal classification based on four modalities
- how they do it 
    - have novel parameter-free attention mechanism 

1. Please provide a brief summary and your overall opinion of the paper
- the paper introduces a way of classifying alzheimer's using a multi-modal approach
- the question of multi-modal encoding is always about how to fuse the predictions together 
- the authors propose to perform weight fusion in a deterministic way, calling it Multi-view attention-guided fusion
- the weights of the weight fusion is based on the inverse coefficient of variation
- their method outperforms other classical frameworks in terms of classification metrics and yields an additional "interpretable" layer which is the weights of the fusion
- overall, I think the paper is okay and the comparisons are fine but it feels a bit unready and the term "attention" is being kind of mis-used as this is just a heuristic way of combining the encodings and not necessarily comparable to the originally proposed attention mechanism 

2. What are the main strengths of the paper?
- rich baseline selection
- approach clear
- results seem good 

3. What are the main weaknesses of the paper?
- in abstract, the main motivation is early AD detection but not used later on; instead, just pure AD classification is used
- no citations within the text!
- mentioned work in the references section seems a bit old; no concurrent work cited
- unclear goal: is it improving transparency or performance? 
- some variables not formally defined ($m_i$, $\beta_i$) 
- notion of attention kind of misleading 
- text and experiment tables are a bit misleading (reported different models in the table than in the text + not defined abbreviations)
- don't mention parameter search for baseline models
- Figure 1 seems incorrect. According to the description in the text, the steps after the CV attention module are consecutive and therefore there should be arrows along the computation steps
- what is $\beta_i$ supposed to be in Figure 1? 
- Cohen's d reported but not interpreted 
- Figure 2 takes up a lot of space (with lots of unused white space) which could have been used for further clarificaation
- no labels in Figure 2 for colors in the plot 
- gist of the paper: many have approached opening the "black box" through interpretability but why shoud one use your method instead? -> missing in your paper 


4. Please provide detailed and constructive feedback for the authors to improve their manuscript
- clarification on mathematical notation
- improve figures according to points mentioned above
- create coherence between text, tables and figures
- improve motivation for your approach compared to others
- more detailed related work and clarification of which research gap your approach is closing compared to other related work


5. How would you rate the clarity of this submission?
- ok-ish


6. How would you rate the novelty of this submission?
- not so much 

7. What is your general recommendation for this submission?
- reject

8. Please justify your recommendation. What were the major factors that led you to this overall score for the submission?
- the sum of the points mentioned above make the paper weak and vulnerable to a lot of critisism. Additionally, the results should be taken with a grain of salt since it is not mentioned whether there was a hyperparameter search or even the implementation details of the compared models with hyperparamneters. There are no actual references within the text (or I couldn't find them) but there are a few papers listed in the References section. Not sure how that worked but this shows unmet scientific standards. 

9. Please rate your level of expertise on the discussed topic
- 3/5


10. Related work to consider
- https://link.springer.com/article/10.1007/s12559-021-09946-2
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12069014/
- https://www.sciencedirect.com/science/article/pii/S1386505625003107
- https://www.nature.com/articles/s41598-024-51985-w









# Multi-modal AI for patient monitoring in cancer care
## my notes
- research gap
    - patient monitoring in between doctor visits for cancer treatment
    - overarching goal: more proactive care
- their approach
    - use remotely accessible data (multi-modal) to predict critical events 
- how they do it specifically
    - use a token-based transformer for multi-modal data to forecast clinical events

1. Please provide a brief summary and your overall opinion of the paper
- goal of the work is to use multi-modal remote patient data to predict critical events for patients undergoing cancer therapy
- the authors use a transformer-based architecture TODO

2. What are the main strengths of the paper?


3. What are the main weaknesses of the paper?


4. Please provide detailed and constructive feedback for the authors to improve their manuscript


5. How would you rate the clarity of this submission?


6. How would you rate the novelty of this submission?


7. What is your general recommendation for this submission?


8. Please justify your recommendation. What were the major factors that led you to this overall score for the submission?


9. Please rate your level of expertise on the discussed topic


10. Please provide any further comment to the organisation committee that was not captured by the previous questions


11. Related work to consider

