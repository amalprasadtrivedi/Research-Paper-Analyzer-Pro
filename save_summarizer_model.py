# save_summarizer_model.py
from transformers import BartTokenizer, BartForConditionalGeneration

model_name = "facebook/bart-large-cnn"
save_path = "assets/models/summarizer_model/"

# Load tokenizer and model
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Save to assets/models/summarizer_model/
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

print(f"✅ BART summarizer model saved to {save_path}")
