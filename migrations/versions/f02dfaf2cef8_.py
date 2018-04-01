"""empty message

Revision ID: f02dfaf2cef8
Revises: c91264c833c2
Create Date: 2018-04-01 13:54:27.143109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f02dfaf2cef8'
down_revision = 'c91264c833c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', mysql.VARCHAR(length=200), nullable=False))
    # ### end Alembic commands ###
