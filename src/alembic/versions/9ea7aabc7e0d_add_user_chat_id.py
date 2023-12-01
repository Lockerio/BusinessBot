"""Add user chat_id

Revision ID: 9ea7aabc7e0d
Revises: 1cc45b0f97f2
Create Date: 2023-12-01 13:58:21.038355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ea7aabc7e0d'
down_revision: Union[str, None] = '1cc45b0f97f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('User', sa.Column('chat_id', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('User', 'chat_id')
