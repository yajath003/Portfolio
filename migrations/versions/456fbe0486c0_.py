"""empty message

Revision ID: 456fbe0486c0
Revises: 459d52bffdb2
Create Date: 2025-06-11 11:26:25.326434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456fbe0486c0'
down_revision = '459d52bffdb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('education',
    sa.Column('education_id', sa.Integer(), nullable=False),
    sa.Column('education_name', sa.String(length=500), nullable=False),
    sa.Column('start_date', sa.DATE(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('logo', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('education_id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('education_id'),
    sa.UniqueConstraint('education_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('education')
    # ### end Alembic commands ###
