# Shuffling the Numbers

### Github Repo for Sourcing Data and Analytic's Statistics Project
#### Can card material affect shuffling effectiveness?

Data Collection, Experimentation, and Statistics

## Dataset

Our collected data is located in data/paper_deck_50_trials.csv and data/plastic_deck_50_trials.csv.

## Prerequisites

Python 3.10.10+, Git

## Installation

### Clone the repo

```
git clone https://github.com/dvm14/shuffling_numbers.git
cd shuffling_numbers
```

## Create and activate a virtual environment

```
python3 -m venv .venv    # Create the virtual environment
source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

## Install dependencies

```
pip install -r requirements.txt
```

## Running the Scripts

In the src file, you can fund 3 python scripts: power_analysis.py, calc_displacement.py, and stats_test.py.

power_analysis.py: calculates the sample size per groups

calc_displacement.py: converts collected card data, calculates mean displacement distance for each sample, stores data in mean_displacement.csv

stats_test.py: runs assumptions tests, statistical test, and creates visualizations of the data


```
cd src
python power_analysis.py #to run the power analysis
python calc_displacement.py #to calculate the displacement data
python stats_test.py #to run the statistical test
```