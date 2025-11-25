from transformers import pipeline
import torch

import csv

####################################################################
# When running the 'twitter-roberta-base-sentiment' model, uncomment
# each code block the relates to that model and comment out the
# code that is labeled with 'bertweet-base-sentiment-analysis' and
# vice versa
# Comments Areas include:
#   - result variable in "getSentiment()"
#   - labelMap variable in "getSentiment()"
#   - model variable directly below this comment
####################################################################

# model = "cardiffnlp/twitter-roberta-base-sentiment-latest"
model = "finiteautomata/bertweet-base-sentiment-analysis"


pipe = pipeline(
    "text-classification",
    model=model,
    device=0 if torch.cuda.is_available() else -1
)


def getSentiment(text: str):
    max_len = 500
    chunks = [text[i:i + max_len] for i in range(0, len(text), max_len)]

    sentiments = []
    for chunk in chunks:
        # result = pipe(chunk, truncation=True, max_length=512)[0] # twitter-roberta-base-sentiment
        result = pipe(chunk, truncation=True, max_length=128)[0] # bertweet-base-sentiment-analysis
        sentiments.append(result)

    avg_score  = sum(r['score'] for r in sentiments) / len(sentiments)
    main_label = max(sentiments, key=lambda r: r['score'])['label']

    ## twitter-roberta-base-sentiment
    # labelMap = {
    #     "LABEL_0": "Negative",
    #     "LABEL_1": "Neutral",
    #     "LABEL_2": "Positive",
    # }
    # bertweet-base-sentiment-analysis
    labelMap = {
        "NEG": "Negative",
        "NEU": "Neutral",
        "POS": "Positive",
    }
    retSent = labelMap.get(main_label, main_label)
    return retSent, f"{round(avg_score, 4)}"


def addToCSV(result, outCSV, id, model, comment):
    reviewer = f"{model}, Jon Wasky"
    with open(outCSV, 'a',newline='' , encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([id, comment, reviewer, result])


if __name__ == "__main__":

    csvPath = input("Please enter the path to the non-reviewed-assessments:\nEx: ~/Repos/sentiment-analysis-swj/deliverables/data/non-reviewed-assessments-base.csv\n")

    outCSV = input("Please enter the path to the output CSV,\nEx: ~/Documents/SentimentResults/twitter-roberta-base.csv\n")

    with open(outCSV, 'a', newline='' , encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["paper_id", "comment", "analyst", "sentiment"])

    with open(csvPath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for (i, row) in enumerate(reader):
            print(f"Paper ID: {row['paper_id']}")
            review = row['comment']

            sentiment, score = getSentiment(review)

            addToCSV(sentiment, outCSV, row['paper_id'], model, row['comment'])
            print(f"    Sentiment: {sentiment}, Score: {score}")


