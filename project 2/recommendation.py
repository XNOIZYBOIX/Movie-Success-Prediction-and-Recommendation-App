import pandas as pd
from flask import Flask, render_template, request

df = pd.read_csv('updated_file_G.csv')

df = df.dropna(subset=['genre_names'])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Recommendation page
@app.route('/recommendations', methods=['POST'])
def recommendations():
    selected_genres = request.form.getlist('genres')
    recommended_movies = []
    for genre in selected_genres:
        genre_movies = df[df['genre_names'].str.contains(genre)]
        recommended_movies.extend(genre_movies['title'].tolist())
    return render_template('recommendations.html', movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
