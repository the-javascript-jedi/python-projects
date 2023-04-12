"""Create address table

Revision ID: 112940f1a549
Revises: 4cb1881f6039
Create Date: 2023-04-12 18:00:48.293066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '112940f1a549'
down_revision = '4cb1881f6039'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # pass
    op.create_table('address',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('address1',sa.String(),nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )

def downgrade() -> None:
    # pass
    op.drop_table('address')