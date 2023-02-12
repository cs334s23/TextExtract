
from TextExtracter import TextExtracter
import pytest
import os

@pytest.fixture
def setup():
    textExtracter = TextExtracter("test_dir/TEST.pdf")
    return textExtracter

# def teardown():
#     dir_name = "test_dir/"
#     test_dir=os.listdir(dir_name)
#     print(test_dir)

#     for item in test_dir:
#         if item.endswith(".txt"):
#             os.remove(os.path.join(dir_name, item))

def test_get_file_path(setup):
    assert setup.get_file_path() == "test_dir/TEST.pdf"

def test_get_file_directory(setup):
    assert setup.get_file_directory() == "test_dir"

def test_get_file_type(setup):
    assert setup.get_file_type() == ".pdf"

def test_get_file_name(setup):
    assert setup.get_file_name() == "TEST"

def test_creating_valid_new_extracted_text_file_name(setup):
    library_used = "pypdf"
    assert setup.create_extracted_text_file_path(library_used) == "test_dir/TEST_pypdf.txt"
    library_used = "tika"
    assert setup.create_extracted_text_file_path(library_used) == "test_dir/TEST_tika.txt"

def test_extracting_text_creates_new_file_in_same_directory(setup):
    setup.extract_text_pypdf()
    assert os.path.exists("test_dir/TEST_pypdf.txt") == True
    # teardown()