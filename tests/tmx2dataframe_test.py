from tmx2dataframe import tmx2dataframe
import pandas as pd
def test_tmx2dataframe_metadata(): 
    metadata, df = tmx2dataframe.read('tests/example.tmx')
    assert metadata['srclang'] == 'zul-ZA'

def test_tmx2dataframe_dataframe(): 
    metadata, df = tmx2dataframe.read('tests/example.tmx')

    assert 'source_language' in df.columns
    assert 'source_sentence' in df.columns
    assert 'target_language' in df.columns
    assert 'target_sentence' in df.columns

    assert len(df) == 2
    df.to_csv('test.csv')
    assert df.iloc[0]['target_language'] == "eng-GB"
    assert df.iloc[0]['target_sentence'] == "freedom of artistic creativity;"

def test_tmx2dataframe_differentattributename(): 
    metadata, df = tmx2dataframe.read('tests/example.2.tmx')

    assert 'source_language' in df.columns
    assert 'source_sentence' in df.columns
    assert 'target_language' in df.columns
    assert 'target_sentence' in df.columns

    assert len(df) == 1
    assert df.iloc[0]['target_language'] == "eng-GB"
    assert df.iloc[0]['target_sentence'] == "We welcome Dr Imtiaz Sooliman of the Gift of the Givers in this house today. "