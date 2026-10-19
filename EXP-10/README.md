\# EXP-10: MLflow Machine Learning Lifecycle



\## Aim

To track machine learning experiments, log parameters and metrics, register a trained model, and serve the model for predictions using MLflow.



\## Tools Used

\- Python 3.12

\- MLflow

\- scikit-learn

\- Iris dataset



\## Implementation

1\. Installed MLflow and the required Python libraries in a virtual environment.

2\. Created `train.py` to train Random Forest classifiers using the Iris dataset.

3\. Executed three experiments using 50, 100, and 150 estimators.

4\. Logged model parameters, accuracy metrics, and model artifacts in MLflow.

5\. Compared experiment runs in the MLflow UI.

6\. Registered the selected model as `EXP10-Iris-RandomForest`, version 1.

7\. Served the registered model on port 1234.

8\. Sent a prediction request to the model endpoint.



\## Access URLs

\- MLflow Tracking UI: `http://127.0.0.1:5000`

\- Model serving endpoint: `http://127.0.0.1:1234/invocations`



\## Experiment Results



| Number of estimators | Accuracy |

|---:|---:|

| 50 | 0.90 |

| 100 | 0.90 |

| 150 | 0.90 |



The registered model uses 150 estimators and a random state of 42.



\## Prediction Test

A prediction request was sent to the model using an Iris sample. The endpoint returned:



```json

{"predictions": \[0]}

```



The predicted class `0` corresponds to Iris setosa.



\## Files

\- `train.py`: Training script that logs experiments and model artifacts.

\- `Submission/`: Reserved for the final submission document and supporting evidence.



\## Result

MLflow experiment tracking, parameter and metric logging, model registration, and model serving were demonstrated successfully.

\# EXP-10: MLflow Machine Learning Lifecycle



\## Aim

To track machine learning experiments, log parameters and metrics, register a trained model, and serve the model for predictions using MLflow.



\## Tools Used

\- Python 3.12

\- MLflow

\- scikit-learn

\- Iris dataset



\## Implementation

1\. Installed MLflow and the required Python libraries in a virtual environment.

2\. Created `train.py` to train Random Forest classifiers using the Iris dataset.

3\. Executed three experiments using 50, 100, and 150 estimators.

4\. Logged model parameters, accuracy metrics, and model artifacts in MLflow.

5\. Compared experiment runs in the MLflow UI.

6\. Registered the selected model as `EXP10-Iris-RandomForest`, version 1.

7\. Served the registered model on port 1234.

8\. Sent a prediction request to the model endpoint.



\## Access URLs

\- MLflow Tracking UI: `http://127.0.0.1:5000`

\- Model serving endpoint: `http://127.0.0.1:1234/invocations`



\## Experiment Results



| Number of estimators | Accuracy |

|---:|---:|

| 50 | 0.90 |

| 100 | 0.90 |

| 150 | 0.90 |



The registered model uses 150 estimators and a random state of 42.



\## Prediction Test

A prediction request was sent to the model using an Iris sample. The endpoint returned:



```json

{"predictions": \[0]}

```



The predicted class `0` corresponds to Iris setosa.



\## Files

\- `train.py`: Training script that logs experiments and model artifacts.

\- `Submission/`: Reserved for the final submission document and supporting evidence.



\## Result

MLflow experiment tracking, parameter and metric logging, model registration, and model serving were demonstrated successfully.



