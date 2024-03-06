def create_file(file_path):
    # פתיחת הקובץ לכתיבה
    with open(file_path, 'w') as file:
        # כתיבת תוכן לקובץ
        file.write("Hello, this is the content of the file.\n")
        file.write("my name is elian\n")    
        file.write("bla bla Hello is")

    print(f"File '{file_path}' has been created and written to.")

def read_file(file_path):
    # פתיחת הקובץ לקריאה
    with open(file_path, 'r') as file:
        # קריאת תוכן הקובץ
        file_contents = file.read()

    # פיצול תוכן הקובץ לרשימת מילים
    word_list = file_contents.split()

    return word_list

def count_and_print_words(word_list):
    word_count = {}

    # ספירת מופעי כל מילה
    for word in word_list:
        # עדכון של הספירה במילון
        word_count[word] = word_count.get(word, 0) + 1

    # הדפסת הספירה ממוינת
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_word_count:
        print(f'{word}: {count}')

# שלב 1
file_path_step1 = 'file_text.txt'
create_file(file_path_step1)

# שלב 2
file_path_step2 = 'file_text.txt'
word_list_step2 = read_file(file_path_step2)
print("list of names:", word_list_step2)

# שלב 3
count_and_print_words(word_list_step2)
