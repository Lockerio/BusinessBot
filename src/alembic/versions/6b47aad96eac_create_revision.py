"""Create revision

Revision ID: 6b47aad96eac
Revises: 
Create Date: 2023-12-01 19:08:52.297228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b47aad96eac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('chat_id', sa.Integer, unique=True, nullable=True),
        sa.Column('first_name', sa.String, nullable=True),
        sa.Column('last_name', sa.String, nullable=True),
        sa.Column('username', sa.String, nullable=True),
        sa.Column('is_bot', sa.Boolean),
        sa.Column('registration_date', sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        'MessageTemplate',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=True),
        sa.Column('text', sa.String, nullable=True),
        sa.Column('delay_time', sa.Integer, nullable=True),
    )

    op.create_table(
        'DelayedMessage',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('User.id')),
        sa.Column('message_id', sa.Integer, sa.ForeignKey('MessageTemplate.id')),
        sa.Column('time_to_send', sa.DateTime, nullable=True),
    )


def downgrade():
    op.drop_table('DelayedMessage')
    op.drop_table('MessageTemplate')
    op.drop_table('User')
