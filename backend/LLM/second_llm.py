import torch
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("shahxeebhassan/bert_base_ai_content_detector")
model = BertForSequenceClassification.from_pretrained("shahxeebhassan/bert_base_ai_content_detector")
inputs = tokenizer("hello im divy and tomorrow im going to home", return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

probabilities = torch.softmax(logits, dim=1).cpu().numpy()

predicted_label = probabilities.argmax(axis=1)

print(f"Predicted label for the input text: {predicted_label[0]}")