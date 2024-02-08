from cerberus import Validator


body = {
    'data': {
        'elemento1': 123,
        'elemento2': 'ola mundo',
        'elemento3': 'False'
    }
}

body_validator = Validator({
    'data': {
        'type': 'dict',
        'schema': {
            'elemento1': {'type': 'integer', 'required': True, 'empty': False},
            'elemento2': {'type': 'string', 'required': True, 'empty': False},
            'elemento3': {'type': 'boolean', 'required': True, 'empty': False}
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print('Erro na validação')
    print(body_validator.errors)
else:
    print('Validação ok')
