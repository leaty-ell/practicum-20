class RomanNumber:
    """
    A class representing Roman numerals and their decimal equivalents.
    
    Class Attributes:
        roman_map (list): A list of tuples mapping Roman symbols to their decimal values.
    """
    
    roman_map = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    
    def __init__(self, rom_value: str) -> None:
        """
        Initialize a RomanNumber object with a Roman numeral string.
        
        Args:
            rom_value (str): The Roman numeral string (e.g., 'VI', 'XXIV').
        """
        if RomanNumber.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print("ошибка")
            self.rom_value = None
    
    def decimal_number(self):
        """
        Convert the Roman numeral to its decimal equivalent.
        
        Returns:
            int | None: The decimal value of the Roman numeral, or None if the
                        Roman numeral is invalid.
        """
        if self.rom_value is None:
            return None
        return RomanNumber._roman_to_decimal(self.rom_value)
    
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
    num_1 = RomanNumber('VI')
    print(num_1.rom_value)
    print(num_1.decimal_number())
    print(num_1)
    
    num_2 = RomanNumber('IIII')
    print(num_2.rom_value)
    
    num_3 = RomanNumber('XXIV')
    print(num_3.decimal_number())
    
    num_4 = RomanNumber('QER2')
    
    nums = []
    nums.append(num_1)
    nums.append(num_2)
    nums.append(num_3)
    nums.append(num_4)
    print(nums)
    
    print(RomanNumber.is_roman('MMMCMLXXXVI'))
    print(RomanNumber.is_roman('MMMMMLXXXVI'))


if __name__ == "__main__":
    main()
