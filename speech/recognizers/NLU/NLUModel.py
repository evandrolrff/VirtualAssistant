import pickle  # Adicione no topo com os outros imports
import os
import yaml
import numpy as np
import tensorflow as tf
from pathlib import Path
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.utils import to_categorical

class NLUModel:
    def __init__(self, config_path = 'train.yml'):
        self.training_path_file = os.path.join(os.path.dirname(__file__), config_path)
        self.inputs = []
        self.outputs = []
        self.chars = set()
        self.chr2idx = {}
        self.idx2chr = {}
        self.max_seq = 0
        self.labels = set()
        self.label2idx = {}
        self.idx2label = {}
        self.model = None
        self.input_data = None
        self.output_data = None
               

    def load_data(self):
        """Carrega os dados do arquivo YAML"""
        try:
            data = yaml.safe_load(open(self.training_path_file, 'r', encoding='utf-8').read())
            
            self.inputs = []
            self.outputs = []
            
            for command in data['commands']:
                self.inputs.append(command['input'].lower())
                self.outputs.append('{}\\{}'.format(command['entity'], command['action']))
                
            return True
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False

    
    def preprocess_text(self):
        """Pré-processa o texto e cria mapeamentos de caracteres"""
        self.chars = set()
        
        for text in self.inputs + self.outputs:
            for ch in text:
                if ch not in self.chars:
                    self.chars.add(ch)
        
        # Mapeamento caracteres para índices
        self.chr2idx = {ch: i for i, ch in enumerate(self.chars)}
        self.idx2chr = {i: ch for i, ch in enumerate(self.chars)}
        
        # Tamanho da maior sequência
        self.max_seq = max([len(x) for x in self.inputs])
        
        print('Número de chars:', len(self.chars))
        print('Maior seq:', self.max_seq)

    
    def prepare_input_data(self):
        """Prepara os dados de entrada no formato adequado"""
        self.input_data = np.zeros((len(self.inputs), self.max_seq), dtype='int32')
        
        for i, input_text in enumerate(self.inputs):
            for k, ch in enumerate(input_text):
                self.input_data[i, k] = self.chr2idx[ch]

    
    def prepare_output_data(self):
        """Prepara os dados de saída (labels) no formato adequado"""
        self.labels = set(self.outputs)
        self.label2idx = {label: i for i, label in enumerate(self.labels)}
        self.idx2label = {i: label for i, label in enumerate(self.labels)}
        
        # Converter outputs para índices numéricos
        output_numeric = np.array([self.label2idx[output] for output in self.outputs])
        
        # Converter para one-hot encoding
        self.output_data = to_categorical(output_numeric, num_classes=len(self.labels))

    
    def build_model(self):
        """Constrói o modelo LSTM"""
        self.model = Sequential([
            Embedding(len(self.chars), 64, input_length=self.max_seq),
            LSTM(128),
            Dense(len(self.labels), activation='softmax')
        ])
        
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        print(self.model.summary())


    def train(self, epochs=50, batch_size=32):
        """Treina o modelo"""
        if self.model is None:
            print("Modelo não foi construído. Chame build_model() primeiro.")
            return
        
        history = self.model.fit(
            self.input_data,
            self.output_data,
            epochs=epochs,
            batch_size=batch_size,
            verbose=1
        )
        
        return history
    

    def predict(self, text):
        """Faz predição para um novo texto de entrada"""
        if self.model is None:
            print("Modelo não foi treinado. Chame train() primeiro.")
            return None
        
        # Pré-processa o texto garantindo o comprimento mínimo
        if not text or len(text.strip()) == 0:
            print("Texto de entrada vazio!")
            return None
            
        text = text.lower().strip()
        
        # Pré-processa o texto de entrada
        processed = np.zeros((1, self.max_seq), dtype='int32')
        
        # Preenche com os caracteres válidos
        for k, ch in enumerate(text[:self.max_seq]):  # Garante que não excede max_seq
            if ch in self.chr2idx:
                processed[0, k] = self.chr2idx[ch]
            else:
                # Tratamento para caracteres não vistos - pode usar um valor padrão
                processed[0, k] = 0  # Ou len(self.chars) para um token desconhecido
        
        # Verificação final para evitar sequências vazias
        if np.all(processed == 0):
            print("Nenhum caractere válido encontrado na entrada!")
            return None
            
        try:
            prediction = self.model.predict(processed, verbose=0)
            predicted_idx = np.argmax(prediction)
            return self.idx2label[predicted_idx]
        except Exception as e:
            print(f"Erro durante a predição: {e}")
            return None
    

    def save_model(self, filepath='nlu_model.h5'):
        """Salva o modelo treinado"""
        trained_model = os.path.join(os.path.dirname(__file__), filepath)
        metadata = {
            'chr2idx': self.chr2idx,
            'idx2chr': self.idx2chr,
            'max_seq': self.max_seq,
            'label2idx': self.label2idx,
            'idx2label': self.idx2label
        }

        if self.model:
            self.model.save(trained_model)
            # Salva os metadados com extensão .pkl
            with open(trained_model.replace('.h5', '.pkl'), 'wb') as f:
                pickle.dump(metadata, f)
            print(f"Modelo e metadados salvos em {trained_model}")
    

    def load_model(self, filepath='nlu_model.h5'):
        """Carrega um modelo previamente treinado"""
        metadata_path = filepath.replace('.h5', '.pkl')
        self.model = tf.keras.models.load_model(filepath)

        # Carrega os metadados
        with open(metadata_path, 'rb') as f:
            metadata = pickle.load(f)
        
        # Restaura os parâmetros
        self.chr2idx = metadata['chr2idx']
        self.idx2chr = metadata['idx2chr']
        self.max_seq = metadata['max_seq']
        self.label2idx = metadata['label2idx']
        self.idx2label = metadata['idx2label']

        # Recompila para evitar o warning das métricas
        self.model.compile(optimizer='adam',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])
        print(f"Modelo carregado de {filepath}")


    def exist_model(self, filepath='nlu_model.h5'):
        """Verifica se o modelo já existe e carrega ele. Do contrário, treina um novo modelo"""
        trained_model = os.path.join(os.path.dirname(__file__), filepath)

        if Path(trained_model).exists():
            print("Modelo encontrado. Carregando...")
            try:
                self.load_model(trained_model)
                print("Modelo carregado com sucesso!")
            except Exception as ex:
                print(f"Erro ao carregar o modelo: {ex}")
                print("Treinando um novo modelo...")
                self.train_new_model()
        else:
            print("Modelo não encontrado. Treinando um novo...")
            self.train_new_model()


    def train_new_model(self):
        """Executa todo o fluxo de treinamento de um novo modelo"""
        if self.load_data():
            self.preprocess_text()
            self.prepare_input_data()
            self.prepare_output_data()
            self.build_model()
            self.train(epochs=50)
            self.save_model()