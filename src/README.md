This model lets you perform monotone Sequence-to-sequence translation including Grapheme-to-Phoneme Conversion, OCR post-correction, and lemmatization.

## Requirements

* M2M aligner: https://github.com/letter-to-phoneme/m2m-aligner
* Marmot: http://cistern.cis.lmu.de/marmot/

## Configuration

- Please specify the path to Marmot in the following files: 
  1. `makeModel-segmenter-order_complex.sh`
  2. `decode-simple_dev.sh`

`marmotTagger=~/projects/marmot/marmot-2015-06-12.jar`

- Specify the path to the m2m aligner in `train_complex.sh`:

`path2M2M=~/projects/OCR/OCR/m2m-aligner-master/`


# Training a model

- To train a 3rd order model for 10 iterations with quadratic penalty of 0.5 and a context window size of 4, run:

```
order=3
iter=10
qpenalty=0.5
w=4
```

`./train_complex.sh data/twitter.200.train ${order} ${iter} ${qpenalty} ${w}`

- Be sure that characters in the training file are separated by a space, and input and output strings are separated by TAB.
- Your files should be UTF-8 encoded.


# Testing a model

- After training, you can apply the trained models as follows:

`./test_dev.sh data/twitter.1K.test MODELS_cl/twitter.200.train.nopipe.m-mAlign.1-2.delX.1-best.conYX.align.rl-align.marmot-3-10-0.5-4 ${w} > my.out`

- This should lead to a word accuracy of 16.66%.


# Citation
Please use the following citation if you use this code.

```
@inproceedings{TUD-CS-2016450,
	author = {Carsten Schnober and Steffen Eger and Erik-Lân Do Dinh and Iryna Gurevych},
	title = {Still not there? Comparing Traditional Sequence-to-Sequence Models to
Encoder-Decoder Neural Networks on Monotone String Translation Tasks},
	month = dec,
	year = {2016},
	booktitle = {Proceedings of the 26th International Conference on Computational
Linguistics (COLING)},
	pages = {(1703--1714)},
	location = {Osaka, Japan},
	language = {English},
	pubkey = {TUD-CS-2016-1450},
	research_area = {Ubiquitous Knowledge Processing, UKP-DIPF},
	research_sub_area = {UKP_reviewed, UKP_a_DLinNLP},
	abstract = {We analyze the performance of encoder-decoder neural models and compare
them with well-known established methods. The latter represent different
classes of traditional approaches that are applied to the monotone
sequence-to-sequence tasks OCR post-correction, spelling correction,
grapheme-to-phoneme conversion, and lemmatization.
Such tasks are of practical relevance for various higher-level research
fields including \textit{digital humanities}, automatic text correction,
and speech recognition. 
We investigate how well generic deep-learning approaches adapt to these
tasks, and how they perform in comparison with established and more
specialized methods, including our own adaptation of pruned CRFs. },
	pdf = {file:32200},
}
```
