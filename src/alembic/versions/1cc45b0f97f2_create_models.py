"""Create models

Revision ID: 1cc45b0f97f2
Revises: 
Create Date: 2023-12-01 10:59:31.276554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cc45b0f97f2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('User',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('username', sa.String(), nullable=True),
                    sa.Column('is_bot', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('MessageTemplate',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('text', sa.String(), nullable=True),
                    sa.Column('delay_time', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('DelayedMessage',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('message_id', sa.Integer(), nullable=True),
                    sa.Column('time_to_send', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['message_id'], ['MessageTemplate.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('DelayedMessage')
    op.drop_table('MessageTemplate')
    op.drop_table('User')
