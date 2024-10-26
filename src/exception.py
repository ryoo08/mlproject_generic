import sys
import logging
'''
Utilité de ce code dans un projet
Ce code permet de :

Obtenir des informations précises sur l'erreur : Il indique non seulement l’erreur, mais aussi son contexte (nom du fichier et ligne).
Faciliter le débogage : Avec des messages d’erreur détaillés, il est plus facile de localiser et de résoudre les problèmes.
Standardiser les erreurs : En ayant une CustomException, toutes les erreurs peuvent être gérées de manière uniforme dans le projet.

'''

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0} line number[{1}] error message [{2}]] ".format(
        file_name, exc_tb.tb_lineno, str(error)

    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

