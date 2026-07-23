#!/usr/bin/env python3

import csv

# Load dataset
tweets = []

with open("twitter_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tweets.append(row)


# Quest 1: Clean Data
def clean_data(data):
    cleaned = []
    fixed = 0

    for tweet in data:
        text = tweet.get("Text", "").strip()

        if text == "":
            fixed += 1
            continue

        if tweet.get("Likes", "").strip() == "":
            tweet["Likes"] = "0"
            fixed += 1

        if tweet.get("Retweets", "").strip() == "":
            tweet["Retweets"] = "0"
            fixed += 1

        cleaned.append(tweet)

    print("Rows fixed/removed:", fixed)
    return cleaned


# Quest 2: Find Most Liked Tweet
def find_most_liked(data):
    highest = data[0]

    for tweet in data:
        if int(tweet["Likes"]) > int(highest["Likes"]):
            highest = tweet

    print("\nMost Liked Tweet")
    print("Username:", highest["Username"])
    print("Likes:", highest["Likes"])
    print("Text:", highest["Text"])


# Quest 3: Bubble Sort
def sort_by_likes(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if int(data[j]["Likes"]) < int(data[j + 1]["Likes"]):
                data[j], data[j + 1] = data[j + 1], data[j]

    print("\nTop 10 Most Liked Tweets")

    top = 10 if len(data) >= 10 else len(data)

    for i in range(top):
        print(
            i + 1,
            data[i]["Username"],
            "-",
            data[i]["Likes"],
            "likes"
        )


# Quest 4: Search
def search_by_keyword(data):
    keyword = input("\nEnter keyword: ").lower()

    results = []

    for tweet in data:
        if keyword in tweet["Text"].lower():
            results.append(tweet)

    print("\nFound", len(results), "matching tweets\n")

    for tweet in results:
        print(tweet["Username"], ":", tweet["Text"])


tweets = clean_data(tweets)
find_most_liked(tweets)
sort_by_likes(tweets)
search_by_keyword(tweets)