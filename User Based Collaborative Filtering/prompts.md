# This script helps you discover movies you might enjoy based on your past ratings and the preferences of users similar to you.

## General Prompts

What are the key data insights from the ratings and movies datasets?

What exploratory data analysis (EDA) steps should be performed before applying collaborative filtering?

How do we decide on a threshold (e.g., 100 ratings) for filtering popular movies?

What visualization techniques can we use to understand relationships between ratings and number of reviews?

## Data Preparation

Loading and Understanding the Data

How can we effectively load large datasets for processing in Python?

What are the unique values and distributions for userId, movieId, and rating?

How can we merge datasets to include meaningful information like movie titles in the ratings data?

## Data Filtering

What is the impact of filtering movies with less than 100 ratings on recommendations?

How can we identify the most popular movies based on the number of ratings?

Why is it important to limit the dataset to frequently rated movies?

##  Data Normalization

How does normalizing ratings improve similarity calculations?

What methods can be used to normalize a user-item matrix?

## Similarity Computation

### Correlation-Based Similarity

How does Pearson correlation measure user similarity?

What are the advantages and limitations of using correlation for similarity?

### Cosine Similarity

Why is cosine similarity used in collaborative filtering?

How does cosine similarity differ from correlation-based similarity?

##  Similar User Identification

How do we define a threshold (e.g., 0.3) for user similarity?

What is the significance of selecting the top n similar users?

What are some strategies to efficiently shrink the pool of potential recommendations?

## Recommendation Generation

Filtering Movies for Recommendations

How do we filter out movies already watched by the target user?

What is the impact of removing unwatched movies from the similar user pool?

## Scoring Movies

What is the formula for scoring a movie based on similar user ratings?

Why is the weighted average used to calculate the movie score?

## Ranking and Prediction

How can we rank movies based on predicted scores?

What does the predicted rating signify for the user?

How do we decide on the number (m) of movies to recommend?

Why might top recommended movies have high predicted ratings (e.g., > 4.5)?

## Evaluation

How can we validate the quality of the recommendations?

What metrics can be used to assess the performance of the recommendation system?

What improvements can be made to enhance recommendations?

