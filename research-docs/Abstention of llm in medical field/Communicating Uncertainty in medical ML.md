### *To be noted : This is a **Perspective/review-style paper**, not a new experimental ML method*
## *Summary :*
### This paper discusses that for medical ML, it is important for the model to quantify and communicate the uncertainty of a certain prediction. It distinguishes between a model's **prediction** and its **uncertainty about that prediction**. Models implementing such approaches allow more informed decision making as well as abstain from certain samples.
### The core of this work is an overview on the **existing approaches** to **quantifying uncertainty** and abstention for ML and how these help in making models safe and reliable in healthcare settings. 
### Types of uncertainty :
- ### Uncertainty inherent in the data. (Aleatoric)
- ### Uncertainty arising from limitations of the model/data knowledge. (Epistemic)

### **Note**: How do we establish that there *is* uncertainty that needs to be addressed?
### Measurement noise, Limited data, Parameter uncertainty,  Model uncertainty, Dataset shift, Out-of-distribution patients, 

### **Uncertainty type 1:**  
### The model's predicted probability itself indicates confidence.

### **Uncertainty type 2:**  
### The predicted probability is itself unstable/unreliable.


### *Approaches discussed :*
| Approach                                  | Basic idea                                                                       | What uncertainty it gives you                    |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Prediction intervals**                  | Give a range rather than a point prediction                                      | Predictive uncertainty                           |
| **Conformal prediction / conformal sets** | Construct prediction sets/intervals using calibration data                       | Whether a prediction should be accepted/rejected |
| **MC Dropout**                            | Run the neural network multiple times with dropout active                        | Variation across stochastic predictions          |
| **Deep ensembles**                        | Train multiple models and compare their predictions                              | Model disagreement / epistemic uncertainty       |
| **Bayesian methods**                      | Treat model parameters as distributions rather than fixed values                 | Posterior/predictive uncertainty                 |
| **Gaussian Processes**                    | Bayesian nonparametric model with uncertainty naturally built in                 | Predictive uncertainty                           |
| **Post-hoc calibration**                  | Transform model confidence so probabilities better correspond to actual accuracy | Reliability of confidence                        |
| **Abstention / selective prediction**     | Refuse to predict when uncertainty is too high                                   | Operational "I don't know"                       |

### *Main Point :* **Prediction correctness and prediction confidence/uncertainty are not the same thing, and a useful ML system should be able to distinguish reliable from unreliable predictions and abstain when appropriate.**
