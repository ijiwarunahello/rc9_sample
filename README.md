# rc9 sample

## Env

- Python3.10.8

## Library

```bash
pip install pywin32
```

## How To Use

### move_sample.py

ロボットをあらかじめティーチングした位置に移動させるスクリプト

移動する順番: P0(原位置)→P1→P0

```bash
python move_sample.py
```

### variable_sample.py

ロボットコントローラ内の変数を読み出すスクリプト

読み出す変数: I0

```bash
python variable_sample.py
```

出力例: `I0: 999.9`
