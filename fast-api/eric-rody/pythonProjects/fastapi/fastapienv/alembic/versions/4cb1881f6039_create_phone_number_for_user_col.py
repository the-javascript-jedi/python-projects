"""create phone number for user col

Revision ID: 4cb1881f6039
Revises: 
Create Date: 2023-04-12 08:59:35.967119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb1881f6039'
down_revision = None
branch_labels = None
depends_on = None

# when we type alembic upgrade <version number> this code is executed
def upgrade() -> None:
    # pass
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))
# when we type alembic downgrade <version number> this code is executed
def downgrade() -> None:
    # pass
    op.drop_column('users','phone_number')