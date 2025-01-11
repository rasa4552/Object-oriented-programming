# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Abra:
    def __init__(self, Abra_mana: int, Abra_manacost: int):
        if not Abra_mana > 0:
            raise ValueError
        self.Abra_mana = Abra_mana

        if Abra_manacost < 0:
            raise ValueError
        if Abra_manacost < Abra_mana:
            raise ValueError
        self.Abra_manacost = Abra_manacost

    def is_Abra(self) -> bool:
        """
        Функция которая проверяет является ли Абра аброй
        :return: Является ли объект стаканом или нет
        """
        ...
    def add_mana_to_pool(self, mana: int) -> int:
        """
        Возврат маны в резерв.
        Если количество добавляемой маны превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемой маны
        :return: Объем непоместившейся маны
        """
        ...
class CadAbra:
    def __init__(self, CadAbra_mana: int, CadAbra_manacost: int):
        if not CadAbra_mana > 0:
            raise ValueError
        self.CadAbra_mana = CadAbra_mana

        if CadAbra_manacost < 0:
            raise ValueError
        if CadAbra_manacost < CadAbra_mana:
            raise ValueError
        self.CadAbra_manacost = CadAbra_manacost

    def is_CadAbra(self) -> bool:
        """
        Функция которая проверяет является ли Абра аброй
        :return: Является ли объект стаканом или нет
        """
        ...

    def add_mana_to_pool(self, mana: int) -> int:
        """
        Возврат маны в резерв.
        Если количество добавляемой маны превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемой маны
        :return: Объем непоместившейся маны
        """
        ...


class Avada:
    def __init__(self, Avada_mana: int, Avada_manacost: int):
        if not Avada_mana > 0:
            raise ValueError
        self.Avada_mana = Avada_mana

        if Avada_manacost < 0:
            raise ValueError
        if Avada_manacost < Avada_mana:
            raise ValueError
        self.Avada_manacost = Avada_manacost

    def is_Avada(self) -> bool:
        """
        Функция которая проверяет является ли Абра аброй
        :return: Является ли объект стаканом или нет
        """
        ...

    def add_mana_to_pool(self, mana: int) -> int:
        """
        Возврат маны в резерв.
        Если количество добавляемой маны превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемой маны
        :return: Объем непоместившейся маны
        """
        ...

if __name__ == "__main__":
    Abra1 = Abra(50, 100)
    CadAbra1 = CadAbra(32, 100)
    Avada1 = Avada(400, 500)


    print(Abra1.Abra_mana, Abra1.Abra_manacost)

    print(CadAbra1.CadAbra_mana, CadAbra1.CadAbra_manacost)

    print(Avada1.Avada_mana, Avada1.Avada_manacost)


    pass
