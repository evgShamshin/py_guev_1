def info_kwargs(**kwargs):
        [print(f'{key}: {value}') for key, value in sorted(kwargs.items())]


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')