from tranformers import pipeline

# Load pre-trained GPT-3 model for text generation
gpt3_model = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Prompt for text generation
prompt_text = "Once upon a time, in a land far away"

# Generate text
generated_text = gpt3_model(prompt_text, max_length=100, do_sample=True)[0]['generated_text']

# Display text
print(generated_text)
