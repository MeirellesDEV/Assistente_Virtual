from tensorflow.keras.models import load_model

model = load_model('baxacinho.0.1')

import leitor_tensorflow as tf

def analisarFrase(str):
    frase = str
    nova_sequencia = tf.tokenizer.texts_to_sequences([frase])
    nova_sequencia_padded = tf.pad_sequences(nova_sequencia, maxlen=100, truncating='post', padding='post')
    prediction = model.predict(nova_sequencia_padded)[0]

    mapping_reverse = {0: 'alegria', 1: 'neutro', 2: 'tristeza', 3: 'raiva'}

    for i, prob in enumerate(prediction):
        print(f'{mapping_reverse[i]}: {prob:.3f}')
        
        if f'{mapping_reverse[i]}' == 'alegria': 
            alegria = f'{prob:.3f}'

        if f'{mapping_reverse[i]}' == 'raiva': 
            raiva = f'{prob:.3f}'

        if f'{mapping_reverse[i]}' == 'tristeza': 
            tristeza = f'{prob:.3f}'

        if f'{mapping_reverse[i]}' == 'neutro': 
            neutro = f'{prob:.3f}'

    return tf.sentimento(alegria, raiva, tristeza, neutro) 

#testando função
#print(type(analisarFrase("VAI SE FUDEEEEEE")))