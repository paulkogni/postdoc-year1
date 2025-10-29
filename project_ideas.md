# Dynamically growing transformers
- general idea: 
    - create small network (transformer, with attention head)
    - train it for a few epochs, let architecture grow (first only a few neurons, then bigger; have a fixed rate)
    - can even think about establishing a final architecture or something
    - see how it behaves when learning representations

- toy data for experiments
    - ask chatti for this 

- real-world data 
    - maybe cifar 10 or something
    - check what is commonly used for self-supervised pre-training
    - also check how this works with clinical data

- topics to read into
    - [ ] self-supervised learning 
    - [ ] evolutionary algorithms
    - [ ] transformers 
    - [ ] attention
    - [ ] growing networks in pytorch 

- related work
    - https://ieeexplore.ieee.org/document/592393
    - https://arxiv.org/html/2406.04607v2
    - https://arxiv.org/abs/2201.05125