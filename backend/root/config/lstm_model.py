from pydantic.dataclasses import dataclass
import os

@dataclass
class Config:
    scale_cols = ['Close', 'Befo', 'Diff', 'Updown', 'Volume']                                 # 변수   /  'Open', 'High', 'Low',
    cols = ['close', 'befo', 'diff', 'updown', 'volume']                                       # 'open', 'high', 'low',
    WINDOW_SIZE = 16                                                                       # 다음날 예측에 사용할 현재일로부터 ~ 과거 데이터 개수

    LOAD_WEIGHT_FILE = 'Batch16_window16_dense5_lr0.004_128_128_16_ep03_soft.h5'
    WEIGHT_FILE = os.path.join('root/file', LOAD_WEIGHT_FILE)
    FORECAST = 16 # 앞으로 예측할 날 수


def conf():
    return Config

