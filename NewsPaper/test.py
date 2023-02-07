"""For experiments."""


from string import Template


text = "Мама мыла раму"

template_string = Template('$prev ...')
preview_example = text[:7]
result_string = template_string.substitute(prev=preview_example)

print(result_string)
