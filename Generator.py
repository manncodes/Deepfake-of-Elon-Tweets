from flask import Flask, render_template, request

import random
from twitter import Tweet
from keras.backend import clear_session
import os
from keras_gpt_2 import load_trained_model_from_checkpoint, get_bpe_from_files, generate

app = Flask(__name__)
    
model_folder = 'checkpoint/run1'    
config_path = os.path.join(model_folder, 'hparams.json')
checkpoint_path = os.path.join(model_folder, 'model-1000')
encoder_path = os.path.join(model_folder, 'encoder.json')
vocab_path = os.path.join(model_folder, 'vocab.bpe')

@app.route('/')
def index():
    return render_template('index.html')

def generate_op(text):
    print('Generate text...')
    #output = generate(model, bpe, ['From the day forth, my arm'], length=20, top_k=1)
    output = generate(model, bpe, [str(text)], length=20, top_k=1)
    return output

@app.route('/', methods=['POST'])
def getValue():
    clear_session()
    if(request.form['submit_btn']=="Submit"):
        text = request.form['user_str']
        length = request.form['user_len']
    elif(request.form['submit_btn']=="Generate"):
        text = " "
        length = random.randint(1,40)


    print('Load model from checkpoint...')
    model = load_trained_model_from_checkpoint(config_path, checkpoint_path)
    print('Load BPE from files...')
    bpe = get_bpe_from_files(encoder_path, vocab_path)
    
    #if(text!=None):
    print('Generate text...')
    #output = generate(model, bpe, ['From the day forth, my arm'], length=20, top_k=1)
    output = generate(model, bpe, [str(text)], length=int(length), top_k=2)

    #print(output)
    ind = output[0].rfind("\n")
    temp = output[0]
    temp = temp[0:ind]
    #print(temp)
    output[0] = temp
    #print(output)        

    try:
        if(request.form['tweet']=="post"):
            Tweet(str(output[0]))
    except:
        print("")

    return render_template('index.html', t=output)

if __name__ == '__main__':
    app.run(debug=True)
