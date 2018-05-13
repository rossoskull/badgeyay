"""empty message

Revision ID: cf531953b5aa
Revises: 60f668afadb7
Create Date: 2018-05-12 19:44:26.325985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf531953b5aa'
down_revision = '60f668afadb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('password', sa.String(length=100), nullable=True),
        sa.Column('name', sa.String(length=80), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('username'))
    op.drop_table('mytable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mytable',
        sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name=u'mytable_pkey'))
    op.drop_table('User')
    # ### end Alembic commands ###