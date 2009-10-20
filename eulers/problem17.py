below_20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen',
                'fourteen', 'fifteen', 'sixteen', 'seventeen',
                'eighteen', 'nineteen']
tys = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
       'seventy', 'eighty', 'ninety']
hundred = ['hundred']
thousand = ['onethousand']

       
def problem17():
    """Return letters would be needed to write all the numbers in words from 1 to 1000"""
    result = len(thousand[0])
    for num in range(1, 1000):
        divident1, remainder1 = divmod(num, 100)
        number_in_words = divident1 and below_20[divident1]+hundred[0] or ''
        
        if remainder1:
            number_in_words = divident1 and number_in_words+'and' or number_in_words
            if remainder1 < 20:
                number_in_words = number_in_words + below_20[remainder1]
            else:
                divident2, remainder2 = divmod(remainder1, 10)
                number_in_words = number_in_words+tys[divident2]
                number_in_words = remainder2 and number_in_words+ below_20[remainder2] or number_in_words

        result = result + len(number_in_words)

    return result

print problem17()
