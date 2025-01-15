import __init__
from models.database import engine
from models.model import subscription, Payments
from sqlmodel import Session, select
from datetime import date, datetime
import matplotlib.pyplot as plt

class subscription_service:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription

    def _is_id(self, id):
        with Session(self.engine) as session:
            statement = select(subscription).where(subscription.id==id)
            result = session.exec(statement).one()
        return result

    def list_all(self):
        with Session(self.engine) as session:
            statement = select(subscription)
            results = session.exec(statement).all()
        return results
    
    def delete(self, id):
        with Session(self.engine) as session:
            statement = select(Payments).where(Payments.subscription_id == id)
            results = session.exec(statement).all()
            for result in results:
                session.delete(result)
            statement2 = select(subscription).where(subscription.id == id)
            result2 = session.exec(statement2).one()
            session.delete(result2)
            session.commit()
    
    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False

    def pay(self, example: subscription):
        with Session(self.engine) as session:
            statement = select(Payments).join(subscription).where(subscription.empresa==example.empresa)
            results = session.exec(statement).all()
            if self._has_pay(results):
                question = input('Essa conta já foi paga neste mês, deseja pagá-la novamente? (Responda com Y ou N): ')
                if not question.upper() == 'Y':
                    return
            pay = Payments(subscription_id=example.id, date=date.today())
            session.add(pay)
            session.commit()
            print('Pagamento adicionado com sucesso!')

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(subscription)
            results = session.exec(statement).all()
        total = 0
        for result in results:
            total += result.valor
        return float(total)

    def _get_last_12_months_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_months = []
        for i in range(12):
            last_12_months.append((month, year))
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        return last_12_months[::-1]

    def _get_values_for_months(self, last_12_months):
        with Session(self.engine) as session:
            statement = (select(Payments, subscription).join(subscription, subscription.id == Payments.subscription_id))
            results = session.exec(statement).all()
            value_for_months = []
            for i in last_12_months:
                value = 0
                for payment, sub in results:
                    if payment.date.month == i[0] and payment.date.year == i[1]:
                        value += float(sub.valor)
                value_for_months.append(value)
            return value_for_months

    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_months = self._get_values_for_months(last_12_months)
        last_12_months2 = []
        for i in last_12_months:
            last_12_months2.append(i[0])
        plt.plot(last_12_months2, values_for_months)
        plt.show()