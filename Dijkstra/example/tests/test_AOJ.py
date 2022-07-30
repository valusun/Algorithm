from glob import glob
import pytest
from .. import AOJ_GRL_1_A
from io import StringIO


class Test_main:
    def test_main(self, monkeypatch, capfd):
        input_file_path = glob("tests/input/*.in")
        for file in input_file_path:
            with open(file) as f:
                inp = StringIO("".join(s for s in f.readlines()))
            output_file_path = file.replace("in", "out")
            with open(output_file_path) as f:
                ans = "".join(s for s in f.readlines())
            monkeypatch.setattr("sys.stdin", inp)
            AOJ_GRL_1_A.main()
            out, _ = capfd.readouterr()
            assert out == ans
