## Item-Based Collaborative Filtering for Movie Recommendations

This repository implements an item-based collaborative filtering recommender system for movies using Python. 

### Overview

Collaborative filtering is a technique used by recommender systems to suggest items to users based on the preferences of similar users or items. This code focuses on item-based collaborative filtering, where recommendations are based on the similarities between movies.

### Code Structure

The code is organized into the following steps:

1. **Data Preparation:** Reads and prepares the datasets (user ratings and movie titles).
2. **Data Exploration:** Explores the data by calculating descriptive statistics and visualizing the relationship between ratings and popularity.
3. **Creating User-Item Interaction Matrix (UII):** Transforms the data into a user-item matrix for efficient similarity calculations.
4. **Identifying Similar Movies:** Uses correlation to find movies with similar ratings to a chosen reference movie.
5. **Filtering Recommendations:** Sets a minimum threshold for the number of ratings a movie needs to be considered for recommendation.

### Dependencies

* Python (3.x recommended)
* pandas
* numpy

### Data Requirements

* Two datasets are required:
    * `u.data`: User ratings for movies (user_id, item_id, rating, timestamp). You can find a similar dataset online.
    * `Movie_Titles.csv`: Lists movie titles corresponding to item IDs in `u.data`. You can create this file manually or use a provided mapping file.

### Running the Code

1. Replace the file paths in the code with the locations of your datasets (`u.data` and `Movie_Titles.csv`).
2. Run the script (e.g., `python item_based_cf.py`).

The code will identify movies similar to a chosen reference movie (e.g., "Fargo (1996)") and recommend those with high correlation and sufficient user ratings.

### Next Steps

* This code provides a basic framework for item-based recommendations. You can extend it to:
    * Recommend movies to a specific user based on their past ratings.
    * Implement user-based collaborative filtering for a different approach.
* Experiment with different correlation measures and recommendation thresholds.
* Consider incorporating additional features like movie genre or release year.

### License

This code is provided for educational purposes only. Feel free to modify and adapt it for your own needs. 
