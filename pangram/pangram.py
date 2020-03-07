def is_pangram(sentence):
    try:
        if len(sentence) < 26:
            return False
        else:
            checker = []
            for i in range(26):
                checker.append(False)
            
            for letter in sentence.lower():
                # Using Unicode number representation for index calculation
                ind = ord(letter) - ord('a')
                if 0 <= ind <= 27:
                    checker[ind] = True
            
            # Missing character check
            for x in checker:
                if x == False:
                    # Where ord('a') could be replaced with 97, it's a constant
                    print('La lettre %s est absente.' % (chr(x + ord('a'))))
                    return False
            return True
        
    except IndexError as i:
        print(i)
        return False
    except TypeError as e:
        print(e)
        return False
    pass
