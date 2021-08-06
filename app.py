import gradio as gr
import torch
from transformers import AutoTokenizer, EncoderDecoderModel

tokenizer = AutoTokenizer.from_pretrained("monsoon-nlp/es-seq2seq-gender-encoder", model_max_length=256)
model = EncoderDecoderModel.from_encoder_decoder_pretrained(
  "monsoon-nlp/es-seq2seq-gender-encoder",
  "monsoon-nlp/es-seq2seq-gender-decoder",
  max_length=40,
)

def flip(content):
    input_ids = torch.tensor(tokenizer.encode(content)).unsqueeze(0)
    generated = model.generate(input_ids, decoder_start_token_id=model.config.decoder.pad_token_id)
    op = tokenizer.decode(generated.tolist()[0][1:])
    if '[SEP]' in op:
        return op[:op.index('[SEP]')]
    return op

iface = gr.Interface(fn=flip,
	inputs=gr.inputs.Textbox(label="Original Spanish text"),
	outputs=gr.outputs.Textbox(label="Flipped"),
	description="seq2seq built from BETO model - see https://huggingface.co/monsoon-nlp/es-seq2seq-gender-encoder",
)
iface.launch()
