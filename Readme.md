# AutoJudge — Predicting Programming Problem Difficulty

Author: Pranshu Sharma  
GitHub: [harryx32](https://github.com/harryx32)  
Date: 2026-01-08

---

## Project Overview

AutoJudge is an end-to-end Machine Learning project that automatically predicts the difficulty level of programming problems using only their textual descriptions. The system performs two tasks:

- Classification Task — Predicts the difficulty class of a problem:
  - Easy
  - Medium
  - Hard

- Regression Task — Predicts a numerical difficulty score representing the complexity of the problem.

The project is inspired by competitive programming platforms such as Codeforces and CodeChef, where difficulty is typically assigned manually. AutoJudge aims to automate this process using Natural Language Processing (NLP) and classical machine learning.

---

## Dataset

The dataset consists of programming problems (collected from public sources) with difficulty labels and numerical scores. The dataset is provided in JSONL (JSON Lines) format. No manual labeling was performed — the provided dataset was used directly.

Each data sample contains the following fields:
- `title`
- `description`
- `input_description`
- `output_description`
- `problem_class` (Easy / Medium / Hard)
- `problem_score` (numerical difficulty score)

Note: For reproducibility, keep the dataset in the `data/` folder and point the training scripts to the correct JSONL file.

---

## Approach and Models

### Data Preprocessing
- Loaded JSONL data into a Pandas DataFrame.
- Handled missing values.
- Combined textual fields into a single text feature by concatenating:
  - Title
  - Problem description
  - Input description
  - Output description

### Feature Extraction
- TF-IDF vectorization of the combined text.
- Considered unigrams and bigrams to capture short phrase signals.
- Resulting TF-IDF vectors were used as input features for both classification and regression models.

### Models
- Classification (Difficulty Class)
  - Linear Support Vector Machine (SVM)
  - Output: Easy / Medium / Hard
- Regression (Difficulty Score)
  - Random Forest Regressor
  - Output: Continuous numerical difficulty score

Both models were trained independently using the same TF-IDF features.

---

## Evaluation Metrics and Results

We evaluate both tasks with standard metrics:

- Classification: Accuracy
- Regression: Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)

Reported results from the final evaluation:

- Accuracy: **0.479951397326853** (≈ 0.4799)
- Confusion Matrix (rows = actual class, columns = predicted class):

  [[ 47  59  47]
   [ 39 255  95]
   [ 28 160  93]]

  (Class order: 0 = Easy, 1 = Medium, 2 = Hard)

- Regression:
  - MAE: **1.8944292223572294**
  - RMSE: **2.230126312384673**

Interpretation:
- The classification accuracy (~48%) reflects the subjective and overlapping nature of difficulty labels across problems.
- The confusion matrix shows the model often predicts Medium for many instances, which may be due to class imbalance or feature ambiguity.
- Regression errors (MAE ≈ 1.89, RMSE ≈ 2.23) indicate the model predicts difficulty scores with reasonable average error but can still produce larger deviations for harder-to-estimate problems.

---

## Web Interface

A simple and interactive Streamlit web application is provided to demo the models.

Features:
- Input fields for:
  - Problem Title
  - Problem Description
  - Input Description
  - Output Description
- A "Predict Difficulty" button
- Displays:
  - Predicted difficulty class (Easy / Medium / Hard)
  - Predicted numerical difficulty score (from the regression model)

The web interface calls the same preprocessing pipeline as training: it vectorizes the combined text using the saved TF-IDF vectorizer and runs both the SVM classifier and Random Forest regressor to return results in real-time.

---

## Steps to Run Locally

1. Clone the repository
```bash
git clone https://github.com/harryx32/AutoJudge-Predicting-Programming-Problem-Difficulty.git
cd AutoJudge-Predicting-Programming-Problem-Difficulty
```

2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Prepare the dataset
- Place your JSONL dataset in `data/` (e.g., `data/problems.jsonl`).
- Ensure scripts/config refer to the correct dataset path.

5. (Optional) Train the models
```bash
python src/train_classification.py --data_path data/problems.jsonl
python src/train_regression.py --data_path data/problems.jsonl
```
Trained models and the TF-IDF vectorizer will be saved to `models/`.

6. Run the Streamlit web app
```bash
python -m streamlit run app.py
```
The app will open in your browser at: http://localhost:8501

---

## Demo Video

https://drive.google.com/file/d/1zQs5i7bwotQqvtl46mCM9hU7X9YoACNS/view?usp=drive_link

---

## Project Structure (Files of Interest)

- `data/` — dataset (JSONL files)
- `src/` — data preprocessing, feature extraction, training, and inference scripts
- `models/` — saved TF-IDF vectorizer, SVM classifier, Random Forest regressor artifacts
- `app.py` — Streamlit web interface
- `requirements.txt` — Python package dependencies
- `notebooks/` — exploratory notebooks and experiments



## Author / Contact

Pranshu Sharma  
Project: AutoJudge — Predicting Programming Problem Difficulty  
GitHub: https://github.com/harryx32  
Email: sharmajiiitr8470@gmail.com

---

## License

This project is provided under the MIT License. See the LICENSE file for details.

---

Thank you for exploring AutoJudge. If you have questions or want suggestions for improving model performance or deployment, feel free to open an issue or contact me on GitHub.
