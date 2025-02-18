This is the repositotry of GLIMPSE: Pragmatically Informative Multi-Document Summarization for Scholarly Reviews
[Paper](https://arxiv.org/abs/2406.07359) | [Code](https://github.com/icannos/glimpse-mds)

## Usage

Everything you need is in the `02_glimpse.ipynb` notebook. You can also run the following scripts:

--also for changing the configuration you can use config class inside both python file extractive and abstractive

```
python extractive.py
python abstractive.py
```

`rsasumm/` provides a python package with an implementation of RSA incremental decoding and RSA reranking of candidates.
`mds/` provides the experiment scripts and analysis for the MultiDocument Summarization task.

## Citation

If you use this code, please cite the following papers:

```@misc{darrin2024glimpsepragmaticallyinformativemultidocument,
      title={GLIMPSE: Pragmatically Informative Multi-Document Summarization for Scholarly Reviews},
      author={Maxime Darrin and Ines Arous and Pablo Piantanida and Jackie CK Cheung},
      year={2024},
      eprint={2406.07359},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.07359},
}
```
