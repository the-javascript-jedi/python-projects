"""add apt num col

Revision ID: fed45d5be514
Revises: f4bac8b9a38b
Create Date: 2023-04-12 23:04:44.737935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fed45d5be514'
down_revision = 'f4bac8b9a38b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address',sa.Column('apt_num',sa.Integer(),nullable=True))


def downgrade() -> None:
    op.drop_column('address','apt_num')
