from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


# регистрируем новый фильтр
@register.filter
# судя по английской документации это шаблон-декоратор для фильтров,
# которые в свой аргумент должны принимать исключительно строку,
# т.е. он сначала перегонит всё в текст, а уже потом загонит в censor
@stringfilter
def censor(text) -> str:
    """Фильтр для цензуры некультурных слов.

    text - то, что будем проверять на ругательства.

    Фильтр возвращает отфильтрованную цензурой строку. Будь то текст, название статьи, комментарий и т.д."""

    bad_words = ['редиска', 'идиот', 'тыжпрограммист']

    # если в наше слово из текста входит плохое слово, то применяем магию
    for bad_word in bad_words:
        for word in text.split():
            if bad_word in word.lower():
                censored_template = str(word[0] + "*" * (len(bad_word) - 1) + word[(len(bad_word)):])
                text = text.replace(word, censored_template)

    return text
