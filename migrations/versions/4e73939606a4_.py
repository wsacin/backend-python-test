"""empty message

Revision ID: 4e73939606a4
Revises: 
Create Date: 2018-01-09 01:51:56.885939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e73939606a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('password')
    op.add_column('todos', sa.Column('done', sa.Boolean()))
    op.add_column('users', sa.Column('pw_hash', sa.String(length=255)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('pw_hash')
    with op.batch_alter_table('todos') as batch_op:
        batch_op.drop_column('done')
    op.add_column('users', sa.Column('password', sa.String(length=255)))
    # ### end Alembic commands ###
