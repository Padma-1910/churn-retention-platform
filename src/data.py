import pandas as pd
from src.config import RAW_DATA

def load_raw() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA)