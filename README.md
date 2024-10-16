Speech to text - Machine learning model

1. **Data Preparation**:
   - The notebook includes steps to load audio files and extract features (such as MFCCs).
   - It splits the dataset into training and testing sets using `train_test_split` from the `sklearn` library.

2. **Model Selection and Training**:
   - Different models are being trained and tested on the audio feature set. There's code to check label distribution and examine individual audio files.
   - The notebook also includes evaluations of the model's performance, printing scores on both the training and testing datasets.

3. **Prediction and Evaluation**:
   - The notebook demonstrates how to make predictions using the trained model and compares predicted values against the actual labels.
   - Model accuracy is computed, and results are compared between training and test sets.

4. **Feature Inspection**:
   - Some cells display data like `labels`, and the model’s predictions on a subset of the data.

It is aimed at processing speech features and building a classification or regression model for a speech recognition task.
