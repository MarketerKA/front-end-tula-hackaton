import json
from django.core import serializers


def model_to_json(model_instance):
    """
    Converts a Django model instance to a JSON-serializable dictionary.

    Args:
        model_instance: A Django model instance.

    Returns:
        A JSON-serializable dictionary representing the model instance.
    """
    # Serialize the model instance to a JSON string
    serialized_data = serializers.serialize('json', [model_instance])

    # Deserialize the JSON string to a Python dictionary
    serialized_dict = json.loads(serialized_data)[0]

    # Extract the fields from the serialized dictionary
    fields = serialized_dict['fields']

    # Add the model's primary key to the dictionary
    fields['id'] = serialized_dict['pk']

    return fields