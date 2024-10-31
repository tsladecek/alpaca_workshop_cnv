# alpaca_workshop_cnv

## Task

Predict pathogenicity of CNVs. Output should be a binary array (see section Submission)

The optimization target is **ACCURACY**

## Data

The `/data` directory contains 3 datasets. `train` and `validation` should be used for training.
You can join them if you wish.

The label column is called `clinsig`. The `example.ipynb` contains scripts for reading the data,
so it is recommended to just extend it.

The `test` dataset is the dataset that should be predicted.

## Rules

No rules. Use whatever model / technology / approach you want. 

## Submission

Please create a sheet with the name of your group here: https://docs.google.com/spreadsheets/d/1qGXqMPoFOZACX0kW7NicKlMhtMJMz94qX0ywzjxKODg/edit?usp=sharing

The sheet should contain only one column with numbers 0 (Benign) and 1 (Pathogenic). Do not name the column

## Timeline

* 9:00 - 10:10 Your work on the problem
* 10:10 - 10:15 Short presentations (max 2-3 minutes) about the approach you used and maybe something interesting you observed
* 10:25 - 10:30 Evaluation

## Setup

Depends on what you want to use. For example, to install jupyter lab:

```bash
python3 -m venv venv
source venv/bin/activate
pip install jupyterlab pandas scikit-learn
jupyter lab
```

There is an `example.ipynb` file with some basic code for reading and saving data. Feel free to use it

## Columns

* clinsig: the label - 0 (Benign) / 1 (Pathogenic)
* chr: chromosome
* start_hg38: start position
* length: length of the cnv (all CNVs have length < 5Mbp)
* gencode_genes
* protein_coding
* pseudogenes
* mirna
* lncrna
* rrna
* snrna
* morbid_genes
* disease_associated_genes
* hi_genes
* regions_HI
* regulatory
* regulatory_enhancer
* regulatory_open_chromatin_region
* regulatory_promoter
* regulatory_promoter_flanking_region
* regulatory_ctcf_binding_site
* regulatory_tf_binding_site
* regulatory_curated
