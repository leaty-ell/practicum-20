class RomanNumber:
    """
    A class representing Roman numerals that supports arithmetic operations.
    
    Class Attributes:
        roman_map (list): A list of tuples mapping Roman symbols to their decimal values.
    """
    
    roman_map = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    
    def __init__(self, value) -> None:
        """
        Initialize a RomanNumber object with either a Roman numeral string or an integer.
        
        Args:
            value (str | int): Either a Roman numeral string or an integer.
        """
        if isinstance(value, str):
            if RomanNumber.is_roman(value):
                self.rom_value = value
                self.int_value = RomanNumber._roman_to_decimal(value)
            else:
                print("ошибка")
                self.rom_value = None
                self.int_value = None
        elif isinstance(value, int):
            if RomanNumber.is_int(value):
                self.int_value = value
                self.rom_value = RomanNumber._decimal_to_roman(value)
            else:
                print("ошибка")
                self.int_value = None
                self.rom_value = None
        else:
            print("ошибка")
            self.rom_value = None
            self.int_value = None
    
    def roman_number(self) -> str | None:
        """Return the Roman numeral equivalent of the number."""
        return self.rom_value
    
    def decimal_number(self) -> int | None:
        """Return the decimal equivalent of the Roman numeral."""
        return self.int_value
    
    @staticmethod
    def is_roman(value: str) -> bool:
        """
        Check if a string is a valid Roman numeral.
        
        Args:
            value (str): The string to check.
        
        Returns:
            bool: True if the string is a valid Roman numeral, False otherwise.
        """
        if not isinstance(value, str) or not value:
            return False
        
        roman_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        for ch in value:
            if ch not in roman_chars:
                return False
        
        i = 0
        while i < len(value):
            count = 1
            while i + count < len(value) and value[i] == value[i + count]:
                count += 1
            if count > 3 and value[i] != 'M':
                return False
            i += count
        
        invalid_subtractions = ['IL', 'IC', 'ID', 'IM', 'XD', 'XM',
                                'VX', 'VL', 'VC', 'VD', 'VM',
                                'LC', 'LD', 'LM', 'DM']
        for i in range(len(value) - 1):
            pair = value[i:i + 2]
            if pair in invalid_subtractions:
                return False
        
        decimal = RomanNumber._roman_to_decimal(value)
        return 1 <= decimal <= 3999
    
    @staticmethod
    def is_int(value: int) -> bool:
        """
        Check if an integer can be represented as a Roman numeral.
        
        Args:
            value (int): The integer to check.
        
        Returns:
            bool: True if the integer can be represented as a Roman numeral,
                  False otherwise (including negative numbers and zero).
        """
        if not isinstance(value, int):
            return False
        return 1 <= value <= 3999
    
    @staticmethod
    def _roman_to_decimal(roman: str) -> int:
        """Convert Roman numeral to decimal (internal use)."""
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        
        result = 0
        prev_value = 0
        
        for ch in reversed(roman):
            curr_value = values[ch]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        
        return result
    
    @staticmethod
    def _decimal_to_roman(decimal: int) -> str:
        """Convert decimal to Roman numeral (internal use)."""
        result = ""
        remaining = decimal
        
        for symbol, value in RomanNumber.roman_map:
            while remaining >= value:
                result += symbol
                remaining -= value
        
        return result
    
    @staticmethod
    def _create_result(result_int: int):
        """
        Create a RomanNumber object from an integer result.
        If the result cannot be represented as a Roman numeral, returns an invalid object.
        
        Args:
            result_int (int): The integer result of an arithmetic operation.
        
        Returns:
            RomanNumber: A RomanNumber object with the result or None values.
        """
        if RomanNumber.is_int(result_int):
            return RomanNumber(result_int)
        else:
            print("ошибка")
            obj = RomanNumber(1)  
            obj.int_value = None
            obj.rom_value = None
            return obj
    
    def __add__(self, other):
        """Addition operator."""
        if self.int_value is None or other.int_value is None:
            print("ошибка")
            return RomanNumber._create_result(1)  
        result = self.int_value + other.int_value
        return RomanNumber._create_result(result)
    
    def __sub__(self, other):
        """Subtraction operator."""
        if self.int_value is None or other.int_value is None:
            print("ошибка")
            return RomanNumber._create_result(1)
        result = self.int_value - other.int_value
        return RomanNumber._create_result(result)
    
    def __mul__(self, other):
        """Multiplication operator."""
        if self.int_value is None or other.int_value is None:
            print("ошибка")
            return RomanNumber._create_result(1)
        result = self.int_value * other.int_value
        return RomanNumber._create_result(result)
    
    def __truediv__(self, other):
        """True division operator (returns float, but we need integer for Roman)."""
        if self.int_value is None or other.int_value is None or other.int_value == 0:
            print("ошибка")
            return RomanNumber._create_result(1)
        result = self.int_value // other.int_value 
        return RomanNumber._create_result(result)
    
    def __floordiv__(self, other):
        """Floor division operator."""
        if self.int_value is None or other.int_value is None or other.int_value == 0:
            print("ошибка")
            return RomanNumber._create_result(1)
        result = self.int_value // other.int_value
        return RomanNumber._create_result(result)
    
    def __mod__(self, other):
        """Modulo operator."""
        if self.int_value is None or other.int_value is None or other.int_value == 0:
            print("ошибка")
            return RomanNumber._create_result(1)
        result = self.int_value % other.int_value
        return RomanNumber._create_result(result)
    
    def __pow__(self, other):
        """Power operator."""
        if self.int_value is None or other.int_value is None or other.int_value < 0:
            print("ошибка")
            return RomanNumber._create_result(1)
        result = self.int_value ** other.int_value
        return RomanNumber._create_result(result)
    
    # In-place operators
    def __iadd__(self, other):
        """In-place addition operator."""
        result = self + other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __isub__(self, other):
        """In-place subtraction operator."""
        result = self - other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __imul__(self, other):
        """In-place multiplication operator."""
        result = self * other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __itruediv__(self, other):
        """In-place true division operator."""
        result = self / other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __ifloordiv__(self, other):
        """In-place floor division operator."""
        result = self // other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __imod__(self, other):
        """In-place modulo operator."""
        result = self % other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __ipow__(self, other):
        """In-place power operator."""
        result = self ** other
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self
    
    def __str__(self) -> str:
        """Return string representation of the Roman numeral."""
        return str(self.rom_value) if self.rom_value is not None else ''
    
    def __repr__(self) -> str:
        """Return a detailed string representation for debugging."""
        return str(self.rom_value) if self.rom_value is not None else 'None'


def main() -> None:
    """
    The main function demonstrating the RomanNumber class with arithmetic operations.
    """
    a = RomanNumber('XI')
    b = RomanNumber('VII')
    c = a + b
    print(c)                  
    
    d = RomanNumber('XII')
    print(c - d)             
    e = RomanNumber('XXXIV')
    f = e * a
    print(f)                
    print(f / RomanNumber('II'))  
    g = f / b
    print(g.rom_value)       
    print(f // b)          
    print(f % b)               
    print(RomanNumber('II') ** RomanNumber('X'))  
    
    a -= b
    print(a)                 
    b += RomanNumber('XX')
    print(b)                   
    b /= RomanNumber('III')
    print(b)                 
    b *= a
    print(b)                 
    b /= RomanNumber('X')
    print(b)                 
    e = RomanNumber('X')
    print(e)                   
    e %= RomanNumber('II')
    print(e)                   

if __name__ == "__main__":
    main()
