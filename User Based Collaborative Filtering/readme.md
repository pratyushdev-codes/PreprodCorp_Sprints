# User-Based Collaborative Filtering for Movie Recommendations

This project implements User-Based Collaborative Filtering (UBCF) for recommending movies to users based on their ratings and the ratings of similar users.

## Functionality

1. **Data Loading:** Loads movie and rating data from CSV files.
2. **Data Preprocessing:**
    - Merges movie and rating data based on movie ID.
    - Filters movies with less than 100 ratings.
    - Creates a user-movie rating matrix.
    - Normalizes the rating matrix.
3. **User Similarity:**
    - Identifies similar users based on Pearson correlation or cosine similarity.
4. **Recommendation:**
    - Recommends movies to a target user based on the ratings of similar users.
    - Predicts the rating for the recommended movies.

## Dependencies

This project requires the following Python libraries:

* pandas
* numpy
* scipy.stats
* seaborn
* sklearn

You can install them using pip:

```bash
pip install pandas numpy scipy seaborn scikit-learn