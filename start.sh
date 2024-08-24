#!/bin/bash

cd "$(dirname "$0")"

source ~/miniforge3/etc/profile.d/conda.sh
conda avtivate venv1


python macro4_1.py &
python macro3.py &
streamlit run webUI.py &