# NewsPortal
NewsPortal (module D) SkillFactory project repository.

---

12.02.23.:
- Пересоздал репозиторий для пушей в него всех изменений по итоговым и промежуточным
заданиям модуля D (Django Framework) в проекте NewsPortal.
Предыдущий репозиторий был удалён, а проект переделан заново.
- ТЗ промежуточных и итоговых заданий буду добавлять в общий каталог, разделив по директориям
с названием конкретного модуля.
- Здесь же (в README.md) буду вести лог изменений и обновлений в проекте NewsPortal.

---

18.02.23.:
Итоговое задание D3.6.

Добавлено:
- кастомный цензор-фильтр, запикивающий слова (на текущий момент): "идиот", "редиска" и "тыжпрограммист".

Вызвать нужный объект из БД для проверки фильтра можно через:
localhost/post/115

- переместил шаблоны в директорию news/templates/news (по рекомендации из Вебинара от Семёна Березовского).

---

01.03.23.:
Итоговое задание D4.7.

Т.к. в этом задании вкрутили разделение на новости и статьи, то я несколько подшаманил urls в приложении news.
Если делать по уму, то надо сносить БД и/или шаманить ещё и модели, перезапиливать миграции... Всего этого
на этом этапе уже делать как-то не хочется.

Добавлено:
- пагинация страниц с публикациями по 7 постов на страницу.
- опробовал дополнительный параметр пагинатора Orphans (сделал = 3).
Помимо этого добавил пару дополнительных указателей на страницы (первая, последняя, следующая, предыдущая).
Они реализуют такой же функционал, как и в стандартной пагинации, но просто ради практики и для закрепления
результатов.
- поиск публикаций по определённым фильтрам, которые можно комбинировать. Т.к. в ТЗ при поиске по дате сказано
сделать поиск именно по ДАТЕ публикации, то использовал просто html-тип 'date', а не 'datetime-local', этого
вполне достаточно. Поиск по названию сделан с параметром 'icontains', а по категориям с возможностью выбирать
по нескольким категориям одновременно по методу "И" (conjoined=True).
- подправил HTML-шаблоны. Пофиксил вывод статей, которые принадлежат к 0, 1 или >1 категории.
- отдельные вьюшки и формы для создания статей и новостей, у которых уже заранее определён тип публикации. У страниц
для редактирования и удаления постов я не делал в адресах разделение по типам публикаций - в таком виде это не имеет
смысла, получается просто дублирование кода (не стал удалять - закомментил).

---
