def translate(text):
    translation = ''
    for char in text:
        lower_char = char.lower()
        if lower_char in 'aáàãạăắằẵặâậấầẫẩẳ':
            translation += 'A' if char.isupper() else 'a'
        elif lower_char in 'eẻẽèẹêềếéểễệ':
            translation += 'E' if char.isupper() else 'e'
        elif lower_char in 'iíìĩỉị':
            translation += 'I' if char.isupper() else 'i'
        elif lower_char in 'oòỏõọóôốồổỗộơớờởỡợ':
            translation += 'O' if char.isupper() else 'o'
        elif lower_char in 'uùúụủũưứừửữự':
            translation += 'U' if char.isupper() else 'u'
        elif lower_char in 'yýỳỷỹỵ':
            translation += 'Y' if char.isupper() else 'y'
        elif lower_char in 'đ':
            translation += 'D' if char.isupper() else 'd'
        else:
            translation += char
    return translation

text = input('Enter your word: ')
print(translate(text))
