import sys
import flair
import torch
from flair.data import Corpus
from flair.datasets import ClassificationCorpus, DataLoader
from flair.models import TextClassifier
from flair.tokenization import SpaceTokenizer

def main():

    # this is the folder in which train, test and dev files reside
    data_folder = ""
    model_path = "bert_model_v4"
    out_path = "prediction.txt"

    flair.device = torch.device('cuda:0')

    # load corpus containing training, test and dev data
    corpus: Corpus = ClassificationCorpus(data_folder, tokenizer=SpaceTokenizer(), test_file='cleanedValidationFlair-2.txt')
                                                                            
    classifier = TextClassifier.load(model_path + '/final-model.pt')

    #test_data_loader = DataLoader(corpus.test, batch_size=32)
    test_data_loader = DataLoader(corpus.test)
    result = classifier.evaluate(test_data_loader.dataset, gold_label_type='class', out_path=out_path)
    print(result)

if __name__ == "__main__":
    main()