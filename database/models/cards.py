# Local
from database.core import Connection
from database.models.accounts import Account


class Card:
    """Object from db. Cards"""

    id: int
    ccv: str
    number: str
    account: Account
    is_active: str
    date_end: str
    pin: str

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        account: Account,
        cvv: str,
        date_end: str,
        is_active: str,
        pin: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    number,
                    account_id,
                    cvv,
                    date_end,
                    is_active,
                    pin
                )
                VALUES (
                    '{number}',
                    '{account.id}',
                    '{cvv}',
                    '{date_end}',
                    '{is_active}',
                    '{pin}'
                )
                """
            )