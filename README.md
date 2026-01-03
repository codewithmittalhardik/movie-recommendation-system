# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/Numpy-013243?logo=numpy&logoColor=white)

A content-based movie recommendation system built with Python. This application analyzes movie metadata (genres, keywords, cast, and crew) to suggest movies similar to the user's selection using Cosine Similarity.

## 🚀 Features
* **Interactive Web Interface:** User-friendly UI built with Streamlit.
* **Smart Recommendations:** Suggests the top 5 most similar movies based on content.
* **Search Functionality:** Instantly search for movies within the database.
* **Poster Integration:** Fetches and displays movie posters using the TMDB API.

## 🛠️ Tech Stack
* **Python:** Core programming language.
* **Streamlit:** For building the web application interface.
* **Pandas:** For data manipulation and frame management.
* **NumPy:** For efficient numerical operations.
* **Scikit-learn:** For `CountVectorizer` and calculating `Cosine Similarity`.

## 📂 Project Structure
```bash
movie-recommender/
├── data/
│   └── tmdb_5000_movies.csv    # Raw dataset
├── app.py                      # Main Streamlit application
├── movies.pkl                  # Pickled movie list (generated)
├── similarity.pkl              # Pickled similarity matrix (generated)
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```
**Clone the repository**
```bash
git clone [https://github.com/codewithmittalhardik/movie-recommendation-system.git](https://github.com/codewithmittalhardik/movie-recommendation-system.git)
```
```bash
cd movie-recommendation-system
```
**Create a virtual environment**
```bash
python -m venv venv
```
```bash
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
**Install dependencies**
```bash
pip install -r requirements.txt
```
**Run the application**
```bash
streamlit run app.py
```
