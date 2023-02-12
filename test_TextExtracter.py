
from TextExtracter import TextExtracter
import pytest
import os
from TextExtracter import get_all_filetype_paths

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

def test_extracting_text_with_pypdf_creates_new_file_in_same_directory(setup):
    setup.extract_text_pypdf()
    assert os.path.exists("test_dir/TEST_pypdf.txt") == True
    # teardown()

def test_extracting_text_with_pdfplumber_creates_new_file_in_same_directory(setup):
    setup.extract_text_pdfplumber()
    assert os.path.exists("test_dir/TEST_pdfplumber.txt") == True

def test_getting_all_pdf_files_in_directory():
    root_dir = "test_dir"
    pdf_paths = [
        "test_dir/TEST.pdf",
        "test_dir/test_dir_depth2/TEST_2.pdf",
        "test_dir/test_dir_depth2/test_dir_depth3/TEST_3.pdf"
    ]

    assert get_all_filetype_paths(root_dir, ".pdf") == pdf_paths