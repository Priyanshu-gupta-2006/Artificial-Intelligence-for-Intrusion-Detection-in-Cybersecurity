from sklearn.feature_extraction.text import CountVectorizer

def preprocess_data(activity_data):
    """
    Converts user activity data into numerical representation.
    """
    vectorizer = CountVectorizer()
    activity_vector = vectorizer.fit_transform(activity_data).toarray()
    return vectorizer, activity_vector