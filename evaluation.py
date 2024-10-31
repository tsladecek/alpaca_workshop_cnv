import numpy as np
from numpy.typing import NDArray
import pandas as pd


def read_labels() -> NDArray[np.int8]:
    with open("data/test_labels.tsv") as f:
        return np.array([int(i.strip()) for i in f.readlines()], dtype=np.int8)

def read_predictions() -> dict[str, NDArray[np.int8]]:
    data = pd.read_excel("data/alpaca_cnv_predictions.ods", engine="odf", sheet_name=None, header=None)

    preds = {}
    for k, v in data.items():
        preds[k] = np.array(v.iloc[:, 0].values, dtype=np.int8)

    return preds


if __name__ == "__main__":
    labels = read_labels()
    preds = read_predictions()

    for group, predictions in preds.items():

        if len(labels) != len(predictions):
            print(f"Invalid submission by group: {group}. Number of predictions does not match number of labels")
            continue

        acc = 100 * sum(labels == predictions) / len(labels)
        print(f"{group}:\t{round(acc, 2)}%")
