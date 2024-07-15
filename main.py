#task1
# def compare_files(file1_path, file2_path):
#     with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
#         lines1 = file1.readlines()
#         lines2 = file2.readlines()

#     max_len = max(len(lines1), len(lines2))
#     different = False

#     for i in range(max_len):
#         line1 = lines1[i].strip() if i < len(lines1) else ""
#         line2 = lines2[i].strip() if i < len(lines2) else ""
#         if line1 != line2:
#             different = True
#             print(f"Рядок {i + 1} не співпадає:")
#             if i < len(lines1):
#                 print(f"Файл 1: {line1}")
#             if i < len(lines2):
#                 print(f"Файл 2: {line2}")

#     if not different:
#         print("Файли ідентичні.")

# file1_path = 'file1.txt'
# file2_path = 'file2.txt'
# compare_files(file1_path, file2_path)
#task2
# def generate_statistics(input_file_path, output_file_path):
#     vowels = 'aeiouAEIOU'
#     consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
#     digits = '0123456789'

#     char_count = 0
#     line_count = 0
#     vowel_count = 0
#     consonant_count = 0
#     digit_count = 0

#     with open(input_file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             line_count += 1
#             char_count += len(line)
#             for char in line:
#                 if char in vowels:
#                     vowel_count += 1
#                 elif char in consonants:
#                     consonant_count += 1
#                 elif char in digits:
#                     digit_count += 1

#     with open(output_file_path, 'w', encoding='utf-8') as file:
#         file.write(f"Кількість символів: {char_count}\n")
#         file.write(f"Кількість рядків: {line_count}\n")
#         file.write(f"Кількість голосних літер: {vowel_count}\n")
#         file.write(f"Кількість приголосних літер: {consonant_count}\n")
#         file.write(f"Кількість цифр: {digit_count}\n")

# input_file_path = 'input.txt'
# output_file_path = 'output.txt'
# generate_statistics(input_file_path, output_file_path)
#task3
# def remove_last_line(input_file_path, output_file_path):
#     with open(input_file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#     if lines:
#         lines = lines[:-1] 

#     with open(output_file_path, 'w', encoding='utf-8') as file:
#         file.writelines(lines)

# input_file_path = 'input1.txt'
# output_file_path = 'output1.txt'
# remove_last_line(input_file_path, output_file_path)
#task4
# def find_longest_line_length(file_path):
#     max_length = 0

#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             line_length = len(line.rstrip('\n'))
#             if line_length > max_length:
#                 max_length = line_length

#     return max_length

# file_path = 'input2.txt'
# longest_line_length = find_longest_line_length(file_path)
# print(f"Довжина найдовшого рядка: {longest_line_length}")
#task5
# def count_word_in_file(file_path, word):
#     word_count = 0
#     word = word.lower()  

#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
            
#             words = line.lower().split()
#             word_count += words.count(word)

#     return word_count

# file_path = 'input3.txt'
# word_to_count = input("Введіть слово для підрахунку: ")
# count = count_word_in_file(file_path, word_to_count)
# print(f"Кількість появ слова '{word_to_count}': {count}")
#task6
# def replace_word_in_file(input_file_path, output_file_path, target_word, replacement_word):
#     with open(input_file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
    
#     updated_content = content.replace(target_word, replacement_word)

#     with open(output_file_path, 'w', encoding='utf-8') as file:
#         file.write(updated_content)

# input_file_path = 'input4.txt'
# output_file_path = 'output4.txt'
# target_word = input("Введіть слово, яке потрібно знайти: ")
# replacement_word = input("Введіть слово, на яке потрібно замінити: ")

# replace_word_in_file(input_file_path, output_file_path, target_word, replacement_word)
# print(f"Слово '{target_word}' було замінено на '{replacement_word}' у файлі '{output_file_path}'.")
