import yfinance as yf
import pandas as pd
acao = yf.Ticker('PETR4.SA')

petrobras = acao.history(start='2022-01-01', end='2023-12-31')

