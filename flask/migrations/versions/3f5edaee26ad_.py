"""empty message

Revision ID: 3f5edaee26ad
Revises: d315663b2b52
Create Date: 2022-03-30 13:36:43.634630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f5edaee26ad'
down_revision = 'd315663b2b52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###
