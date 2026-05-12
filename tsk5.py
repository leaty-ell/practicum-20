class RomanNumber:
    """
    A class representing Roman numerals that can be initialized with either
    a Roman numeral string or an integer.
    
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
            value (str | int): Either a Roman numeral string or an integer 
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
        """
        Return the Roman numeral equivalent of the number.
        
        Returns:
            str | None: The Roman numeral string, or None if the number is invalid.
        """
        return self.rom_value
    
    def decimal_number(self) -> int | None:
        """
        Return the decimal equivalent of the Roman numeral.
        
        Returns:
            int | None: The decimal value, or None if the Roman numeral is invalid.
        """
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
        """
        Convert Roman numeral to decimal (internal use).
        
        Args:
            roman (str): The Roman numeral string.
        
        Returns:
            int: The decimal equivalent of the Roman numeral.
        """
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
        """
        Convert decimal to Roman numeral (internal use).
        
        Args:
            decimal (int): The decimal number (1-3999).
        
        Returns:
            str: The Roman numeral representation.
        """
        result = ""
        remaining = decimal
        
        for symbol, value in RomanNumber.roman_map:
            while remaining >= value:
                result += symbol
                remaining -= value
        
        return result
    
    def __str__(self) -> str:
        """
        Return string representation of the Roman numeral.
        
        Returns:
            str: The rom_value if it exists, otherwise an empty string.
        """
        return str(self.rom_value) if self.rom_value is not None else ''
    
    def __repr__(self) -> str:
        """
        Return a detailed string representation for debugging.
        
        Returns:
            str: The rom_value or 'None' as a string representation.
        """
        return str(self.rom_value) if self.rom_value is not None else 'None'


def main() -> None:
    """
    The main function demonstrating the RomanNumber class functionality.
    """
    num_1 = RomanNumber(214)
    print(num_1.int_value)         
    print(num_1.roman_number())     
    print(num_1.rom_value)          
    print(num_1)                   
    
    num_2 = RomanNumber(5690)     
    print(num_2.int_value)         
    
    num_3 = RomanNumber('DXCVI')
    print(num_3.int_value)       
    print(num_3.rom_value)         
    print(num_3)                  
    
    print(RomanNumber.is_int(-614))  
    print(RomanNumber.is_int(3758))  


if __name__ == "__main__":
    main()
