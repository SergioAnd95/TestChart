import json
from TestChart.settings import FILE_PATH
from main.models import Group, Chart


def save_to_db(group: str, param: str, value: str):
    """
    :param group: str
    :param param: str
    :param value: str
    :return: none
    """
    group = Group.get_or_create(group)
    Chart.objects.create(region=group, param=param, value=value)


def parse():
    """
    function for parse document and save data
    :return: none
    """
    with open(FILE_PATH, 'r') as f:
        data = json.loads(f.read())['data']
        print(data)
        for line in data:
            print(line)
            save_to_db(group=line['Регион'], param=line['Страна'], value=line['Значение'])