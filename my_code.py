class SplitWords:
    def split_words(self, text):

        cleaned_text = ""
        for char in text:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9') or char == ' ':
                cleaned_text += char

        new_list = []
        for word in cleaned_text.split():
            new_list.append(word)

        return new_list
sw = SplitWords()
result = sw.split_words("Happy birthday!!! to you @123")
print(result)