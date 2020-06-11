"""
The objective of this Python program is to compare two columns and output the difference. 

Three assumptions regarding this program:

    1. Each column is stored in a single flat text file with the following format:
        ColumnHeader
        Value1
        Value2
        ...

    2. Column values can be either integer or string. There are no mixed value types in one single
    column file. Integer column has the column header starts with "Int_" and string column starts
    with "Str_", e.g.

    3. The difference of two columns is outputted into a separate text file with header "CompareResult":
        - For integer columns, the difference is the difference of two values.
        - For string columns, use a "T" if two strings match each other and use a "F" if they do not
        match, ignore case.
"""

class Column:
    """Column class that stores and compares data between two parsed text files."""

    def __init__(self, filepath):
        """
        Parameters
        ----------
        filepath: str
            Name of input source file 
        """
        
        with open(filepath) as f:
            f = f.read().split("\n")
            self.rows = f[1:]
    
    @classmethod
    def fromType(cls, filepath):
        """Segregates a Column class into a subclass based on its data type.
        
        Parameters
        ----------
        filepath: str
            Name of input source file 
        """

        with open(filepath) as f:
            # Extendibility option: Change input source format here 
            f = f.read().split("\n")
            dtype = f[0].split("_")[0].lower()

            # Extendibility option: Add new data types here and define a corresponding 
            # subclass with class method, compare_line, outside of this Column class
            if dtype == "int":
                return IntColumn(filepath)
            elif dtype == "str":
                return StrColumn(filepath)
   
    @classmethod
    def compare(cls, c1, c2):
        """Compares two Column subclasses and outputs their difference to a text file.
        
        Parameters
        ----------
        c1: Column subclass
            Variable name of a Column subclass 
        c2: Column subclass
            Variable name of a Column subclass

        Raises
        ------
        TypeError
            If the Column objects are not of the same subclass type. 
        ValueError
            If the two files do not have the same number of lines/values. 
        """

        if type(c1) is not type(c2):
            raise TypeError("The two columns must be of the same type.")

        if len(c1.rows) != len(c2.rows):
            raise ValueError("The two files must have the same number of lines.")
        
        # Extendibility option: Change output source name here 
        with open("compare_result.txt", "w") as f:
            f.write("CompareResult\n")
            
            for x1, x2 in zip(c1.rows, c2.rows):
                line = type(c1).compare_line(x1, x2)
                # Extendibility option: Change output source format here 
                f.write(line + "\n")

        print("Output stored in compare_result.txt\n")

    @classmethod
    def compare_line(cls, l1, l2):
        pass

class IntColumn(Column):

    @classmethod
    def compare_line(cls, l1, l2):
        """Outputs the difference of two column values.

        Parameters
        ----------
        l1: str
            Column #1 value 
        l2: str
            Column #2 value 
            
        Returns
        -------
        int
            difference of l1 and l2
        """

        return str(int(l1) - int(l2))

class StrColumn(Column):
    
    @classmethod
    def compare_line(cls, l1, l2):
        """Returns 'T' if the two column values match (case-insensitive), and 'F' elsewise.
        
        Parameters
        ----------
        l1: str
            Column #1 value 
        l2: str
            Column #2 value 
            
        Returns
        -------
        str
            'T' or 'F' 
        """

        if l1.casefold() == l2.casefold():
            return "T"
        else:
            return "F"

a = Column.fromType("input1_int.txt") 
b = Column.fromType("input2_int.txt") 
c = Column.fromType("input1_str.txt")
d = Column.fromType("input2_str.txt") 

Column.compare(a, b)
# Column.compare(c, d)