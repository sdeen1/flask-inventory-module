"""item table

Revision ID: 233ef722f4e9
Revises: 
Create Date: 2023-08-12 18:16:35.993703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '233ef722f4e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('available', sa.Integer(), nullable=True),
    sa.Column('halfDay', sa.String(length=8), nullable=True),
    sa.Column('day', sa.String(length=8), nullable=True),
    sa.Column('week', sa.String(length=8), nullable=True),
    sa.Column('month', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_item_name'), ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_item_name'))

    op.drop_table('item')
    # ### end Alembic commands ###