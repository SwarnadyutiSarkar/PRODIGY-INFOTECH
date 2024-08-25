from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

def load_dataset(file_path, tokenizer, block_size=128):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size
    )
    return dataset

def main():
    model_name = 'gpt2'  # You can choose 'gpt2-medium', 'gpt2-large', or 'gpt2-xl' based on your needs
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Load dataset
    file_path = 'data.txt'
    dataset = load_dataset(file_path, tokenizer)

    # Create data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir='./results',          # Output directory
        overwrite_output_dir=True,       # Overwrite the content of the output directory
        num_train_epochs=1,              # Number of training epochs
        per_device_train_batch_size=4,   # Batch size per device
        save_steps=10_000,                # Save checkpoint every 10,000 steps
        save_total_limit=2,              # Only keep the last 2 checkpoints
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset
    )

    # Start training
    trainer.train()

    # Save the model
    model.save_pretrained('./fine-tuned-gpt2')
    tokenizer.save_pretrained('./fine-tuned-gpt2')

if __name__ == "__main__":
    main()
