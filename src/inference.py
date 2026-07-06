from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

MODEL_PATH = "models/gpt2-finetuned"

print("Loading tokenizer...")
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)

print("Loading model...")
model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)

model.eval()

print("Model loaded successfully!")

while True:
    prompt = input("\nEnter Prompt (type 'exit' to quit): ")

    if prompt.lower() == "exit":
        break

    text = f"""### Instruction:
{prompt}

### Response:
"""

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=80,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\nGenerated Response:")
    print(response)