"""empty message

Revision ID: ced800acd7f8
Revises: 
Create Date: 2024-03-21 21:27:18.120411

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ced800acd7f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed', sa.Boolean(), nullable=True))
        batch_op.drop_column('date_completed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_completed', mysql.DATETIME(), nullable=True))
        batch_op.drop_column('completed')

    # ### end Alembic commands ###
