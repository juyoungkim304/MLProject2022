import sys
import flair, torch
from flair.data import Corpus
from flair.datasets import ClassificationCorpus
from flair.embeddings import TransformerDocumentEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer
from flair.tokenization import SpaceTokenizer
from torch.optim.lr_scheduler import OneCycleLR

from torch.optim.adam import Adam
from torch.optim.adamw import AdamW

def main():

    flair.device = torch.device('cuda:0')

    # this is the folder in which train, test and dev files reside
    data_folder = ""
    bert_dir = "digitalepidemiologylab/covid-twitter-bert-v2"
    model_path = "bert_model"

    print(bert_dir)
    print(model_path)

    # load corpus containing training, test and dev data
    # train/val split comes from the train_file
    # dev file "visualizes" the model performance on the dev/test - to pick best model
    # we're looking for the performance on the final model regardless, so dev_file doesn't matter
    corpus: Corpus = ClassificationCorpus(data_folder, tokenizer=SpaceTokenizer(), train_file='cleanedTrainingFlair-2.txt',
                                  test_file='cleanedValidationFlair-2.txt',
                                  dev_file='cleanedValidationFlair-2.txt')

    label_dict = corpus.make_label_dictionary(label_type='class')

    document_embeddings = TransformerDocumentEmbeddings(bert_dir, layers='all', layer_mean=True, fine_tune=True)

    classifier = TextClassifier(document_embeddings, label_dictionary=label_dict, multi_label=False, label_type='class')

    trainer = ModelTrainer(classifier, corpus)

    trainer.train(model_path,
                #optimizer=Adam,
                optimizer=AdamW,
                #learning_rate=1e-5,
                learning_rate=5e-6,
                scheduler=OneCycleLR,
                #patience=25,
                #max_epochs=25,
                patience=20,
                max_epochs=20,
                mini_batch_size=128,   
                mini_batch_chunk_size=2,   
                num_workers=2,                  
                )


if __name__ == "__main__":
    main()