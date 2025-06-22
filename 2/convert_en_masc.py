import os

from stanza.models.constituency import tree_reader
from stanza.utils.datasets.constituency import utils



def read_files(input_path):
    tree_files = [os.path.join(input_path, x) for x in os.listdir(input_path)]
    all_sents = []
    sent = ''
    for file in tree_files:
        with open(file, encoding='utf-8') as fin:
            lines = fin.readlines()
            for line in lines:
                if line != '\n':
                    sent += line.strip()
                else:
                    sent = sent.replace('( (' , '(ROOT (').replace('\n', '')
                    if '(CODE' not in sent and sent != '':
                        if sent.count('(') == sent.count(')'):
                            all_sents.append(sent)
                    sent = ''
    return all_sents

def convert_en_masc(input_path, train_size=0.8, dev_size=0.1):
    sents = read_files(input_path)
    natural_trees = []

    for sent in sents:
        trees = tree_reader.read_trees(sent)
        # if len(trees) != 1:
        #     raise ValueError("Unexpectedly found %d trees in sentence: %s" % (len(trees), sent))
        tree = trees[0]
        natural_trees.append(tree)

    print("Read %d natural trees" % len(natural_trees))
    train_trees, dev_trees, test_trees = utils.split_treebank(natural_trees, train_size, dev_size)
    print("Split %d trees into %d train %d dev %d test" % (len(natural_trees), len(train_trees), len(dev_trees), len(test_trees)))
    print("Total lengths %d train %d dev %d test" % (len(train_trees), len(dev_trees), len(test_trees)))
    return train_trees, dev_trees, test_trees