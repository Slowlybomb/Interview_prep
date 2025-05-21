import re

def filter_reviews(reviews: list[str]) -> list[str]:
    """Write a function to filter out duplicate reviews from a list. 
    A review is considered duplicate if the text 
    (case-insensitive, ignore punctuation and spacing) is the same.
    
    Input: ["Great product!", "great PRODUCT", "Would buy again."]

    Output: ["Great product!", "Would buy again."]"""
    seen = set()
    output = []

    for review in reviews:
        normalised = re.sub(r'[^a-zA-Z0-9]', '', review).lower()
        if normalised not in seen:
            seen.add(normalised)
            output.append(review)

    return output

if __name__ == "__main__":
    """Input: ["Nice!", "nice", "Nice  ", "Not bad", "NOT BAD"]
    Output: ["Nice!", "Not bad"]

    Input: ["I love it", "i Love  it!!", "Meh", "meh.", "MEH"]
    Output: ["I love it"]

    Input: ["Perfect", "Almost perfect", "Perfect!"]
    Output: ["Perfect", "Almost perfect"]"""

    reviews = ["Great product!", "great PRODUCT", "Would buy again."]
    print(filter_reviews(reviews))