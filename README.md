# SpaceX Falcon 9 Landing Prediction

**IBM Applied Data Science Capstone**

---

## 🎯 Project Goal

To predict whether the SpaceX Falcon 9 first stage will land successfully. This determines if a launch costs **$62 million** (reusable) or **$165 million** (not reusable).

## 📁 Repository Map

* **`data/`**: Raw and cleaned CSV files.
* **`notebooks/`**: End-to-end data science pipeline (API, SQL, Maps, Dashboard, ML).
* **`presentation/`**: Final results and business insights.

## 🛠️ Tech Stack

* **Python:** Pandas, Scikit-Learn
* **Visualization:** Folium, Plotly Dash, Seaborn
* **Database:** SQL (SQLite)

## 🔬 Key Insights

* **Launch Sites:** KSC LC-39A has the highest success rate.
* **Trends:** Success rates have improved significantly over time.
* **Orbits:** ES-L1, GEO, and HEO orbits show the highest landing success.

## 🤖 Machine Learning Results

All models were tuned using **GridSearchCV** and tested on unseen data.

| Algorithm | Accuracy |
| --- | --- |
| **Decision Tree** | **83.3%** |
| **SVM** | **83.3%** |
| **Logistic Regression** | **83.3%** |
| **K-Nearest Neighbors** | **83.3%** |

## 🚀 Quick Start

1. `git clone [https://github.com/YOUR_GITHUB_USERNAME/Data-Science-Capstone-Spacex.git](https://github.com/YOUR_GITHUB_USERNAME/Data-Science-Capstone-Spacex.git)`
2. `pip install -r requirements.txt`
3. Run the notebooks in the `notebooks/` folder sequentially.

---

**Author:** Yash Pandey

**Connect:** [LinkedIn](https://www.linkedin.com/in/yash-pandey-151961213/) | [Email](pandeyyash25@gmail.com)
