from tmx2dataframe import tmx2dataframe

def test_tmx2dataframe_metadata(): 
    metadata, df = tmx2dataframe.read('tests/example0.tmx')
    assert metadata['srclang'] == 'zul-ZA'

def test_tmx2dataframe_dataframe(): 
    metadata, df = tmx2dataframe.read('tests/example0.tmx')

    assert 'zul-ZA' in df.columns
    assert 'eng-GB' in df.columns

    assert len(df) == 2
    assert df.iloc[0]['eng-GB'] == "freedom of artistic creativity;"

def test_tmx2dataframe_differentattributename(): 
    metadata, df = tmx2dataframe.read('tests/example.1.tmx')

    assert 'zul-ZA' in df.columns
    assert 'eng-GB' in df.columns

    assert len(df) == 2
    assert df.iloc[0]['eng-GB'] == "freedom of artistic creativity;"

def test_multi_locales():
    metadata, df = tmx2dataframe.read('tests/example2_multi_locales.tmx')

    assert 'zul-ZA' in df.columns
    assert 'eng-GB' in df.columns
    assert 'tel-IN' in df.columns

    assert len(df) == 2
    assert df.iloc[0]['eng-GB'] == "freedom of artistic creativity;"
    assert df.iloc[0]['zul-ZA'] == "inkululeko yokwakha izinto ngokusebenzisa ubuciko;"
    assert df.iloc[0]['tel-IN'] == "కళాత్మక సృజనాత్మకత స్వేచ్ఛ;"
