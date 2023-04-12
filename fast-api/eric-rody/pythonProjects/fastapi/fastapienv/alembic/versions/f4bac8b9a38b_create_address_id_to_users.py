"""create address_id to users

Revision ID: f4bac8b9a38b
Revises: 112940f1a549
Create Date: 2023-04-12 18:13:10.406907

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f4bac8b9a38b'
down_revision = '112940f1a549'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # pass
    op.add_column("users",sa.Column('address_id',sa.Integer(),nullable=True))
    op.create_foreign_key('address_users_fk',source_table="users",referent_table="address",local_cols=['address_id']
                          ,remote_cols=["id"],ondelete="CASCADE")

def downgrade() -> None:
    # pass
    op.drop_constraint('address_users_fk',table_name="users")
    op.drop_column("users","address_id")