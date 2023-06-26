"""empty message

Revision ID: 0844a71c0e59
Revises: 
Create Date: 2023-06-26 10:25:08.208481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0844a71c0e59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('twitter_link', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('instagram_link', sa.String(length=120), nullable=True))
        batch_op.drop_column('state')
        batch_op.drop_column('city')
        batch_op.drop_column('website')

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('twitter_link', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('instagram_link', sa.String(length=120), nullable=True))
        batch_op.drop_column('website')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.drop_column('instagram_link')
        batch_op.drop_column('twitter_link')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_column('instagram_link')
        batch_op.drop_column('twitter_link')

    # ### end Alembic commands ###
