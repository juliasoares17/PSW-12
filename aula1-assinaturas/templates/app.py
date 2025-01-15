import __init__
from views.view import subscription_service
from models.database import engine
from datetime import datetime
from decimal import Decimal
from models.model import subscription

class UI:
    def __init__(self):
        self.subscription_service = subscription_service(engine)

    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Adicionar pagamento
            [4] -> Valor total
            [5] -> Gastos dos últimos 12 meses
            [6] -> Sair
            ''')

            choice = int(input('Escolha uma opção: '))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.add_payment()
            elif choice == 4:
                self.total_value()
            elif choice == 5:
                self.subscription_service.gen_chart()
            else:
                break

    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data de assinatura (dd/mm/aaaa): '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))
        example = subscription(empresa = empresa, site = site, data_assinatura = data_assinatura, valor = valor)
        self.subscription_service.create(example)

    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all() 
        #ToDo: quando excluir uma assinatura, excluir/inativar todos os pagamentos dela
        print('Assinaturas disponíveis:')
        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')
        choice = int(input('Escolha a assinatura que deseja excluir: '))
        self.subscription_service.delete(choice)
        print('Assinatura excluída com sucesso!')

    def add_payment(self):
        subscriptions = self.subscription_service.list_all()
        print('Assinaturas disponíveis:')
        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')
        choice = int(input('Escolha a assinatura que deseja pagar: '))
        result = self.subscription_service._is_id(choice)
        self.subscription_service.pay(result)


    def total_value(self):
        print(f'Seu valor mensal total gasto em assinaturas é: {self.subscription_service.total_value()}')

UI().start()