import re


def process_message(message, response_array, response):
    # Divide el mensaje y la puntuación en una matriz
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Puntúa la cantidad de palabras en el mensaje
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

   
    # Devuelve la respuesta y la puntuación de la respuesta.
    # print (puntuación, respuesta)
    return [score, response]


def get_response(message):
    # Agregue sus respuestas personalizadas aquí
    response_list = [
        process_message(message, ['hola', 'que', 'hey'], 'Bienvenido!'),
        process_message(message, ['adios', 'Adios'], 'Hasta la vista puto!'),
        process_message(message, ['como', 'estas', 'tu'], 'Yo estoy súper bien, gracias!'),
        process_message(message, ['llamas', 'nombre','tu'], 'Mi nombre es Rardo, y mi papá es Luis Cardozo!'),
        process_message(message, ['ayuda', 'porfavor'], 'Claro soy tu asistente dime que pasá!'),
        process_message(message, ['puedes', 'hacer'], 'Soy un bot muy sarcastico, puedo hacer tu tarea si quieres.'),
        process_message(message, ['investiga','youtube'],'https://www.youtube.com/'),
        process_message(message, ['google','investigar'],'https://www.google.com/'),
        process_message(message, ['hello motherfack','chingate'],'Chingas a tu madre!'),
        process_message(message, ['oh wow','seguro?','encerio'],'Naaaa como crees que hare tu tarea wey, nmms'),
        # Agrega más respuestas aquí
    ]

    # Comprueba todas las puntuaciones de respuesta y devuelve la mejor respuesta coincidente.
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Obtenga el valor máximo para la mejor respuesta y guárdelo en una variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Devolver la respuesta coincidente al usuario
    if winning_response == 0:
        bot_response = 'No entendí lo que escribiste. '
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Prueba tu sistema
# get_response ('¿Cómo te llamas bruv?')
# get_response ('¿Me pueden ayudar con algo, por favor?')
