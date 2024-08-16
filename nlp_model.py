from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pre-trained model and tokenizer
model_name = 't5-small'  # You can use a different model if needed
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def generate_sql_query(natural_language_input, schema_info):
    input_text = f"Schema: {schema_info} Query: {natural_language_input}"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"])
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query
