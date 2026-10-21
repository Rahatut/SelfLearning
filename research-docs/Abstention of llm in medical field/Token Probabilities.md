## *Summary :*
### When an LLM answers a medical question incorrectly, can we detect that it is likely to be wrong by looking at its token probabilities? This is what this paper tried finding out. 
### The authors *compared* - the *probability of the chosen token*  (**response token probability**) and the *confidence* expressed by the LLM when asked how confident it is.
### The core goal was to quantify the trustability of answer, since LLMs tend to be overconfident in their answers.

### *Findings :* The models stated confidence score is way higher than actual token probability. In case of looking at the tokens probability - they show a better picture : The authors observed that ***token probabilities were significantly more likely to exceed 80% for correct answers than incorrect ones across all tested models.***
### Stats Analysis : AUROC was used to see how well does confidence discriminate between Correct and incorrect ans?
### *the superiority of token probability was statistically significant*

### *How connects to our work :* Main point - **token probabilities provide a substantially stronger correctness signal.** Directs towards - Looking into the internal mechanisms of how LLMs generate answers using prediction of next token and probability of chosen token can give more insights on how uncertainty appears and how it can be measured

### Quantization may preserve answer accuracy reasonably well while degrading the model's ability to distinguish when its answers are unreliable.