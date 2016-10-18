# PCRF-Seq2Seq

An adaptation of MarMot morphological tagger for generic sequence-to-sequence tasks.


Please use the following citation:

```
@inproceedings{	TUD-CS-2016450,
	author = {Carsten Schnober and Steffen Eger and Erik-Lân Do Dinh and Iryna Gurevych},
	title = {Still not there? Comparing Traditional Sequence-to-Sequence Models to
Encoder-Decoder Neural Networks on Monotone String Translation Tasks},
	month = dec,
	year = {2016},
	booktitle = {Proceedings of the 26th International Conference on Computational
Linguistics (COLING)},
	pages = {(to appear)},
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
}
```

> **Abstract:** We analyze the performance of encoder-decoder neural models and compare them with well-known established methods. The latter represent different classes of traditional approaches that are applied to the monotone sequence-to-sequence tasks OCR post-correction, spelling correction, grapheme-to-phoneme conversion, and lemmatization.
Such tasks are of practical relevance for various higher-level research fields including \textit{digital humanities}, automatic text correction, and speech recognition. 
We investigate how well generic deep-learning approaches adapt to these tasks, and how they perform in comparison with established and more specialized methods, including our own adaptation of pruned CRFs. 


Contact persons: 
  * Carsten Schnober, schnober@ukp.informatik.tu-darmstadt.de
  * Steffen Eger, eger@ukp.informatik.tu-darmstadt.de
  * Erik-Lân Do Dinh, dodinh@ukp.informatik.tu-darmstadt.de

http://www.ukp.tu-darmstadt.de/

http://www.tu-darmstadt.de/


Don't hesitate to send us an e-mail or report an issue, if something is broken (and it shouldn't be) or if you have further questions.

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication. 

## Project structure
**(change this as needed!)**

* `src` -- this folder contains the code and detailed instructions
* `src/data/` -- sample data from the Twitter typo corpus

## Requirements
See `src/README.md` for details!

* [Marmot](https://github.com/muelletm/cistern/) morphological tagger
* [m2m-aligner](https://github.com/letter-to-phoneme/m2m-aligner) 

## Installation and Running
See `src/README.md` for details!
 
