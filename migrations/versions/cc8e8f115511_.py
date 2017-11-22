"""empty message

Revision ID: cc8e8f115511
Revises: 2dca19b68faa
Create Date: 2017-11-22 22:32:24.689182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc8e8f115511'
down_revision = '2dca19b68faa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projectBase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('fullName', sa.String(length=255), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('whitepaper', sa.String(length=255), nullable=True),
    sa.Column('desp', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('projectGit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('gitAddress', sa.String(length=255), nullable=True),
    sa.Column('star', sa.Integer(), nullable=True),
    sa.Column('forks', sa.Integer(), nullable=True),
    sa.Column('openIssue', sa.Integer(), nullable=True),
    sa.Column('releases', sa.Integer(), nullable=True),
    sa.Column('contributors', sa.Integer(), nullable=True),
    sa.Column('lastCommit', sa.DateTime(), nullable=True),
    sa.Column('weekCommit', sa.Integer(), nullable=True),
    sa.Column('monthCommit', sa.Integer(), nullable=True),
    sa.Column('seasonCommit', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('projectPrice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('supply', sa.String(length=255), nullable=True),
    sa.Column('currentPrice', sa.DECIMAL(), nullable=True),
    sa.Column('marketPrice', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projectPrice')
    op.drop_table('projectGit')
    op.drop_table('projectBase')
    # ### end Alembic commands ###
