import csv #this reads the file 
import pickle #saves the traininf data to a disk
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

CSV_PATH = "chord_data.csv"
MODEL_PATH = "chord_model.pkl"#where the trained model goes 
def normalize(row):
    wrist_x, wrist_y, wrist_z = row[0], row[1], row[2]
    out = []
    for i in range(0, len(row), 3):
        out.extend([
            row[i] - wrist_x,
            row[i + 1] - wrist_y,
            row[i + 2] - wrist_z,
        ])
    return out

def load_data ():
    x = [] #number 63
    y = []

    with open(CSV_PATH) as f:
        for row in csv.reader(f):
            x.append(normalize([float(n) for n in row[:-1]]))
            y.append(row[-1])
    return x,y

if __name__ == "__main__":
    X, y = load_data()
    print(f"Loaded {len(X)} samples")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_PATH}")
