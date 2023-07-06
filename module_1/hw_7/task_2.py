def make_country(country, capital):
    dict_1 = {country: capital}
    return f"The capital of {country} is {dict_1[country]}"


print(make_country("Ukraine", "Kiev"))


"""
with **kwargs
"""


def make_country_2(**kwargs):
    return f"The capital of {kwargs.get('country_2')} is {kwargs['capital_2']}"


print(make_country_2(country_2="USA", capital_2="Washington"))
