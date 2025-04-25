import openai
from config import AZURE_OPENAI_API_KEY

openai.api_key = AZURE_OPENAI_API_KEY

def extract_risks_gpt(text):
    prompt = f"""Analyze the following supply chain related content and extract:
1. Potential risks
2. Affected regions or suppliers
3. Severity and urgency
4. Recommended mitigations

Content:
{text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return response.choices[0].message.content
