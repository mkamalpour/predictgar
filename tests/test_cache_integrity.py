import pandas as pd
import pytest
import data_pipeline as data


def test_failed_cache_write_preserves_previous_history(tmp_path, monkeypatch):
    monkeypatch.setattr(data, 'CACHE_DIR', str(tmp_path))
    cache = data.Cache(None)
    frame = pd.DataFrame({'date': pd.to_datetime(['2024-01-01']), 'price': [100]})
    assert cache.save('sample', frame)
    path = tmp_path / 'product_sample.csv'
    original = path.read_bytes()

    def broken_write(self, path, **kwargs):
        path.write_text('partial')
        raise OSError('disk full')

    monkeypatch.setattr(pd.DataFrame, 'to_csv', broken_write)
    assert cache.save('sample', frame) is False
    assert path.read_bytes() == original
    assert list(tmp_path.iterdir()) == [path]


@pytest.mark.parametrize('force', [True, False])
def test_external_refresh_preserves_cached_fallback(monkeypatch, force):
    source = data.ExternalDataSource()
    cached = pd.DataFrame({'date': pd.to_datetime(['2024-01-01']), 'value': [100]})
    monkeypatch.setattr(source, '_load_cache', lambda key: cached)
    calls = []
    monkeypatch.setattr(source, '_fetch_tgju_series', lambda symbol: calls.append(symbol))
    assert source.get('usd_irr_free', force_refresh=force) is cached
    assert len(calls) == int(force)
