import re

with open('text.txt', 'r', encoding='utf-8') as file:
    file_text = file.read()


# Patterns
def getAllDates(text):
    date_pattern = r'(\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b|\b\d{4}[./]\d{2}[./]\d{2}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s+\d{4}\b)'
    return re.findall(date_pattern, text)


def getAllEmails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(email_pattern, text)


if __name__ == '__main__':
    print("Dates:", getAllDates(file_text))
    print("Emails:", getAllEmails(file_text))

#XPath, так як ідентифікатор являється найкращим вибором, то можна просто привязатись до нього

# Input для введення пошукового запиту
# //input[@id='text-input-what']

# Input для введення регіону
# //input[@id='text-input-where']
#
# Кнопка пошуку
# //button[@class='yosegi-InlineWhatWhere-primaryButton' and @type='submit']
