class RomanNumerals:
    roman_num_dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400, 
        "C": 100, 
        "XC": 90, 
        "L": 50, 
        "XL": 40, 
        "X": 10, 
        "IX": 9, 
        "V": 5, 
        "IV": 4, 
        "I": 1 
    }
    @staticmethod
    def to_roman(val : int) -> str:        
        split_nums = []
        converted = ''
        
        count = len(str(val))-1
        for char in str(val):
            whole_num = int(char) * (10 ** count)
                
            split_nums.append(whole_num)
            count -= 1
            
        for num in split_nums:
            for key, value in RomanNumerals.roman_num_dict.items():
                if num == value:
                    converted += key
                    break
                elif num and num / int(str(num)[0]) == value:
                    for i in range(int(str(num)[0])):
                        converted += key
        converted = converted.replace('IIIII', 'V')
                
        return converted
        
        
        return test

    @staticmethod
    def from_roman(roman_num : str) -> int:
        #full string shortened one by one to find chars
        return 0