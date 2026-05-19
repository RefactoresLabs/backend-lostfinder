from backend.app.application.services.code_generator import CodeGenerator


import re


def test_code_generator_returns_string():

    code = CodeGenerator.generate()

    assert isinstance(code, str)

def test_code_generator_has_uppercase_and_digits_only():

    pattern = re.compile(r"[A-Z0-9]+")

    code = CodeGenerator.generate()

    assert pattern.fullmatch(code) is not None