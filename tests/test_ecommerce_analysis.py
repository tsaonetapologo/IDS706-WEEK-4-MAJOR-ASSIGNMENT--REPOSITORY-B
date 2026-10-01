from src.ecommerce_analysis import load_data, clean_data, prepare_model_data


def test_load_data():
    df = load_data()
    assert not df.empty


def test_clean_data():
    df = load_data()
    cleaned = clean_data(df)
    assert not cleaned.empty


def test_prepare_model_data():
    df = load_data()
    cleaned = clean_data(df)
    model_df = prepare_model_data(cleaned)

    assert "age" in model_df.columns
    assert "purchase_amount" in model_df.columns
    assert not model_df.empty
    assert model_df["purchase_amount"].notna().all()
    assert model_df["purchase_amount"].iloc[0] == 333.8


def test_prepare_model_data_shape():
    df = load_data()
    cleaned = clean_data(df)
    model_df = prepare_model_data(cleaned)

    assert model_df.shape[0] == 1000
    assert model_df.shape[1] == 2
