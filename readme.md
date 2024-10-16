# Jérôme plays with AI ideas

This repo started with me trying out the [Hugging Face NLP course](https://huggingface.co/learn/nlp-course). As always, things quickly started
to grow and deserved being managed in a repo.

Don't expect anything particularly dependable here, this is just me toying 
around. If you end up looking at this repo, it's probably more that I'm needing help from you rather than the other way round...

## Setup

This project uses conda to manage its dependencies

```
conda env create -f ai-play-conda.yml
conda activate ai-play
```

note: to update yml, run `conda env export >ai-play-conda.yml`

## GMail export classification

To kick off this experiment, a summary is generated for each mail. This will process a maximum 
of 100 mails for now, as that's enough to already see problems appear...
```
python . mcls
```
The mails are expected at `~/Downloads/Takeout/all-mails.mbox`.


## Hugging Face NLP examples

To run sample 8, for example, use:
```
python . nlpt 8
```

## GMail export parsing example

 (WIP) Reads a gmail export (in .MBOX format), and builds a [DuckDB](https://duckdb.org) database 
indexing addresses and labels.

The file must be at `~/Downloads/Takeout/all-mails.mbox`.

```
python . mtst
```

