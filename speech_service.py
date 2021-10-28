from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC, Wav2Vec2CTCTokenizer, Wav2Vec2FeatureExtractor
import torch
import os
# import kenlm
# from pyctcdecode import build_ctcdecoder
from pydub import AudioSegment
import numpy as np

class Speech_Service:
    def __init__(self):
        #load pretrained processor and model
        tokenizer = Wav2Vec2CTCTokenizer(os.path.join('models/7/checkpoint-8000/vocab.json'), unk_token="[UNK]", pad_token="[PAD]", word_delimiter_token="|")
        feature_extractor = Wav2Vec2FeatureExtractor(feature_size=1, sampling_rate=16000, padding_value=0.0, do_normalize=True, return_attention_mask=True)
        self.processor = Wav2Vec2Processor(feature_extractor=feature_extractor, tokenizer=tokenizer)
        self.model = Wav2Vec2ForCTC.from_pretrained('models/7/checkpoint-8000')
        # self.lm = kenlm.Model('models/product_5_gram.arpa')
        # vocab_dict = self.processor.tokenizer.get_vocab()
        # sort_vocab = sorted((value, key) for (key,value) in vocab_dict.items())
        # self.vocab = [x[1].replace("|", " ") if x[1] not in self.processor.tokenizer.all_special_tokens else "" for x in sort_vocab]
        # self.lm_decoder = build_ctcdecoder(self.vocab, self.lm, alpha=0.5, beta=2.0, ctc_token_idx=69)

    def predict(self, audio_file, do_postprocess=False):
        sound = AudioSegment.from_file(audio_file)
        sound = sound.set_frame_rate(16000)
        samples = sound.get_array_of_samples()
        audio_Test = np.array(samples).T.astype(np.float32)
        inputs = self.processor(audio_Test, sampling_rate=16_000, return_tensors="pt", padding=True)

        #infer
        with torch.no_grad():
            logits = self.model(inputs.input_values,).logits

        # KenLM Decoded prediction
        if do_postprocess:
            lm_logits = logits.cpu().detach().numpy()[0]
            return [self.lm_decoder.decode(lm_logits, beam_width=500)]
        else:
            predicted_ids = torch.argmax(logits, dim=-1)
            return self.processor.batch_decode(predicted_ids)

if __name__ == "__main__":
    # create an instance of the speech service
    ss = Speech_Service()

    # make a prediction
    text = ss.predict("test.mp3")
    print(text)
    