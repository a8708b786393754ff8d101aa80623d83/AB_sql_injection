import concurrent.futures
import requests 

def is_error(resp: requests.Response, failed: str) -> bool: 
    """Regarde si il ya un message d'erruer

    Args:
        resp (requests.Response): reponse de la requete
        failed (str): message d'erruer de connexion

    Returns:
        bool: True si il y a le message d'erruer, False si il'y en a pas.
    """

    return failed in resp.text

def successful_injection(resp_one: str, resp_two: str) -> bool: 
    """Verifie si le contenue de la page sans paylaod est la meme que celle avec le payload, 
    si c'est pas la meme,c'est que l'injection a reussi

    Args:
        resp_one (str): contenue de la page avant le payload
        resp_two (str): contenue de la page avec le payload

    Returns:
        bool: True si la reponse avec le payload n'est pas la meme que sans payload, False si c'est la meme
    """
    
    return resp_two != resp_one


def before_last_lenght_file_element(file_name: str) -> tuple:
    """  
    Remove the last 2 digits of the file length
    Args:
        file_name (str): name file  

    Returns:
        list : content file 
        int  : ast 2 digits of the file length 
    """

    elements = []
    try:
        with open(file_name, encoding="utf-8") as file_wordlists:
            elements = file_wordlists.readlines()
    except UnicodeDecodeError:
        with open(file_name, encoding="ISO-8859-1") as file_wordlists:
            elements = file_wordlists.readlines()

    try:
        return elements, int(str(len(elements))[:-2])
    except ValueError:
        return elements, len(elements)


def calcul(length_content: int, operator: int) -> int:
    """
    Calculate on how much to cut the contents of the file
    Args:
        length_content (int): lenght content file 
        operator (int): before_last_lenght_file_element function result

    Returns:
        int : result calcul cutt parts 
    """

    calcul = int
    if length_content > 1000000:  # Million
        calcul = length_content//10000

    elif length_content > 100000:  # cent mille
        calcul = length_content//operator//1.8

    elif length_content > 10000:  # dix mille
        calcul = length_content//operator//2

    elif length_content > 1000:  # mille
        calcul = length_content//operator//3

    if calcul == 0:
        return operator

    return int(calcul)


def cutt(_list: list, result_calcul: int) -> None:
    """
    Generator function which returns the elements of the file
    Args:
        _list (list): list content file 
        result_calcul (int): result of calcul function

    Yields:
        str : line on file 
    """

    start = result_calcul
    while (result_calcul < len(_list)):
        yield _list[result_calcul:result_calcul+start]
        result_calcul += start


def thread_executor(funct, elements: list, number_thread: int) -> None:
    """
    Function that executes the thread
    Args:
        element (list): lines of file 
        funct ([type]): function for execute on thread
        number_thread (int): number of thread.
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=number_thread) as executor:
        executor.map(funct, elements)
