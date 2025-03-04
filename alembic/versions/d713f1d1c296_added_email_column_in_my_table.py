"""Added email column in my table

Revision ID: d713f1d1c296
Revises: 
Create Date: 2025-02-06 09:05:15.227637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd713f1d1c296'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.add_column('user', sa.Column('email', sa.String(length=120), nullable=False))
    op.create_table('user', sa.Column('name', sa.String(length=30), nullable=False),
                    sa.Column('email', sa.String(length=40)))

def downgrade() -> None:
    op.drop_table('user')
