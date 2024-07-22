## NullClass Task 1

The first task is about loading a pretrained LSTM model trained on english french translation dataset and using it to translate a user passed sentence in `english` to `french`. The model params and configurations are saved in the folder `english_to_french_lstm_model`. The two tokenizers are saved in `english_tokenizer.json` and `french_tokenizer.json`. 

In order to run the notebook, follow the steps:

1. Create a conda environment

```bash
conda create --name nullclass python=3.9
```

2. Activate the environment

```bash
conda activate nullclass
```
3. Install cudnn plugin
```bash
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
```

4. Install tensorflow

```bash
pip install --upgrade pip
# Anything above 2.10 is not supported on the GPU on Windows Native
pip install "tensorflow<2.11" 
```



The same environment `nullclass` can be used for running notebooks for other tasks as well. Now run the notebook named `task1.ipynb`. The GUI for the task 1 is implemented in the file`gui_task1.py`.

Run the following command to launch the GUI:
```bash
python gui_task1.py
```
