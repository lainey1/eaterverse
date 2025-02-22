"""empty message

Revision ID: 10e75d298727
Revises: 69cbd7a58a11
Create Date: 2024-12-29 16:39:12.019186

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '10e75d298727'
down_revision = '69cbd7a58a11'
branch_labels = None
depends_on = None


def upgrade():
    schema = os.environ.get("SCHEMA") if environment == "production" else None
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema=schema
    )


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###


    op.drop_table('review_images')
    # ### end Alembic commands ###
