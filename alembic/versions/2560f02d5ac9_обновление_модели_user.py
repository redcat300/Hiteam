"""обновление модели User

Revision ID: 2560f02d5ac9
Revises: 0cf65cf26c1d
Create Date: 2024-10-09 12:53:02.368937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2560f02d5ac9'
down_revision: Union[str, None] = '0cf65cf26c1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'hashed_password')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
