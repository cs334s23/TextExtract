from pypdf import PdfReader
import pdfplumber
import os


class TextExtracter:
    def __init__(self, file_path):
        """
        This class will extract text from various file types using direct extract methodologies
        Currently there are two libraries used to extract text from a file

            'pypdf' - see extract_text_pypdf() function
            'pdfplumber' - see extract_text_pdfplumber() function


        Parameters
        ----------
        file_path : string
            The path to the file to extract text from

        """
        # relative path to file 
        self.file_path = file_path

        # directory the attachment file from
        self.file_directory = os.path.dirname(self.file_path)

        # file name (without extension/type)
        self.file_name = os.path.split(self.file_path)[-1].split(".")[0] 

        # file type (pdf, docx, doc )
        # By splitting the path on the period and getting the last element ([-1]) this is the file type
        self.file_type = "." + self.file_path.split(".")[-1]
        
    def get_file_path(self):
        """
        Returns class variable for the file_path
        """
        return self.file_path

    def get_file_directory(self):
        """
        Returns the directory that the file came from
        """
        return self.file_directory
    
    def get_file_name(self):
        """
        Returns the file_name without the file extension
        """
        return self.file_name
    
    def get_file_type(self):
        """
        Returns the file extension for a file
        """
        return self.file_type
    
    def create_extracted_text_file_path(self, library_used):
        """
        Returns the path for the extracted text file

        Format: 
            - <original_file_directory>/<original_file_name>_<extraction_library_used>.txt

        This function is used by the various extract_text functions
        """
        return f"{self.file_directory}/{self.file_name}_{library_used}.txt"

    def extract_text_pypdf(self):
        """
        Uses the 'pypdf' library
        The extract text method will use the pypdf library to extract text from a pdf
        Text contents are then written to a new txt file with the ending _pypdf.txt

        """
        library_used = "pypdf"
        with open(self.file_path, "rb") as pdf:
            reader = PdfReader(pdf)
            text = ""
            for i in range(len(reader.pages)):
                text+= reader.pages[i].extract_text()

        with open(self.create_extracted_text_file_path(library_used), "w") as extracted_text_file:
            print(text, file = extracted_text_file)

    def extract_text_pdfplumber(self):
        """
        Uses the 'pdfplumber' library
        The extract text method will use the pdfplumber library to extract text from a pdf
        Text contents are then written to new txt file with the ending _pdfplumber.txt

        """
        library_used = "pdfplumber"
        with pdfplumber.open(self.file_path) as pdf:
            text = ""
            for i in range(len(pdf.pages)):
                text+= pdf.pages[i].extract_text()
        with open(self.create_extracted_text_file_path(library_used), "w") as extracted_text_file:
            print(text, file = extracted_text_file)



    # def get_attachment_subject():
    #     #TODO Possibly the first line of the file?
    #     return ""

def get_all_filetype_paths(root_dir, file_type):
    """
    This function gets a list of all the relative file paths in a certain directory for a certain file type
    Using the os.walk method we go through each subdirectory finding all occurences of a specified file type
    
    Parameters
    --------------
    root_dir : string
        a directory to start the search from, this function will look through each subdirectory and append to an
        ongoing list of paths that contain files with `file_type` extensions

    file_type : string
        the file extension to search for
    
    Returns 
    --------------
    paths : list
        a list of paths to the found `file_type` files 

    """

    paths = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_type):
                paths.append(os.path.join(root, file))
    return paths


# Example of searching through the OSHA/ directory getting all the file paths that end in .pdf
pdf_paths_OSHA = get_all_filetype_paths("OSHA/", file_type=".pdf")
print(pdf_paths_OSHA[:4])
for osha_file in pdf_paths_OSHA[:4]: # first 5 files 
    textExtract = TextExtracter(osha_file)
    textExtract.extract_text_pypdf()
    textExtract.extract_text_pdfplumber()

