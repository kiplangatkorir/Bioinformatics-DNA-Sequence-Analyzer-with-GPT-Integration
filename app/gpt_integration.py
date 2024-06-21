import openai

openai.api_key = 'YOUR_API_KEY'

def gpt_analysis(dna_sequence):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-16k",
        prompt=f"Analyze the following DNA sequence: {dna_sequence}",
        max_tokens=1024
    )
    return response.choices[0].text.strip()
