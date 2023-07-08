from datetime import date

string_variable = "i am a variable"
numeric_variable = 1

a_formatted_string_literal = f"a formatted with a {string_variable}"
print(a_formatted_string_literal)
print('\n')

a_formatted_string_literal = f"a formatted with a {numeric_variable}"
print(a_formatted_string_literal)
print('\n')

a_string_with_double_curly_brace = f"a formatted with a {{ numeric_variable }}"
print(a_string_with_double_curly_brace)
print('\n')

print("example using a conversion modifier '!r'. notice the "''" around the value showing it is a string")
a_formatted_string_with_conversion_field = f"a formatted with a {string_variable!r}"
print(a_formatted_string_with_conversion_field)
print('\n')

print("example using a format spec ':'")
today = date(year=2023, month=1, day=27)
a_formatted_string_with_format_modifier = f"today's date is {today:%Y %B %d}"
print(a_formatted_string_with_format_modifier)
print('\n')



