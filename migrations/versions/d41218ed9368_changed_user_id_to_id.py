"""changed user_id to id

Revision ID: d41218ed9368
Revises: 55752bda3276
Create Date: 2024-03-01 14:43:31.432241

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd41218ed9368'
down_revision = '55752bda3276'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('events_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['id'], ['id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('tasks_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['id'], ['id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_column('id')

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('tasks_ibfk_1', 'user', ['user_id'], ['user_id'])
        batch_op.drop_column('id')

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('events_ibfk_1', 'user', ['user_id'], ['user_id'])
        batch_op.drop_column('id')

    # ### end Alembic commands ###