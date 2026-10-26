import numpy as np
import pandas as pd
import pytest
from model_pipeline import backtest


@pytest.mark.parametrize('overrides', [dict(horizon=0), dict(horizon=True), dict(n_folds=-1), dict(n_folds=1.5)])
def test_invalid_backtest_sizes_fail_before_training(overrides):
    args = dict(df=pd.DataFrame(), target='price', lags=[1], windows=[3], freq='D',
                detrend_method='none', selected_models=['Ridge'])
    with pytest.raises(ValueError, match='positive integer'):
        backtest(**(args | overrides))


def test_duplicate_dates_and_nonfinite_target_rejected():
    frame = pd.DataFrame(dict(date=['2026-01-01'] * 2, price=[1., 2.]))
    args = dict(target='price', lags=[1], windows=[3], freq='D', detrend_method='none', selected_models=['Ridge'])
    with pytest.raises(ValueError, match='unique'):
        backtest(frame, **args)
    frame['date'] = pd.date_range('2026-01-01', periods=2)
    frame.loc[0, 'price'] = np.nan
    with pytest.raises(ValueError, match='finite'):
        backtest(frame, **args)
