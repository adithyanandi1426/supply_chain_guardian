from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import AZURE_TEXT_ANALYTICS_ENDPOINT, AZURE_TEXT_ANALYTICS_KEY

def authenticate_client():
    return TextAnalyticsClient(
        endpoint=AZURE_TEXT_ANALYTICS_ENDPOINT,
        credential=AzureKeyCredential(AZURE_TEXT_ANALYTICS_KEY)
    )

def analyze_text(text):
    client = authenticate_client()
    response = client.analyze_sentiment(documents=[text])[0]
    key_phrases = client.extract_key_phrases(documents=[text])[0].key_phrases
    return {
        "Sentiment": response.sentiment,
        "ConfidenceScores": response.confidence_scores,
        "KeyPhrases": key_phrases
    }
