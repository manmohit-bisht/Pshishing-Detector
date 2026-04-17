import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv("phishing_dataset.csv")

print("Dataset_Shape: ",df.shape)

X = df.iloc[:, :-1] #X represents features
Y = df.iloc[:,-1] #Represents label i.e phishing or legit

print(f"Features shape : {X.shape}")
print(f"Labels shape   : {Y.shape}")
print(f"Feature names  : {X.columns.tolist()[:7]} ___ (only first 7)")

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print(f"\nTraining on : {len(X_train)} URLs")
print(f"\nTesting on  : {len(X_test)} URLs")

model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs = -1)
model.fit(X_train, Y_train)

print("Training Completed")

Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,Y_pred)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

#Saving to disk

joblib.dump(model,"Phishing_model.pkl")
print("Saved as Phishing_model.pkl")


feature_importance = pd.Series(model.feature_importances_,index=X.columns).sort_values(ascending=False)

print("10 most important features:\n",feature_importance.head(10))