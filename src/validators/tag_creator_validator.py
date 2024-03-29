from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import \
    HttpUnprocessableEntity


def tag_creator_validator(request: any) -> None:
    print(request.json)
    body_validator = Validator({
        'product_code': {'type': 'string', 'required': True, 'empty': False}
    })

    response = body_validator.validate(request.json)
    if response is False:
        # raise ValueError(body_validator.errors)
        raise HttpUnprocessableEntity(body_validator.errors)
