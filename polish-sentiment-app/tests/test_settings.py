from settings import Settings


def test_default_values():
    settings = Settings()
    assert settings.hf_model_name == "bardsai/twitter-sentiment-pl-base"
    assert settings.local_model_name == "twitter-sentiment-pl-base"
    assert settings.model_path == "artifacts/model"
    assert settings.tokenizer_path == "artifacts/tokenizer"
    assert settings.onnx_model_path == "artifacts/onnx"
    assert settings.onnx_model_name == "twitter-sentiment-pl-base.onnx"
