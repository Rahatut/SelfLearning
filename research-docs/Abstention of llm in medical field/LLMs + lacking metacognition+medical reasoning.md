## *Summary :*  
### In the medical field it is important for reasoning on diagnosis and knowledge application to have maximum accuracy and carefulness because of the sensitiveness and the weight of possible consequences. Usage of LLMs in this field can vastly improve the healthcare system, however an important caveat to note is - whether they are reliable enough to handle this matter carefully.
### What the researchers in the paper did is : built a benchmark -"MetaMedQA" consisting of multiple choice QnA with : 
- ### Correct answers
- ### No answers - option none of the above to be picked (Missing ans)
- ### Fictional and incomplete scenario - None of the above ans (Unknown)
### Then they ran 12 models and evaluated how they perform on this benchmark. 

### Their findings : Models *confidently* answer even when there is *no correct answer* in the option or *sufficient enough* scenario for it to be able to answer. 
### Measuring criteria : Unknown recall, Missing ans recall, confidence score (high-5, low-3)
### Observations : Only GPT-3.5, GPT-4o and Qwen2-72B meaningfully varied their confidence.
### The issue is that they can give incorrect answers **without appropriately signaling that they might be wrong**.

## *How connects to our work :*
### this paper acts as **A behavioral precedent for measuring whether an LLM recognizes that it should not answer**