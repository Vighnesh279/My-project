
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

mlflow.set_experiment("EXP-10-Iris-Classification")

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

for n_estimators in [50, 100, 150]:
    with mlflow.start_run() as run:
        model = RandomForestClassifier(
            n_estimators=n_estimators, random_state=42
        )
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("random_state", 42)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(
  		model,
    		name="model",
    		skops_trusted_types=["sklearn.tree._tree.Tree"]
	)

        print("Run ID:", run.info.run_id)
        print("Number of estimators:", n_estimators)
        print("Accuracy:", accuracy)
        print("-" * 40)
