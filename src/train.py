from datasets import load_from_disk
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    Trainer,
    TrainingArguments,
    DefaultDataCollator,
)

# Load dataset
dataset = load_from_disk("data/tokenized")

# Load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Load model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Data collator
data_collator = DefaultDataCollator()

# Training arguments
training_args = TrainingArguments(
    output_dir="models/gpt2-finetuned",
    do_train=True,
    num_train_epochs=20,
    per_device_train_batch_size=2,
    learning_rate=5e-5,
    logging_strategy="steps",
    logging_steps=1,
    save_strategy="epoch",
    report_to="none",
    remove_unused_columns=False,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator,
)

trainer.train()

trainer.save_model("models/gpt2-finetuned")
tokenizer.save_pretrained("models/gpt2-finetuned")

print("\n✅ Training Completed")