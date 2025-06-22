# PoS Taggers, Constituency Parsers and Dependency Parsers

This repository holds a project I worked on in one of my Master's course.

## Overview
The project was to do a set of tasks related to common tools used in Natural Language Processing (NLP). 
Mainly, PoS taggers, Constituency Parsers and Dependency Parsers.

All the implementations are located in the Jupyter Notebook: `PoSConstDepParsers.ipynb`


> [!WARNING]
> At the time of writing this README, there is a bug on GitHub where the Jupyter Notebooks do not render in the preview page. More info on this issue can be found here: [Notebook no longer rendering on GitHub: "state" key missing from metadata.widgets #155944](https://github.com/orgs/community/discussions/155944). If a solution is found to this issue I will update this README to remove this warning.


You can read the full report I wrote for this task in the `report(spanish).pdf` file. It is written in Spanish. If someone is interested I might translate it to english in the future. 

The Notebook itself also has almost everything explained (also in Spanish), again if requested I might translate it to English in the future.


## Tasks
The tasks proposed for the completion of this project are described as follows (translated to english):

### Task 1: Training and Labeling with PoS Taggers

#### a) With pre-trained models
Find and download a freely available tagger(s) that includes pre-trained models for two languages: (1) English and (2) a Romance language. Use it to tag a text file (.txt) of approximately 10,000 words for each language.


For each tagger used, include a section in the report analyzing its characteristics (the model it is based on, etc.), the URL of the website where it was obtained, whether and how the input text needed to be preprocessed, a brief analysis of the output, etc. 
A compressed file containing a subdirectory for each language will also be attached, including:
* a text file indicating the URL of the original source of the tagged text (URL.txt),
* the raw input text file to be tagged (INPUT_RAW.txt),
* and a copy of the tagger output for that input (OUTPUT_RAW.txt).

> In this repo you can find the INPUT_RAW and OUTPUT_RAW files for all the languages I used.

#### b) Training the models
The same applies, but without using pre-trained models. Search for freely available corpora with which to train the tagger.

The same as in the previous section, including as much information as possible regarding the different training corpora used, the characteristics of the machine used, and the training times required.

### Task 2: Training and Evaluation of Constituent Parsers

#### a) English + Romance language
Search for and download a parser based on freely available constituents and then train and evaluate it for two languages: (1) English and (2) a Romance language.

For each parser used, the report will include a section analyzing its characteristics (model on which it is based, etc.), the URL of the website where it was obtained, whether it was necessary to preprocess the input text/postprocess the output and how, etc. Similarly, separate sections must be included describing the characteristics of the treebanks used, whether they needed to be adapted and how, etc.
Finally, for each language, a comparative table(s) and/or graph(s) of the results obtained with each parser will be included, as well as a brief analysis of those results, along with the characteristics of the machine used and the training times required.


#### b) Other parsers and/or languages
Same as Task 1.b, expand the study to include more parsers and, above all, more languages.

> This is probably the hardest task in the project, mainly because of the scarcity of freely available Constituency Treebanks.


### Task 3: Training and Evaluation of Dependency Parsers
Basically the same as Exercise 2 but this time with dependency-based parsers.

#### a) English + Romance language
This task is essentially the same as for the case of constituent-based analysis (Task 2.a), but this time: (1) two parsers instead of just one; (2) analysis of dependencies instead of constituents.

#### b) Other parsers and/or languages
Again, this task is the same as for the case of constituent-based analysis (Task 2.b), although this time for dependency analysis.


## Implementation
As said in the Overview, all the implementation is done in the Jupyter Notebook: `PoSConstDepParsers.ipynb`.

This notebook was originally created in [Google Colab](https://colab.google/) and all the training and inference were carried out in that platform, so some changes had to be made to accommodate the limitations (specially GPU usage time and memory consumption) of Google Colab. 

Two main libraries were used in this project: 

* SpaCy

* Stanza

## Notes
The Treebanks were left out of the repo as they can be found on each source respectively. 

For all the cases where `SpaCy` was used, a `configuration.cfg` file was created. These files are used to configure the training of each model.
They contain the language and pipeline used for each model. More information about these configuration files can be found in the [SpaCy Documentation](https://spacy.io/usage/training#config).
This file is not completed as is, a command has to be used to complete the configuration file, those command are also added in the notebook.

Also, to get the outputs in `.conllu` format from `SpaCy` an additional library is needed: `spacy_conll`. Then a component `conll_formatter` has to be added to the model's pipeline to be able to output files in `Conllu` format.


Finally, the evaluation was carried out using a wrapper function using a portion of the `conll18_ud_eval.py` script from the [CoNLL 2018 Shared Task](https://universaldependencies.org/conll18/evaluation.html) and also added to this repository.

In the cases where `Stanza` was used it was necessary to clone the repo to properly train the models, more info on this process can be found in the [Stanza Documentation](https://stanfordnlp.github.io/stanza/training_and_evaluation.html).

For the constituency parsers using `Stanza`, a configuration script had to be created to set environment variables that point to the proper directories. That configuration can be found in this repository in `2/config.sh`. I placed this configuration script in the stanza directory (after cloning the repo) in `stanza/scripts/config.sh`. 
For more information on how to train a Constituency parser using stanza, refer to the [Stanza documentation](https://stanfordnlp.github.io/stanza/new_language_constituency.html)

Finally, some of the treebanks used for the constituency models had different structure than expected (Most libraries expect the PennTreeBank structure `PTB`). To prepare the datasets, a script was created and added to the local cloned repo of `stanza` and the main script to prepare the datasets was also modified to add all the treebanks used:
* `convert_en_masc.py` New script used to convert the EN MASC treebank to PTB format.
*  `prepare_con_dataset.py` Stanza script modified to add all the treebanks used to train the constituency parsers. 