import logging
import os
from datetime import datetime

"""
Pourquoi ce fichier est important
Ce fichier logger.py permet de :

Garder un historique d’exécution : les fichiers de log enregistrent les informations sur chaque exécution, ce qui est utile pour suivre les performances, les erreurs, et comprendre ce qui se passe dans le code.
Faciliter le débogage : les messages de log permettent de savoir où et quand un problème survient.
Améliorer la maintenance : en ayant des logs organisés, il est plus facile de diagnostiquer et résoudre les problèmes dans le projet.
En résumé, logger.py centralise la configuration de la journalisation pour l’ensemble du projet, aidant à maintenir un suivi clair des événements importants pendant l'exécution du code.

Dans un projet ML, logger.py est comme un carnet de bord qui enregistre tous les événements importants, facilite le suivi et le débogage,
 et permet d’analyser les performances pour chaque étape du projet. C'est particulièrement utile pour comprendre ce qui se passe dans 
 les coulisses de ton modèle et pour éviter les erreurs difficiles à repérer en cours de route.
"""
#Cette ligne crée un nom de fichier de log en utilisant la date et l'heure actuelles, au format MM_DD_YYYY_HH_MM_SS.log. Chaque fois que le code est exécuté, le nom du fichier est unique grâce à l’horodatage. Cela permet d'avoir un fichier de log différent pour chaque session d'exécution.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

'''
%(asctime)s : l'heure d'enregistrement du message.
%(lineno)d : le numéro de ligne dans le code.
%(name)s : le nom du logger (ici, il peut être laissé vide).
%(levelname)s : le niveau de gravité du message (INFO, ERROR, etc.).
%(message)s : le contenu du message de log.
level=logging.INFO : enregistre tous les messages d'information (INFO) et plus graves (comme ERROR).
'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, 
    
)

    
