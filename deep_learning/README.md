# Comparison of deep learning models for virus miRNAs prediction
---
Contact: [L. Bugnon](mailto:lbugnon@sinc.unl.edu.ar), [Research Institute for Signals, Systems and Computational Intelligence, sinc(i) - UNL - CONICET](http://www.sinc.unl.edu.ar)

This directory contains the source code and data to reproduces the numerical comparison of three different machine learning models trained to predict virus miRNAs in different class imbalances, as described in:

>L. A. Bugnon, J. Raad, G.A. Merino, C. Yones, F. Ariel, D.H. Milone, Senior Member, IEEE, G. Stegmayer, "Machine learning for the discovery of new miRNAs: helping the fight against COVID-19 ", (under review)

## Installation

The experiment is self-contained in the "main.ipynb" notebook. It can easily run in a stand alone way with [Google Colaboratory](https://colab.research.google.com/), with no install requirements (just a google account and a web browser).

Otherwise, if you prefer to run in a local machine, a python>=3.6 distribution is needed. You need to install the Jupiter Notebooks package:
```bash
pip3 install notebook
```
Then all the required packages and datasets are set up following the notebook instructions.

## More details
You can find more details of the deep learning methods in the following publications: 
>C. Yones, J. Raad, L. Bugnon, D. H. Milone and G. Stegmayer, High precision in microRNA prediction: a novel genome-wide approach based on convolutional deep residual networks (under review, [DOI](https://doi.org/10.1101/2020.10.23.352179)).

>L. A. Bugnon, C. Yones, D. H. Milone and G. Stegmayer, Deep neural architectures for highly imbalanced data in bioinformatics, IEEE Transactions on Neural Networks and Learning Systems, 2019 ([DOI](https://doi.org/10.1109/tnnls.2019.2914471)).


